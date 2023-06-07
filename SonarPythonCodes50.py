from aws_cdk.aws_iam import PolicyStatement, Effect

PolicyStatement(
    effect=Effect.ALLOW,
    actions=["*"], # Sensitive
    resources=["arn:aws:iam:::user/*"]
)