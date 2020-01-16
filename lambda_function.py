import json

from shared import *
from hello_world import *

def lambda_handler(event, context):
    # TODO implement
    
     
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
