For aws_cdk.aws_apigateway.DomainName:

from aws_cdk.aws_apigateway import DomainName, SecurityPolicy
class ExampleStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        DomainName(self, "example",
            domain_name="example.com",
            certificate=certificate,
            security_policy=SecurityPolicy.TLS_1_0 # Noncompliant
        )