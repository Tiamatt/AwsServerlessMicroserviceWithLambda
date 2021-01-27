import json
import boto3
import decimal
from botocore.exceptions import ClientError

# get a list of all movies
def lambda_handler(event, context):
    
    response = get_movies_from_db()

    return {
        'statusCode': 200,
        'body': json.dumps(response, indent=2, default=handle_decimal_type)
    }

# Get a list of all movies from DynamoDB table
def get_movies_from_db():
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('movies-table')

    try:
        response = table.scan()
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response.get('Items', [])
        
        
# The problem is that the Dynamo Python library is converting numeric values to Decimal objects, 
# but those aren't JSON serializable by default, so json.dumps blows up. 
# You will need to provide json.dumps with a converter for Decimal objects.
def handle_decimal_type(obj):
    if isinstance(obj, decimal.Decimal):
        if float(obj).is_integer():
            return int(obj)
        else:
            return float(obj)
    raise TypeError