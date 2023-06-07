url = "http://example.com" # Sensitive
url = "ftp://anonymous@example.com" # Sensitive
url = "telnet://anonymous@example.com" # Sensitive

import telnetlib
cnx = telnetlib.Telnet("towel.blinkenlights.nl") # Sensitive

import ftplib
cnx = ftplib.FTP("ftp.example.com") # Sensitive

import smtplib
smtp = smtplib.SMTP("smtp.example.com", port=587) # Sensitive
-------------------------------------------------------------
For aws_cdk.aws_elasticloadbalancingv2.ApplicationLoadBalancer:

from aws_cdk import (
    aws_elasticloadbalancingv2 as elbv2,
)

lb = elbv2.ApplicationLoadBalancer(
    self,
    "LB",
    vpc=vpc,
    internet_facing=True
)

lb.add_listener(
    "Listener-default",
    port=80, # Sensitive
    open=True
)
lb.add_listener(
    "Listener-http-explicit",
    protocol=elbv2.ApplicationProtocol.HTTP, # Sensitive
    port=8080,
    open=True
)
-------------------------------------------------------------
For aws_cdk.aws_elasticloadbalancingv2.ApplicationListener:

from aws_cdk import (
    aws_elasticloadbalancingv2 as elbv2,
)

elbv2.ApplicationListener(
    self,
    "listener-http-explicit-const",
    load_balancer=lb,
    protocol=elbv2.ApplicationProtocol.HTTP, # Sensitive
    port=8081,
    open=True
)
-------------------------------------------------------------
For aws_cdk.aws_elasticloadbalancingv2.NetworkLoadBalancer:

from aws_cdk import (
    aws_elasticloadbalancingv2 as elbv2,
)
lb = elbv2.NetworkLoadBalancer(
    self,
    "LB",
    vpc=vpc,
    internet_facing=True
)

lb.add_listener( # Sensitive
    "Listener-default",
    port=1234
)
lb.add_listener(
    "Listener-TCP-explicit",
    protocol=elbv2.Protocol.TCP, # Sensitive
    port=1337
)
-------------------------------------------------------------
For aws_cdk.aws_elasticloadbalancingv2.NetworkListener:

from aws_cdk import (
    aws_elasticloadbalancingv2 as elbv2,
)

elbv2.NetworkListener(
    self,
    "Listener-TCP-explicit",
    protocol=elbv2.Protocol.TCP, # Sensitive
    port=1338,
    load_balancer=lb
)
-------------------------------------------------------------
For aws_cdk.aws_elasticloadbalancingv2.CfnListener:

from aws_cdk import (
    aws_elasticloadbalancingv2 as elbv2,
)

elbv2.CfnListener(
    self,
    "listener-http",
    default_actions=[application_default_action],
    load_balancer_arn=lb.load_balancer_arn,
    protocol="HTTP", # Sensitive
    port=80
)

elbv2.CfnListener(
    self,
    "listener-tcp",
    default_actions=[network_default_action],
    load_balancer_arn=lb.load_balancer_arn,
    protocol="TCP", # Sensitive
    port=1000
)
-------------------------------------------------------------
For aws_cdk.aws_elasticloadbalancing.LoadBalancerListener:

from aws_cdk import (
    aws_elasticloadbalancing as elb,
)

elb.LoadBalancerListener(
    external_port=10000,
    external_protocol=elb.LoadBalancingProtocol.TCP, # Sensitive
    internal_port=10000
)

elb.LoadBalancerListener(
    external_port=10080,
    external_protocol=elb.LoadBalancingProtocol.HTTP, # Sensitive
    internal_port=10080
)
-------------------------------------------------------------
For aws_cdk.aws_elasticloadbalancing.CfnLoadBalancer:

from aws_cdk import (
    aws_elasticloadbalancing as elb
)

elb.CfnLoadBalancer(
    self,
    "elb-tcp",
    listeners=[
        elb.CfnLoadBalancer.ListenersProperty(
            instance_port="10000",
            load_balancer_port="10000",
            protocol="tcp" # Sensitive
        )
    ],
    subnets=vpc.select_subnets().subnet_ids
)

elb.CfnLoadBalancer(
    self,
    "elb-http-dict",
    listeners=[
        {
            "instancePort":"10000",
            "loadBalancerPort":"10000",
            "protocol":"http" # Sensitive
        }
    ],
    subnets=vpc.select_subnets().subnet_ids
)
-------------------------------------------------------------
For aws_cdk.aws_elasticloadbalancing.LoadBalancer:

from aws_cdk import (
    aws_elasticloadbalancing as elb,
)

elb.LoadBalancer(
    self,
    "elb-tcp-dict",
    vpc=vpc,
    listeners=[
        {
            "externalPort":10000,
            "externalProtocol":elb.LoadBalancingProtocol.TCP, # Sensitive
            "internalPort":10000
        }
    ]
)

loadBalancer.add_listener(
    external_port=10081,
    external_protocol=elb.LoadBalancingProtocol.HTTP, # Sensitive
    internal_port=10081
)
loadBalancer.add_listener(
    external_port=10001,
    external_protocol=elb.LoadBalancingProtocol.TCP, # Sensitive
    internal_port=10001
)
-------------------------------------------------------------
For aws_cdk.aws_elasticache.CfnReplicationGroup:

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
-------------------------------------------------------------
For aws_cdk.aws_kinesis.CfnStream:

from aws_cdk import (
    aws_kinesis as kinesis,
)

kinesis.CfnStream( # Sensitive, encryption is disabled by default for CfnStreams
    self,
    "cfnstream-implicit-unencrytped",
    shard_count=1
)

kinesis.CfnStream(self,
    "cfnstream-explicit-unencrytped",
    shard_count=1,
    stream_encryption=None # Sensitive
)
-------------------------------------------------------------
For aws_cdk.aws_kinesis.Stream:

from aws_cdk import (
    aws_kinesis as kinesis,
)

stream = kinesis.Stream(self,
    "stream-explicit-unencrypted",
    shard_count=1,
    encryption=kinesis.StreamEncryption.UNENCRYPTED # Sensitive
)
