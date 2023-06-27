#For aws_cdk.aws_elasticloadbalancingv2.CfnListener:

from aws_cdk import (
    aws_elasticloadbalancingv2 as elbv2,
)

elbv2.CfnListener(
    self,
    "listener-http",
    default_actions=[application_default_action],
    load_balancer_arn=lb.load_balancer_arn,
    protocol="HTTP", # Sensitive
    port=80
)

elbv2.CfnListener(
    self,
    "listener-tcp",
    default_actions=[network_default_action],
    load_balancer_arn=lb.load_balancer_arn,
    protocol="TCP", # Sensitive
    port=1000
)