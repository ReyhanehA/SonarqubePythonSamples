from aws_cdk.aws_ec2 import Volume

class EBSVolumeStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        Volume(self,
            "unencrypted-implicit",
            availability_zone="eu-west-1a",
            size=Size.gibibytes(1)
        ) # Sensitive as encryption is disabled by default