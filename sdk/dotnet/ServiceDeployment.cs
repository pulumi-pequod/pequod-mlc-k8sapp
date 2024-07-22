// *** WARNING: this file was generated by Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pequod.K8sapp
{
    [K8sappResourceType("k8sapp:index:ServiceDeployment")]
    public partial class ServiceDeployment : global::Pulumi.ComponentResource
    {
        /// <summary>
        /// ServieDeployment IP address.
        /// </summary>
        [Output("ipAddress")]
        public Output<string> IpAddress { get; private set; } = null!;


        /// <summary>
        /// Create a ServiceDeployment resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ServiceDeployment(string name, ServiceDeploymentArgs args, ComponentResourceOptions? options = null)
            : base("k8sapp:index:ServiceDeployment", name, args ?? new ServiceDeploymentArgs(), MakeResourceOptions(options, ""), remote: true)
        {
        }

        private static ComponentResourceOptions MakeResourceOptions(ComponentResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new ComponentResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/pulumi-pequod/pequod-mlc-k8sapp",
            };
            var merged = ComponentResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
    }

    public sealed class ServiceDeploymentArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Allocate an IP address for the service.
        /// </summary>
        [Input("allocateIpAddress")]
        public Input<bool>? AllocateIpAddress { get; set; }

        /// <summary>
        /// Docker image to deploy.
        /// </summary>
        [Input("image", required: true)]
        public Input<string> Image { get; set; } = null!;

        /// <summary>
        /// Using minikube.
        /// </summary>
        [Input("isMinikube")]
        public Input<bool>? IsMinikube { get; set; }

        /// <summary>
        /// K8s namespace in which to deploy.
        /// </summary>
        [Input("namespace", required: true)]
        public Input<string> Namespace { get; set; } = null!;

        /// <summary>
        /// Container port.
        /// </summary>
        [Input("port")]
        public Input<double>? Port { get; set; }

        /// <summary>
        /// Number of replicas to deploy.
        /// </summary>
        [Input("replicas")]
        public Input<double>? Replicas { get; set; }

        public ServiceDeploymentArgs()
        {
        }
        public static new ServiceDeploymentArgs Empty => new ServiceDeploymentArgs();
    }
}
