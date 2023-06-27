#For aws_cdk.aws_opensearchservice.CfnDomain:

from aws_cdk.aws_opensearchservice import CfnDomain

class CfnDomainStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        CfnDomain(self, "Sensitive") # Sensitive, encryption is disabled by default