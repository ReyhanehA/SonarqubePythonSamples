from OpenSSL import SSL

SSL.Context(SSL.SSLv3_METHOD)  # Noncompliant

import ssl

ssl.SSLContext(ssl.PROTOCOL_SSLv3) # Noncompliant
-------------------------------------------------------
For aws_cdk.aws_apigateway.DomainName:

from aws_cdk.aws_apigateway import DomainName, SecurityPolicy
class ExampleStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        DomainName(self, "example",
            domain_name="example.com",
            certificate=certificate,
            security_policy=SecurityPolicy.TLS_1_0 # Noncompliant
        )
-------------------------------------------------------
For aws_cdk.aws_opensearchservice.CfnDomain:

from aws_cdk.aws_opensearchservice import CfnDomain, EngineVersion
class ExampleStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        CfnDomain(self, "example",
            version=EngineVersion.OPENSEARCH_1_3
        ) # Noncompliant: enables TLS 1.0 which is a deprecated version of the protocol
