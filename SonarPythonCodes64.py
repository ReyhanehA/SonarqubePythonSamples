#For aws_cdk.aws_ec2.SecurityGroup:

from aws_cdk import (
    aws_ec2 as ec2
)

ec2.SecurityGroup(  # Sensitive; allow_all_outbound is enabled by default
    self,
    "example",
    vpc=vpc
)
