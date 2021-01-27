import json
import boto3
import uuid
from botocore.exceptions import ClientError

# Extract movie object from request body and insert it into DynamoDB table
def lambda_handler(event, context):

    # ================== inputs ================== #
    # event = {
    #     "httpMethod": "POST",
    #     "body": {
    #     	"title": "Godfather",
    #     	"year": 1972,
    #     		"director": {
    #               "firstname": "Francis",
    #               "lastname": "Coppola"
    #                 },
    #     	"country": "United States"
    #     }
    # }
    # ============================================ #

    if ('body' not in event or event['httpMethod'] != 'POST' or 'title' not in event['body']):
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Bad Request'})
        }
    
    new_movie = json.loads(event['body'])
    response = add_movie_to_db(new_movie)
    
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'A new movie was saved successfully in database'})
    }



# Insert a new item into DynamoDB table
def add_movie_to_db(new_movie):
    
    new_movie['uuid'] = str(uuid.uuid1())

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('movies-table')
    
    try:
        response = table.put_item(Item=new_movie)
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response