from aws_cdk.aws_iam import Effect, PolicyDocument, PolicyStatement

PolicyDocument(
    statements=[
        PolicyStatement(
            effect=Effect.ALLOW,
            actions=["lambda:UpdateFunctionCode"],
            resources=["*"]  # Noncompliant
        )
    ]
)