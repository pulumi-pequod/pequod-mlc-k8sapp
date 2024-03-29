// *** WARNING: this file was generated by Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

// Export members:
export { ProviderArgs } from "./provider";
export type Provider = import("./provider").Provider;
export const Provider: typeof import("./provider").Provider = null as any;
utilities.lazyLoad(exports, ["Provider"], () => require("./provider"));

export { ServiceDeploymentArgs } from "./serviceDeployment";
export type ServiceDeployment = import("./serviceDeployment").ServiceDeployment;
export const ServiceDeployment: typeof import("./serviceDeployment").ServiceDeployment = null as any;
utilities.lazyLoad(exports, ["ServiceDeployment"], () => require("./serviceDeployment"));


const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "k8sapp:index:ServiceDeployment":
                return new ServiceDeployment(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("k8sapp", "index", _module)
pulumi.runtime.registerResourcePackage("k8sapp", {
    version: utilities.getVersion(),
    constructProvider: (name: string, type: string, urn: string): pulumi.ProviderResource => {
        if (type !== "pulumi:providers:k8sapp") {
            throw new Error(`unknown provider type ${type}`);
        }
        return new Provider(name, <any>undefined, { urn });
    },
});
