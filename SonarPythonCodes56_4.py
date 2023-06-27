#For aws_cdk.aws_elasticache.CfnReplicationGroup:

from aws_cdk import (
    aws_elasticache as elasticache
)

elasticache.CfnReplicationGroup(
    self,
    "unencrypted-explicit",
    replication_group_description="a replication group",
    automatic_failover_enabled=False,
    transit_encryption_enabled=False, # Sensitive
    cache_subnet_group_name="test",
    engine="redis",
    engine_version="3.2.6",
    num_cache_clusters=1,
    cache_node_type="cache.t2.micro"
)

elasticache.CfnReplicationGroup( # Sensitive, encryption is disabled by default
    self,
    "unencrypted-implicit",
    replication_group_description="a test replication group",
    automatic_failover_enabled=False,
    cache_subnet_group_name="test",
    engine="redis",
    engine_version="3.2.6",
    num_cache_clusters=1,
    cache_node_type="cache.t2.micro"
)