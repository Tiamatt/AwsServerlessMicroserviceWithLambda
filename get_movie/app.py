import json
import boto3
import decimal
from botocore.exceptions import ClientError

# get a movie based on it's uuid
def lambda_handler(event, context):

    # ================== inputs ================== #
    # event = {
    #   "httpMethod": "GET",
    #   "pathParameters": {
    #       "uuid": "8f44f626-6050-11eb-a02c-09a6e91b6550"
    #   }
    # }
    # ============================================ #
    
    if ('pathParameters' not in event or event['httpMethod'] != 'GET'):
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Bad Request'})
        }
    
    payload = event['pathParameters']
        
    response = get_movie_from_db(
        payload['uuid']
        )

    if ('Item' not in response):
        return {
            'statusCode': 404,
            'body': json.dumps({'message': 'Movie not found'})
        }

    return {
        'statusCode': 200,
        'body': json.dumps(response['Item'], indent=2, default=handle_decimal_type)
    }
   

# get a movie from DynamoDB table using it's uuid
def get_movie_from_db(uuid):
    
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('movies-table')

    try:
        response = table.get_item(Key={'uuid': uuid})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response
        
        
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