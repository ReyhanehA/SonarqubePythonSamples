#For aws_cdk.aws_elasticloadbalancingv2.ApplicationLoadBalancer:

from aws_cdk import (
    aws_elasticloadbalancingv2 as elbv2,
)

lb = elbv2.ApplicationLoadBalancer(
    self,
    "LB",
    vpc=vpc,
    internet_facing=True
)

lb.add_listener(
    "Listener-default",
    port=80, # Sensitive
    open=True
)
lb.add_listener(
    "Listener-http-explicit",
    protocol=elbv2.ApplicationProtocol.HTTP, # Sensitive
    port=8080,
    open=True
)
