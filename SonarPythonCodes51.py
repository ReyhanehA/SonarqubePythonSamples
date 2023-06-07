from aws_cdk.aws_iam import PolicyStatement, AnyPrincipal, Effect
from aws_cdk.aws_s3 import Bucket

bucket = Bucket(self, "ExampleBucket")

bucket.add_to_resource_policy(PolicyStatement(
  effect=Effect.ALLOW,
  actions=["s3:*"],
  resources=[bucket.arn_for_objects("*")],
  principals=[AnyPrincipal()] # Sensitive
))