import * as k8s from "@pulumi/kubernetes";
import * as k8stypes from "@pulumi/kubernetes/types/input";
import * as pulumi from "@pulumi/pulumi";

/**
 * ServiceDeployment is an abstraction that uses a class to fold together the common pattern of a
 * Kubernetes Deployment and its associated Service object.
 */
export class ServiceDeployment extends pulumi.ComponentResource {
    public readonly deployment: k8s.apps.v1.Deployment;
    public readonly service: k8s.core.v1.Service;
    public ipAddress?: pulumi.Output<string>;

    constructor(name: string, args: ServiceDeploymentArgs, opts?: pulumi.ComponentResourceOptions) {
        super("pequod:k8sapp:ServiceDeployment", name, {}, opts);

        const namespace = args.namespace

        const labels = { app: name };
        const containerPort = args.port || 80;
        const container: k8stypes.core.v1.Container = {
            name,
            image: args.image,
            resources: { requests: { cpu: "100m", memory: "100Mi" } },
            env: [{ name: "GET_HOSTS_FROM", value: "dns" }],
            ports: [{ containerPort: containerPort}],
        };
        this.deployment = new k8s.apps.v1.Deployment(name, {
            metadata: {
                namespace: namespace
            },
            spec: {
                selector: { matchLabels: labels },
                replicas: args.replicas || 1,
                template: {
                    metadata: { labels: labels },
                    spec: { containers: [ container ] },
                },
            },
        }, { parent: this });

        this.service = new k8s.core.v1.Service(name, {
            metadata: {
                name: name,
                namespace: namespace,
                labels: this.deployment.metadata.labels,
            },
            spec: {
                ports: [ { port: containerPort, targetPort: containerPort}], 
                selector: this.deployment.spec.template.metadata.labels,
                // Minikube does not implement services of type `LoadBalancer`; require the user to specify if we're
                // running on minikube, and if so, create only services of type ClusterIP.
                type: args.allocateIpAddress ? (args.isMinikube ? "ClusterIP" : "LoadBalancer") : undefined,
            },
        }, { parent: this });

        console.log("args", args)
        if (args.allocateIpAddress) {
            console.log("Allocating IP address for service")
            if (args.isMinikube) {
                this.ipAddress = this.service.spec.clusterIP 
            } else {
                const ingress = this.service.status.apply(status => status.loadBalancer.ingress[0])
                ingress.apply(ingress => console.log("Ingress: ", ingress))
                this.ipAddress = ingress.apply(ingress => ingress.ip || ingress.hostname || "")
                this.ipAddress.apply(ip => console.log("Allocated IP address for service: ", ip))
            }
        }
    }
}

export interface ServiceDeploymentArgs {
    image: string;
    namespace: pulumi.Input<string> | string;
    replicas?: number;
    port?: number;
    allocateIpAddress?: boolean;
    isMinikube?: boolean;
}