For aws_cdk.aws_opensearchservice.CfnDomain:

from aws_cdk.aws_opensearchservice import CfnDomain, EngineVersion
class ExampleStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        CfnDomain(self, "example",
            version=EngineVersion.OPENSEARCH_1_3
        ) # Noncompliant: enables TLS 1.0 which is a deprecated version of the protocol