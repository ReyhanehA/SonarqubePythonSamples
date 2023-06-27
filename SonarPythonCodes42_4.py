#For aws_cdk.aws_ec2.CfnSecurityGroupIngress

from aws_cdk import aws_ec2 as ec2

ec2.CfnSecurityGroupIngress( # Noncompliant
    self,
    "ingress-all-ip-tcp-ssh",
    ip_protocol="tcp",
    cidr_ip="0.0.0.0/0",
    from_port=22,
    to_port=22,
    group_id=security_group.attr_group_id
)

ec2.CfnSecurityGroupIngress( # Noncompliant
    self,
    "ingress-all-ipv6-all-tcp",
    ip_protocol="-1",
    cidr_ipv6="::/0",
    group_id=security_group.attr_group_id
)