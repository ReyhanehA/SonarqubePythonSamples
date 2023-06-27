#For aws_cdk.aws_ec2.Instance and other constructs that support a connections attribute:

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
