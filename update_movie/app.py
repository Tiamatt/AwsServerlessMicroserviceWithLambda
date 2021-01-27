import json
import boto3
import uuid
from botocore.exceptions import ClientError

# Extract movie object from request body and update it in DynamoDB table
def lambda_handler(event, context):

    # ================== inputs ================== #
    # event = {
    #     "httpMethod": "PUT",
    #     "body": {
    #         "uuid": "73481194-5d39-11eb-9e87-65cf6e771b06",
    #     	"title": "Anecdote",
    #     	"year": 1989,
    #     		"director": {
    #               "firstname": "Yefim",
    #               "lastname": "Abramov"
    #                 },
    #     	"country": "Azerbaijan"
    #     }
    # }
    # ============================================ #

    if ('body' not in event or event['httpMethod'] != 'PUT' or 'uuid' not in event['body'] or 'title' not in event['body']):
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Bad Request'})
        }
    
    updated_movie = json.loads(event['body'])
    response = update_movie_in_db(updated_movie)

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Movie was updated successfully in database'})
    }

# Update an item in DynamoDB table
def update_movie_in_db(updated_movie):

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('movies-table')
    
    try:
        response = table.put_item(Item=updated_movie)
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response