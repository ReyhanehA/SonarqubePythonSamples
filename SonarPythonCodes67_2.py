#For aws_cdk.aws_sqs.CfnQueue:

from aws_cdk import (
    aws_sqs as sqs
)

class CfnQueueStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        sqs.CfnQueue( # Sensitive, unencrypted by default
            self,
            "example"
        )
