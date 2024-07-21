# coding=utf-8
# *** WARNING: this file was generated by Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ServiceDeploymentArgs', 'ServiceDeployment']

@pulumi.input_type
class ServiceDeploymentArgs:
    def __init__(__self__, *,
                 image: pulumi.Input[str],
                 namespace: pulumi.Input[str],
                 allocation_ip_address: Optional[pulumi.Input[bool]] = None,
                 is_minikube: Optional[pulumi.Input[bool]] = None,
                 port: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 replicas: Optional[pulumi.Input[float]] = None,
                 resources: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a ServiceDeployment resource.
        :param pulumi.Input[str] image: Docker image to deploy.
        :param pulumi.Input[str] namespace: K8s namespace in which to deploy.
        :param pulumi.Input[bool] allocation_ip_address: Allocate an IP address for the service.
        :param pulumi.Input[bool] is_minikube: Using minikube.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] port: Container ports.
        :param pulumi.Input[float] replicas: Number of replicas to deploy.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] resources: Resource requirements for the container.
        """
        pulumi.set(__self__, "image", image)
        pulumi.set(__self__, "namespace", namespace)
        if allocation_ip_address is not None:
            pulumi.set(__self__, "allocation_ip_address", allocation_ip_address)
        if is_minikube is not None:
            pulumi.set(__self__, "is_minikube", is_minikube)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if replicas is not None:
            pulumi.set(__self__, "replicas", replicas)
        if resources is not None:
            pulumi.set(__self__, "resources", resources)

    @property
    @pulumi.getter
    def image(self) -> pulumi.Input[str]:
        """
        Docker image to deploy.
        """
        return pulumi.get(self, "image")

    @image.setter
    def image(self, value: pulumi.Input[str]):
        pulumi.set(self, "image", value)

    @property
    @pulumi.getter
    def namespace(self) -> pulumi.Input[str]:
        """
        K8s namespace in which to deploy.
        """
        return pulumi.get(self, "namespace")

    @namespace.setter
    def namespace(self, value: pulumi.Input[str]):
        pulumi.set(self, "namespace", value)

    @property
    @pulumi.getter(name="allocationIpAddress")
    def allocation_ip_address(self) -> Optional[pulumi.Input[bool]]:
        """
        Allocate an IP address for the service.
        """
        return pulumi.get(self, "allocation_ip_address")

    @allocation_ip_address.setter
    def allocation_ip_address(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allocation_ip_address", value)

    @property
    @pulumi.getter(name="isMinikube")
    def is_minikube(self) -> Optional[pulumi.Input[bool]]:
        """
        Using minikube.
        """
        return pulumi.get(self, "is_minikube")

    @is_minikube.setter
    def is_minikube(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_minikube", value)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Container ports.
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter
    def replicas(self) -> Optional[pulumi.Input[float]]:
        """
        Number of replicas to deploy.
        """
        return pulumi.get(self, "replicas")

    @replicas.setter
    def replicas(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "replicas", value)

    @property
    @pulumi.getter
    def resources(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource requirements for the container.
        """
        return pulumi.get(self, "resources")

    @resources.setter
    def resources(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "resources", value)


class ServiceDeployment(pulumi.ComponentResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allocation_ip_address: Optional[pulumi.Input[bool]] = None,
                 image: Optional[pulumi.Input[str]] = None,
                 is_minikube: Optional[pulumi.Input[bool]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 replicas: Optional[pulumi.Input[float]] = None,
                 resources: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Create a ServiceDeployment resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] allocation_ip_address: Allocate an IP address for the service.
        :param pulumi.Input[str] image: Docker image to deploy.
        :param pulumi.Input[bool] is_minikube: Using minikube.
        :param pulumi.Input[str] namespace: K8s namespace in which to deploy.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] port: Container ports.
        :param pulumi.Input[float] replicas: Number of replicas to deploy.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] resources: Resource requirements for the container.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ServiceDeploymentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a ServiceDeployment resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ServiceDeploymentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServiceDeploymentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allocation_ip_address: Optional[pulumi.Input[bool]] = None,
                 image: Optional[pulumi.Input[str]] = None,
                 is_minikube: Optional[pulumi.Input[bool]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 replicas: Optional[pulumi.Input[float]] = None,
                 resources: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is not None:
            raise ValueError('ComponentResource classes do not support opts.id')
        else:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ServiceDeploymentArgs.__new__(ServiceDeploymentArgs)

            __props__.__dict__["allocation_ip_address"] = allocation_ip_address
            if image is None and not opts.urn:
                raise TypeError("Missing required property 'image'")
            __props__.__dict__["image"] = image
            __props__.__dict__["is_minikube"] = is_minikube
            if namespace is None and not opts.urn:
                raise TypeError("Missing required property 'namespace'")
            __props__.__dict__["namespace"] = namespace
            __props__.__dict__["port"] = port
            __props__.__dict__["replicas"] = replicas
            __props__.__dict__["resources"] = resources
            __props__.__dict__["frontend_ip"] = None
        super(ServiceDeployment, __self__).__init__(
            'k8sapp:index:ServiceDeployment',
            resource_name,
            __props__,
            opts,
            remote=True)

    @property
    @pulumi.getter(name="frontendIp")
    def frontend_ip(self) -> pulumi.Output[str]:
        """
        Frontend IP address.
        """
        return pulumi.get(self, "frontend_ip")
