#For aws_cdk.aws_ec2.SecurityGroup

from aws_cdk import aws_ec2 as ec2
security_group = ec2.SecurityGroup(
    self,
    "custom-security-group",
    vpc=vpc
)

security_group.add_ingress_rule(
    ec2.Peer.any_ipv4(), # Noncompliant
    ec2.Port.tcp_range(1, 1024)
)