// Code generated by Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package k8sapp

import (
	"context"
	"reflect"

	"github.com/pulumi-pequod/pequod-mlc-k8sapp/sdk/go/k8sapp/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type ServiceDeployment struct {
	pulumi.ResourceState
}

// NewServiceDeployment registers a new resource with the given unique name, arguments, and options.
func NewServiceDeployment(ctx *pulumi.Context,
	name string, args *ServiceDeploymentArgs, opts ...pulumi.ResourceOption) (*ServiceDeployment, error) {
	if args == nil {
		args = &ServiceDeploymentArgs{}
	}

	opts = internal.PkgResourceDefaultOpts(opts)
	var resource ServiceDeployment
	err := ctx.RegisterRemoteComponentResource("k8sapp:index:ServiceDeployment", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

type serviceDeploymentArgs struct {
	// Stack delete setting for automated purge processing.
	DeleteStack *string `pulumi:"deleteStack"`
	// Drift management setting for refresh or correction.
	DriftManagement *string `pulumi:"driftManagement"`
	// Pulumi access token to set up as a deployment environment variable if provided.
	PulumiAccessToken *string `pulumi:"pulumiAccessToken"`
	// Team to which the stack should be assigned.
	TeamAssignment *string `pulumi:"teamAssignment"`
	// Time to live time setting.
	TtlTime *float64 `pulumi:"ttlTime"`
}

// The set of arguments for constructing a ServiceDeployment resource.
type ServiceDeploymentArgs struct {
	// Stack delete setting for automated purge processing.
	DeleteStack pulumi.StringPtrInput
	// Drift management setting for refresh or correction.
	DriftManagement pulumi.StringPtrInput
	// Pulumi access token to set up as a deployment environment variable if provided.
	PulumiAccessToken pulumi.StringPtrInput
	// Team to which the stack should be assigned.
	TeamAssignment pulumi.StringPtrInput
	// Time to live time setting.
	TtlTime pulumi.Float64PtrInput
}

func (ServiceDeploymentArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*serviceDeploymentArgs)(nil)).Elem()
}

type ServiceDeploymentInput interface {
	pulumi.Input

	ToServiceDeploymentOutput() ServiceDeploymentOutput
	ToServiceDeploymentOutputWithContext(ctx context.Context) ServiceDeploymentOutput
}

func (*ServiceDeployment) ElementType() reflect.Type {
	return reflect.TypeOf((**ServiceDeployment)(nil)).Elem()
}

func (i *ServiceDeployment) ToServiceDeploymentOutput() ServiceDeploymentOutput {
	return i.ToServiceDeploymentOutputWithContext(context.Background())
}

func (i *ServiceDeployment) ToServiceDeploymentOutputWithContext(ctx context.Context) ServiceDeploymentOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ServiceDeploymentOutput)
}

// ServiceDeploymentArrayInput is an input type that accepts ServiceDeploymentArray and ServiceDeploymentArrayOutput values.
// You can construct a concrete instance of `ServiceDeploymentArrayInput` via:
//
//	ServiceDeploymentArray{ ServiceDeploymentArgs{...} }
type ServiceDeploymentArrayInput interface {
	pulumi.Input

	ToServiceDeploymentArrayOutput() ServiceDeploymentArrayOutput
	ToServiceDeploymentArrayOutputWithContext(context.Context) ServiceDeploymentArrayOutput
}

type ServiceDeploymentArray []ServiceDeploymentInput

func (ServiceDeploymentArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*ServiceDeployment)(nil)).Elem()
}

func (i ServiceDeploymentArray) ToServiceDeploymentArrayOutput() ServiceDeploymentArrayOutput {
	return i.ToServiceDeploymentArrayOutputWithContext(context.Background())
}

func (i ServiceDeploymentArray) ToServiceDeploymentArrayOutputWithContext(ctx context.Context) ServiceDeploymentArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ServiceDeploymentArrayOutput)
}

// ServiceDeploymentMapInput is an input type that accepts ServiceDeploymentMap and ServiceDeploymentMapOutput values.
// You can construct a concrete instance of `ServiceDeploymentMapInput` via:
//
//	ServiceDeploymentMap{ "key": ServiceDeploymentArgs{...} }
type ServiceDeploymentMapInput interface {
	pulumi.Input

	ToServiceDeploymentMapOutput() ServiceDeploymentMapOutput
	ToServiceDeploymentMapOutputWithContext(context.Context) ServiceDeploymentMapOutput
}

type ServiceDeploymentMap map[string]ServiceDeploymentInput

func (ServiceDeploymentMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*ServiceDeployment)(nil)).Elem()
}

func (i ServiceDeploymentMap) ToServiceDeploymentMapOutput() ServiceDeploymentMapOutput {
	return i.ToServiceDeploymentMapOutputWithContext(context.Background())
}

func (i ServiceDeploymentMap) ToServiceDeploymentMapOutputWithContext(ctx context.Context) ServiceDeploymentMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ServiceDeploymentMapOutput)
}

type ServiceDeploymentOutput struct{ *pulumi.OutputState }

func (ServiceDeploymentOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ServiceDeployment)(nil)).Elem()
}

func (o ServiceDeploymentOutput) ToServiceDeploymentOutput() ServiceDeploymentOutput {
	return o
}

func (o ServiceDeploymentOutput) ToServiceDeploymentOutputWithContext(ctx context.Context) ServiceDeploymentmentOutput {
	return o
}

type ServiceDeploymentArrayOutput struct{ *pulumi.OutputState }

func (ServiceDeploymentArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*ServiceDeployment)(nil)).Elem()
}

func (o ServiceDeploymentArrayOutput) ToServiceDeploymentArrayOutput() ServiceDeploymentArrayOutput {
	return o
}

func (o ServiceDeploymentmentArrayOutput) ToServiceDeploymentArrayOutputWithContext(ctx context.Context) ServiceDeploymentArrayOutput {
	return o
}

func (o ServiceDeploymentArrayOutput) Index(i pulumi.IntInput) ServiceDeploymentOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *ServiceDeployment {
		return vs[0].([]*ServiceDeploymentment)[vs[1].(int)]
	}).(ServiceDeploymentOutput)
}

type ServiceDeploymentMapOutput struct{ *pulumi.OutputState }

func (ServiceDeploymentMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*ServiceDeployment)(nil)).Elem()
}

func (o ServiceDeploymentMapOutput) ToServiceDeploymentMapOutput() ServiceDeploymentMapOutput {
	return o
}

func (o ServiceDeploymentMapOutput) ToServiceDeploymentMapOutputWithContext(ctx context.Context) ServiceDeploymentMapOutput {
	return o
}

func (o ServiceDeploymentMapOutput) MapIndex(k pulumi.StringInput) ServiceDeploymentOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *ServiceDeployment {
		return vs[0].(map[string]*ServiceDeployment)[vs[1].(string)]
	}).(ServiceDeploymentOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ServiceDeploymentInput)(nil)).Elem(), &ServiceDeployment{})
	pulumi.RegisterInputType(reflect.TypeOf((*ServiceDeploymentArrayInput)(nil)).Elem(), ServiceDeploymentArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*ServiceDeploymentMapInput)(nil)).Elem(), ServiceDeploymentMap{})
	pulumi.RegisterOutputType(ServiceDeploymentOutput{})
	pulumi.RegisterOutputType(ServiceDeploymentArrayOutput{})
	pulumi.RegisterOutputType(ServiceDeploymentMapOutput{})
}
