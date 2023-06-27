#For aws_cdk.aws_elasticloadbalancing.CfnLoadBalancer:

from aws_cdk import (
    aws_elasticloadbalancing as elb
)

elb.CfnLoadBalancer(
    self,
    "elb-tcp",
    listeners=[
        elb.CfnLoadBalancer.ListenersProperty(
            instance_port="10000",
            load_balancer_port="10000",
            protocol="tcp" # Sensitive
        )
    ],
    subnets=vpc.select_subnets().subnet_ids
)

elb.CfnLoadBalancer(
    self,
    "elb-http-dict",
    listeners=[
        {
            "instancePort":"10000",
            "loadBalancerPort":"10000",
            "protocol":"http" # Sensitive
        }
    ],
    subnets=vpc.select_subnets().subnet_ids
)