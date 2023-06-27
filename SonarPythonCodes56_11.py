#For aws_cdk.aws_elasticloadbalancingv2.ApplicationListener:

from aws_cdk import (
    aws_elasticloadbalancingv2 as elbv2,
)

elbv2.ApplicationListener(
    self,
    "listener-http-explicit-const",
    load_balancer=lb,
    protocol=elbv2.ApplicationProtocol.HTTP, # Sensitive
    port=8081,
    open=True
)