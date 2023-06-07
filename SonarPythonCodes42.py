For aws_cdk.aws_ec2.Instance and other constructs that support a connections attribute:

from aws_cdk import aws_ec2 as ec2

instance = ec2.Instance(
    self,
    "my_instance",
    instance_type=nano_t2,
    machine_image=ec2.MachineImage.latest_amazon_linux(),
    vpc=vpc
)

instance.connections.allow_from(
    ec2.Peer.any_ipv4(), # Noncompliant
    ec2.Port.tcp(22),
    description="Allows SSH from all IPv4"
)
instance.connections.allow_from_any_ipv4( # Noncompliant
    ec2.Port.tcp(3389),
    description="Allows Terminal Server from all IPv4"
)
------------------------------------------
For aws_cdk.aws_ec2.SecurityGroup

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
------------------------------------------
For aws_cdk.aws_ec2.CfnSecurityGroup

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
------------------------------------------
For aws_cdk.aws_ec2.CfnSecurityGroupIngress

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
