import json
import boto3

def lambda_handler(event, context):
    dynamo = boto3.client("dynamodb")
    
    URL = "https://s8xnksme9e.execute-api.ap-northeast-1.amazonaws.com/dev"
    client = boto3.client("apigatewaymanagementapi", endpoint_url = URL)
    
    msg = {"message": "Hello from server!"}
    
    response = dynamo.scan(TableName="websocket")
    for connection in response["Items"]:
        response = client.post_to_connection(ConnectionId=connection["connectionid"]["S"], Data=json.dumps(msg))
    #response = client.post_to_connection(ConnectionId="bBicBdA2BcwCFAQ=", Data=json.dumps(msg))
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }