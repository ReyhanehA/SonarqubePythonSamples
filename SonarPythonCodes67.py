#For aws_cdk.aws_sqs.Queue:

from aws_cdk import (
    aws_sqs as sqs
)

class QueueStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        sqs.Queue( # Sensitive, unencrypted by default
            self,
            "example"
        )