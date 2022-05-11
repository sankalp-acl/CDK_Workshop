"""_summary_: creates the stack!
"""
from typing_extensions import runtime
from constructs import Construct
from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as _apigateway
)

class CdkWorkshopStack(Stack):
    """_summary_

    Args:
        Stack (_type_): creates a stack
    """

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
    
        # define a lambda function
        my_lambda = _lambda.Function(self, 'lambda-sp',
                                     runtime=_lambda.Runtime.PYTHON_3_8,
                                     code=_lambda.Code.from_asset('lambda'),
                                     handler='hello.handler')
        
        # define an API Gateway integration with lambda function
        my_api_gateway = _apigateway.LambdaRestApi(self, 'endpoint-sp',
                                                   handler=my_lambda)