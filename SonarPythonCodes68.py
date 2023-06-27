#For aws_cdk.aws_sns.Topic:

from aws_cdk import (
    aws_sns as sns
)

class TopicStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        sns.Topic( # Sensitive, unencrypted by default
            self,
            "example"
        )
