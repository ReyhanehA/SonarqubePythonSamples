For aws_cdk.aws_apigateway.Resource:

from aws_cdk import (
    aws_apigateway as apigateway
)

resource = api.root.add_resource("example")
resource.add_method(
    "GET",
    authorization_type=apigateway.AuthorizationType.NONE  # Sensitive
)
--------------------------------------------------
For aws_cdk.aws_apigatewayv2.CfnRoute:

from aws_cdk import (
    aws_apigatewayv2 as apigateway
)

apigateway.CfnRoute(
    self,
    "no-auth",
    api_id=api.ref,
    route_key="GET /test",
    authorization_type="NONE"  # Sensitive
)
