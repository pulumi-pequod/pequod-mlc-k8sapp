#  Copyright 2016-2020, Pulumi Corporation.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from typing import Optional, Sequence

import pulumi
from pulumi import ResourceOptions, ComponentResource, Inputs, Output
from pulumi_kubernetes.apps.v1 import Deployment, DeploymentSpecArgs
from pulumi_kubernetes.core.v1 import (
    ContainerArgs,
    ContainerPortArgs,
    PodSpecArgs,
    PodTemplateSpecArgs,
    ResourceRequirementsArgs,
    Service,
    ServicePortArgs,
    ServiceSpecArgs,
)
from pulumi_kubernetes.meta.v1 import LabelSelectorArgs, ObjectMetaArgs

class ServiceDeploymentArgs:

    allocate_ip_address: pulumi.Input[bool]
    """Whether or not to allocate an IP address for the service. Defaults to false."""
    image: pulumi.Input[str]
    """Name of the image for the application."""
    is_minikube: pulumi.Input[bool]
    """Used to indicate if minikube environment is being used. Defaults to False."""
    namespace: pulumi.Input[str]
    """K8s namespace to use."""
    container_port: pulumi.Input[int]
    """Port container listens on."""
    request_cpu: pulumi.Input[str]
    """Requested CPU. E.g. 250m means 0.25 CPU. Defaults to 100m."""
    request_memory: pulumi.Input[str]
    """Requested memory. E.g. 64Mi means 64 MiB. Defaults to 64Mi."""
    replicas: pulumi.Input[int]
    """Number of pod replicas to create. Defaults to 1."""
    target_port: pulumi.Input[int]
    """Target port for the service. Defaults to the containerPort."""

    @staticmethod
    def from_inputs(inputs: Inputs) -> 'ServiceDeploymentArgs':
        return ServiceDeploymentArgs(
            allocate_ip_address=inputs['allocateIpAddress'],
            image=inputs['image'],
            is_minikube=inputs['isMiniKube'],
            namespace=inputs['namespace'],
            container_port=inputs['containerPort'],
            request_cpu=inputs['requestCpu'],
            request_memory=inputs['requestMemory'],
            replicas=inputs['replicas'],
            target_port=inputs['targetPort']
        )

    def __init__(self, 
                 image: pulumi.Input[str],
                 namespace: pulumi.Input[str],
                 container_port: pulumi.Input[int],
                 allocate_ip_address: Optional[pulumi.Input[bool]] = None,
                 is_minikube: Optional[pulumi.Input[bool]] = None,
                 request_cpu: Optional[pulumi.Input[str]] = None,
                 request_memory: Optional[pulumi.Input[str]] = None,
                 replicas: Optional[pulumi.Input[int]] = None,
                 target_port: Optional[pulumi.Input[int]] = None,
                 ) -> None:

        self.image = image 
        self.namespace = namespace
        self.container_port = container_port
        self.allocate_ip_address = allocate_ip_address
        self.is_minikube = is_minikube
        self.request_cpu = request_cpu
        self.request_memory = request_memory
        self.replicas = replicas
        self.target_port = target_port


class ServiceDeployment(ComponentResource):
    ip_address: Output[str]

    def __init__(self, 
                 name: str, 
                 args: ServiceDeploymentArgs, 
                 props: Optional[dict] = None,
                 opts: Optional[ResourceOptions] = None) -> None:

        super().__init__('pequod:k8s:ServiceDeployment', name, props, opts)

        image = args.image
        namespace = args.namespace
        container_port = args.container_port
        allocate_ip_address = args.allocate_ip_address or False
        is_minikube = args.is_minikube or False
        request_cpu = args.request_cpu or "100m"
        request_memory = args.request_memory or "64Mi"
        replicas = args.replicas or 1
        target_port = args.target_port or container_port

        labels = {"app": name}
        container = ContainerArgs(
            name=name,
            image=args.image,
            resources=ResourceRequirementsArgs(
                requests={
                    "cpu": request_cpu,
                    "memory": request_memory
                },
            ),
            ports=[ContainerPortArgs(container_port=container_port)]
        )

        self.deployment = Deployment(
            name,
            metadata=ObjectMetaArgs(
                namespace=namespace
            ),
            spec=DeploymentSpecArgs(
                selector=LabelSelectorArgs(match_labels=labels),
                replicas=replicas, 
                template=PodTemplateSpecArgs(
                    metadata=ObjectMetaArgs(labels=labels),
                    spec=PodSpecArgs(containers=[container]),
                ),
            ),
            opts=pulumi.ResourceOptions(parent=self))

        self.service = Service(
            name,
            metadata=ObjectMetaArgs(
                name=name,
                namespace=namespace,
                labels=self.deployment.metadata.apply(lambda m: m.labels),
            ),
            spec=ServiceSpecArgs(
                ports=[ServicePortArgs(port=container_port, target_port=target_port)],
                selector=self.deployment.spec.apply(lambda s: s.template.metadata.labels),
                type=("ClusterIP" if is_minikube else "LoadBalancer") if allocate_ip_address else None,
            ),
            opts=pulumi.ResourceOptions(parent=self))

        if allocate_ip_address:
            if is_minikube:
                self.ip_address = self.service.spec.apply(lambda s: s.cluster_ip)
            else:
                ingress=self.service.status.apply(lambda s: s.load_balancer.ingress[0])
                self.ip_address = ingress.apply(lambda i: i.ip or i.hostname or "")

        self.register_outputs({})
