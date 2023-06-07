For aws_cdk.aws_sagemaker.CfnNotebookInstance:

from aws_cdk import (
    aws_sagemaker as sagemaker
)

class CfnSagemakerStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        sagemaker.CfnNotebookInstance(
            self, "Sensitive",
            instance_type="instanceType",
            role_arn="roleArn"
        )  # Sensitive, no KMS key is set by default; thus, encryption is disabled

