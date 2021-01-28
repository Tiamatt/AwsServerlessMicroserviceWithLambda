# ServerlessMicroserviceApp

This project is a simple serverless microservice on AWS that enables users to create and manage movies data. The entire backend is based on API Gateway, Lambda and DynamoDB. To manage, document and visualize all APIs in one place, SwaggerHub is used.

![SwaggerHub UI](readme-images/i-1.png)

## **Overview**

The goal of this project is to learn how to create an application composed of small, easily deployable, loosely coupled, independently scalable, serverless components.

As I’m strongly against managing environments manually and take Infrastructure as Code for granted, AWS SAM will be a great fit for our serverless application. As a result, the entire application should be deployed in any AWS account with a single CloudFormation template.

## **Architecture**

:one: A user sends a request to the server by calling APIs from SwaggerHub UI. The request which includes all necessary information is sent to Amazon API Gateway restful service.

:two: API Gateway transfers the collected user information to a Lambda function.

:three: AWS Lambda function executes event-based logic calling DynamoDB database.

:four: DynamoDB provides a persistence layer where data can be stored/retrieved by the API's Lambda function.

The high-level architecture for the serverless microservice is illustrated in the diagram below:

![Architecture](readme-images/i-2.png)

## **Initial Setup**

To codify, build, package, deploy, and manage our AWS resources in a fully automated fashion, you need to install:

:point_right: AWS SAM

:point_right: AWS Cloud​Formation

:point_right: AWS CLI

:point_right: AWS SDK for Python (boto3)

:point_right: Docker

If you don't want to install or maintain a local IDE, use AWS Cloud9 instead (you can find how to set up AWS Cloud9 [here](https://dev.to/tiamatt/serverless-create-debug-and-deploy-lambda-and-api-gateway-via-aws-sam-and-aws-cloud9-5158)). Otherwise you might need to install the latest [AWS CLI](https://aws.amazon.com/cli/), [AWS SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) and [Python](https://www.python.org/downloads/) on your development machine.

## **AWS Resources**

Here is the list of AWS resources that the project template creates:

:heavy_check_mark: AWS Lambda

:heavy_check_mark: Amazon DynamoDB

:heavy_check_mark: Amazon API Gateway

:heavy_check_mark: AWS IAM

:heavy_check_mark: Amazon S3 (that is where your CloudFormation template will be stored)

Lambda functions are written on Python 3.8.


## **Demo**

![SwaggerHub](readme-images/i-11.png)

:tada: Create a new movie:

![CreateMovie](readme-images/i-10.png)

![CreateMovie](readme-images/i-12.png)

:tada: Get a list of all movies:

![GetMovies](readme-images/i-13.png)

![GetMovies](readme-images/i-14.png)

:tada: Get a movie by uuid:

![GetMovie](readme-images/i-15.png)

![GetMovie](readme-images/i-16.png)


:tada: Delete a movie by uuid:

![DeleteMovie](readme-images/i-17.png)

![DeleteMovie](readme-images/i-18.png)

:tada: Update an existing movie:

![UpdateMovie](readme-images/i-19.png)

![UpdateMovie](readme-images/i-20.png)

![UpdateMovie](readme-images/i-21.png)


## **Article**

You can find all the details and step by step explanation of the project by reading my articles:

:point_right: **AWS project - Building a serverless microservice with Lambda**

:point_right: **Serverless - Create, debug and deploy Lambda and API Gateway via AWS SAM and AWS Cloud9** [(read)](https://dev.to/tiamatt/serverless-create-debug-and-deploy-lambda-and-api-gateway-via-aws-sam-and-aws-cloud9-5158)

## **Deploy**

To build and deploy your application for the first time, run the following in your shell:

```YAML
sam build --use-container
sam deploy --guided
```

## **Cleanup**

To delete the sample application that you created, use the AWS CLI:

```YAML
aws cloudformation delete-stack --stack-name aws-serverless-microservice-app-stack
```

## **Happy dance**

Finally, time for happy dance!

![UpdateMovie](readme-images/meme-joker-dance.png)