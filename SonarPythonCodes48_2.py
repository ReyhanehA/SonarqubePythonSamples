#For aws_cdk.aws_rds.CfnDBInstance:

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