#For aws_cdk.aws_elasticloadbalancingv2.NetworkLoadBalancer:

from aws_cdk import (
    aws_elasticloadbalancingv2 as elbv2,
)
lb = elbv2.NetworkLoadBalancer(
    self,
    "LB",
    vpc=vpc,
    internet_facing=True
)

lb.add_listener( # Sensitive
    "Listener-default",
    port=1234
)
lb.add_listener(
    "Listener-TCP-explicit",
    protocol=elbv2.Protocol.TCP, # Sensitive
    port=1337
)