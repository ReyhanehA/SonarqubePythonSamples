For aws_cdk.aws_efs.FileSystem and aws_cdk.aws_efs.CfnFileSystem:

from aws_cdk import (
    aws_efs as efs
)

efs.FileSystem(
    self,
    "example",
    encrypted=False  # Sensitive