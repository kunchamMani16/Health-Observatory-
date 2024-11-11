import json
import boto3

def lambda_handler(event, context):
    client = boto3.client("dynamodb")
    client.put_item(TableName="websocket", Item={"connectionid": {"S": event["requestContext"].get("connectionId")}})
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }