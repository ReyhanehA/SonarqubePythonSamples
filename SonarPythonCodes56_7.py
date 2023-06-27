#For aws_cdk.aws_elasticloadbalancing.LoadBalancerListener:

from aws_cdk import (
    aws_elasticloadbalancing as elb,
)

elb.LoadBalancerListener(
    external_port=10000,
    external_protocol=elb.LoadBalancingProtocol.TCP, # Sensitive
    internal_port=10000
)

elb.LoadBalancerListener(
    external_port=10080,
    external_protocol=elb.LoadBalancingProtocol.HTTP, # Sensitive
    internal_port=10080
)