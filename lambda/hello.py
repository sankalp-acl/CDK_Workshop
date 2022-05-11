"""_summary_: lambda function handler for endpoint request handling
"""
import json

def handler(event, context):
    print('request: {}'.format(json.dumps(event)))
    
    return {
            'statusCode': 200,
            'headers': {
                        'Content-Type': 'text/plain'
                        },
            'body': 'Good Morning, CDK! You have hit {}\n'.format(event['path'])
            }
