#For aws_cdk.aws_ec2.Volume:

from aws_cdk.aws_ec2 import Volume

class EBSVolumeStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        Volume(self,
            "unencrypted-explicit",
            availability_zone="eu-west-1a",
            size=Size.gibibytes(1),
            encrypted=False  # Sensitive
        )

