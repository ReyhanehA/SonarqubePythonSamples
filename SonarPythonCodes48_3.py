#For aws_cdk.aws_dms.CfnReplicationInstance:

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