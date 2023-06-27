#For aws_cdk.aws_ec2.CfnInstance:

from aws_cdk import aws_ec2 as ec2

ec2.CfnInstance(
    self,
    "cfn_public_exposed",
    instance_type="t2.micro",
    image_id="ami-0ea0f26a6d50850c5",
    network_interfaces=[
        ec2.CfnInstance.NetworkInterfaceProperty(
            device_index="0",
            associate_public_ip_address=True, # Sensitive
            delete_on_termination=True,
            subnet_id=vpc.select_subnets(subnet_type=ec2.SubnetType.PUBLIC).subnet_ids[0]
        )
    ]
)