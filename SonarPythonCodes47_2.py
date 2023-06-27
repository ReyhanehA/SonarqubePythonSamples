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