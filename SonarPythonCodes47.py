For aws_cdk.aws_apigateway.Resource:

from aws_cdk import (
    aws_apigateway as apigateway
)

resource = api.root.add_resource("example")
resource.add_method(
    "GET",
    authorization_type=apigateway.AuthorizationType.NONE  # Sensitive
)
