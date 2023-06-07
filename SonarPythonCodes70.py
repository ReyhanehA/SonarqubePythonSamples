For aws_cdk.aws_opensearchservice.Domain:

from aws_cdk.aws_opensearchservice import Domain, EngineVersion

class DomainStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        Domain(self, "Sensitive",
            version=EngineVersion.OPENSEARCH_1_3
        ) # Sensitive, encryption is disabled by default
--------------------------------------------
For aws_cdk.aws_opensearchservice.CfnDomain:

from aws_cdk.aws_opensearchservice import CfnDomain

class CfnDomainStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        CfnDomain(self, "Sensitive") # Sensitive, encryption is disabled by default

