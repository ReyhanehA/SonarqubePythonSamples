#For aws_cdk.aws_kinesis.Stream:

from aws_cdk import (
    aws_kinesis as kinesis,
)

stream = kinesis.Stream(self,
    "stream-explicit-unencrypted",
    shard_count=1,
    encryption=kinesis.StreamEncryption.UNENCRYPTED # Sensitive
)