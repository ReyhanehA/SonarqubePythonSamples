#For aws_cdk.aws_elasticloadbalancing.LoadBalancer:

from aws_cdk import (
    aws_elasticloadbalancing as elb,
)

elb.LoadBalancer(
    self,
    "elb-tcp-dict",
    vpc=vpc,
    listeners=[
        {
            "externalPort":10000,
            "externalProtocol":elb.LoadBalancingProtocol.TCP, # Sensitive
            "internalPort":10000
        }
    ]
)

loadBalancer.add_listener(
    external_port=10081,
    external_protocol=elb.LoadBalancingProtocol.HTTP, # Sensitive
    internal_port=10081
)
loadBalancer.add_listener(
    external_port=10001,
    external_protocol=elb.LoadBalancingProtocol.TCP, # Sensitive
    internal_port=10001
)