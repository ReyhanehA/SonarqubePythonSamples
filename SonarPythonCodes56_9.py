#For aws_cdk.aws_elasticloadbalancingv2.NetworkListener:

from aws_cdk import (
    aws_elasticloadbalancingv2 as elbv2,
)

elbv2.NetworkListener(
    self,
    "Listener-TCP-explicit",
    protocol=elbv2.Protocol.TCP, # Sensitive
    port=1338,
    load_balancer=lb
)