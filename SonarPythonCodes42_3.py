#For aws_cdk.aws_ec2.CfnSecurityGroup

from aws_cdk import aws_ec2 as ec2

ec2.CfnSecurityGroup(
    self,
    "cfn-based-security-group",
    group_description="cfn based security group",
    group_name="cfn-based-security-group",
    vpc_id=vpc.vpc_id,
    security_group_ingress=[
        ec2.CfnSecurityGroup.IngressProperty( # Noncompliant
            ip_protocol="6",
            cidr_ip="0.0.0.0/0",
            from_port=22,
            to_port=22
        ),
        ec2.CfnSecurityGroup.IngressProperty( # Noncompliant
            ip_protocol="tcp",
            cidr_ip="0.0.0.0/0",
            from_port=3389,
            to_port=3389
        ),
        { # Noncompliant
            "ipProtocol":"-1",
            "cidrIpv6":"::/0"
        }
    ]
)