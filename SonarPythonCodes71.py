For aws_cdk.aws_rds.DatabaseCluster and aws_cdk.aws_rds.DatabaseInstance:

from aws_cdk import (
    aws_rds as rds
)

class DatabaseStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        rds.DatabaseCluster( # Sensitive, unencrypted by default
            self,
            "example"
        )
-------------------------------------------------------
For aws_cdk.aws_rds.CfnDBCluster and aws_cdk.aws_rds.CfnDBInstance:

from aws_cdk import (
    aws_rds as rds
)

class DatabaseStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        rds.CfnDBCluster( # Sensitive, unencrypted by default
            self,
            "example"
        )
