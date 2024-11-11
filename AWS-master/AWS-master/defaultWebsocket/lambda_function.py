import json
import boto3
URL = "https://s8xnksme9e.execute-api.ap-northeast-1.amazonaws.com/dev"
gatewayapi = boto3.client("apigatewaymanagementapi", endpoint_url=URL)
def lambda_handler(event, context):
    # TODO implement
    
    msg = json.loads(event["body"])
    
    if "id" in msg:
        id=msg["id"]
        msg=msg["message"]
        post_message1(id,msg);
        client = boto3.client("dynamodb")
        client.put_item(TableName="patient_db", Item={'patient_id' : {"S":id},"Medicine":{"S":msg}})
   
    # client = boto3.client("apigatewaymanagementapi", endpoint_url = URL)
    # dynamo = boto3.client("dynamodb")
    # connectionId = event["requestContext"].get("connectionId")
    # #msg=event["requestContext"]
    # msg = json.loads(event["body"])
    # response = dynamo.scan(TableName="websocket")
    # for connection in response["Items"]:
    #     if connection["connectionid"]["S"]!=connectionId:
    #         response = client.post_to_connection(ConnectionId=connection["connectionid"]["S"], Data=json.dumps(msg))

        
    
    return {
        'statusCode': 200,
        'body': json.dumps('Default route invoked!')
    }
def post_message1(connectionId, msg):
    gateway_resp = gatewayapi.post_to_connection(
        ConnectionId=connectionId, Data=json.dumps({"message": msg})
    )    