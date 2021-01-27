import json
import boto3
import uuid
from botocore.exceptions import ClientError

# Delete a movie by uuid
def lambda_handler(event, context):


    # ================== inputs ================== #
    # event = {
    #   "httpMethod": "DELETE",
    #   "pathParameters": {
    #       "uuid": "5f392f4f-5d38-11eb-be85-7194ef9da28f"
    #   }
    # }
    # ============================================ #

    if ('pathParameters' not in event or event['httpMethod'] != 'DELETE'):
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Bad Request'})
        }
    
    payload = event['pathParameters']
        
    response = delete_movie_from_db(payload['uuid'])

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'The movie was deleted successfully from database'})
    }


# Delete a selected movie from DynamoDB table using it's uuid
def delete_movie_from_db(uuid):
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('movies-table')
    
    try:
        response = table.delete_item(
            Key={ 'uuid': uuid },
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response
# Notes: by default delete_item from boto3 does not return an error even if operation is performed on an Item that does not exists.
# that is why 