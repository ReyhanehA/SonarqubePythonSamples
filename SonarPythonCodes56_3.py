#For aws_cdk.aws_kinesis.CfnStream:

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