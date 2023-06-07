For aws_cdk.aws_ec2.Instance and similar constructs:

from aws_cdk import aws_ec2 as ec2

ec2.Instance(
    self,
    "vpc_subnet_public",
    instance_type=nano_t2,
    machine_image=ec2.MachineImage.latest_amazon_linux(),
    vpc=vpc,
    vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC) # Sensitive
)
-----------------------------------------------------
For aws_cdk.aws_ec2.CfnInstance:

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
-----------------------------------------------------
For aws_cdk.aws_dms.CfnReplicationInstance:

from aws_cdk import aws_dms as dms

rep_instance = dms.CfnReplicationInstance(
    self,
    "explicit_public",
    replication_instance_class="dms.t2.micro",
    allocated_storage=5,
    publicly_accessible=True, # Sensitive
    replication_subnet_group_identifier=subnet_group.replication_subnet_group_identifier,
    vpc_security_group_ids=[vpc.vpc_default_security_group]
)
-----------------------------------------------------
For aws_cdk.aws_rds.CfnDBInstance:

from aws_cdk import aws_rds as rds
from aws_cdk import aws_ec2 as ec2

rds_subnet_group_public = rds.CfnDBSubnetGroup(
    self,
    "public_subnet",
    db_subnet_group_description="Subnets",
    subnet_ids=vpc.select_subnets(
        subnet_type=ec2.SubnetType.PUBLIC
    ).subnet_ids
)

rds.CfnDBInstance(
    self,
    "public-public-subnet",
    engine="postgres",
    master_username="foobar",
    master_user_password="12345678",
    db_instance_class="db.r5.large",
    allocated_storage="200",
    iops=1000,
    db_subnet_group_name=rds_subnet_group_public.ref,
    publicly_accessible=True, # Sensitive
    vpc_security_groups=[sg.security_group_id]
)
