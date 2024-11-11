import json
import boto3

# connection URL (i.e. backend URL)
URL = "https://s8xnksme9e.execute-api.ap-northeast-1.amazonaws.com/dev"
gatewayapi = boto3.client("apigatewaymanagementapi", endpoint_url=URL)


def lambda_handler(event, context):
    # fetching connectionId from event
    connectionId = event["requestContext"].get("connectionId")

    # loading JSON message
    msg = json.loads(event["body"])
    
    if "id" in msg:
        #client=boto3.client("dynamodb")
        msg=msg["message"]
        id=msg["id"]
        post_message1(id,msg);
        
        

    # check if message key exist in payload
    elif "message" in msg:
        client = boto3.client("dynamodb")
        response=client.scan(TableName="websocket")
        doctor=client.scan(TableName="websocket",AttributesToGet=['connectionid'],Limit=1)
        items=doctor['Items']
        
        doctorid=items[0].get('connectionid').get('S')
        
        # fetching client message
        msg = msg["message"]
        
        if float(msg)<=29 :
            # response from server
            r_msg = "paracetamol is prescribed"
            # posts message to connected client
            client.put_item(TableName="hospital", Item={"temperature": {"S":msg},"Medicine":{"S":r_msg}})
            r_msg="3"
            for connection in response["Items"]:
                if connection["connectionid"]["S"]!=connectionId:
                        response = gatewayapi.post_to_connection(ConnectionId=connection["connectionid"]["S"], Data=json.dumps({"message": r_msg,"id":connectionId}))
            #post_message(doctorid, r_msg,connectionId)
            # return statuscode
            return {"statusCode": 200}

        elif 30<=float(msg)<=31:
            r_msg = "Crocin is prescribed"
            client.put_item(TableName="hospital", Item={"temperature": {"S":msg},"Medicine":{"S":r_msg}})
            r_msg="4"
            for connection in response["Items"]:
                if connection["connectionid"]["S"]!=connectionId:
                        response = gatewayapi.post_to_connection(ConnectionId=connection["connectionid"]["S"], Data=json.dumps({"message":r_msg,"id":connectionId}))
            #post_message(doctorid, r_msg,connectionId)
            return {"statusCode": 200}

        elif 31<float(msg):
            r_msg = "go for a check up and take dolo-650"
            client.put_item(TableName="hospital", Item={"temperature": {"S":msg},"Medicine":{"S":r_msg}})
            r_msg="5"
            for connection in response["Items"]:
                if connection["connectionid"]["S"]!=connectionId:
                        response = gatewayapi.post_to_connection(ConnectionId=connection["connectionid"]["S"], Data=json.dumps({"message":r_msg,"id":connectionId}))
            #post_message(doctorid, r_msg,connectionId)
            # closing the connection from server
            #response = gatewayapi.delete_connection(ConnectionId=connectionId)
            return {"statusCode": 200}

        # if 99<=int(msg)<=101 :
        #     # response from server
        #     r_msg = "paracetamol is prescribed"
        #     # posts message to connected client
        #     client.put_item(TableName="hospital", Item={"temperature": {"S":msg},"Medicine":{"S":r_msg}})
        #     r_msg="3"
        #     post_message(doctorid, r_msg,connectionId)
        #     # return statuscode
        #     return {"statusCode": 200}

        # elif 101<int(msg)<=104:
        #     r_msg = "Crocin is prescribed"
        #     client.put_item(TableName="hospital", Item={"temperature": {"S":msg},"Medicine":{"S":r_msg}})
        #     r_msg="4"
        #     post_message(doctorid, r_msg,connectionId)
        #     return {"statusCode": 200}

        # elif 104<int(msg)<=108:
        #     r_msg = "go for a check up and take dolo-650"
        #     client.put_item(TableName="hospital", Item={"temperature": {"S":msg},"Medicine":{"S":r_msg}})
        #     r_msg="5"
        #     post_message(doctorid, r_msg,connectionId)
        #     # closing the connection from server
        #     #response = gatewayapi.delete_connection(ConnectionId=connectionId)
        #     return {"statusCode": 200}
        # else:
        #     r_msg = "Thanks!"
        #     post_message(connectionId, r_msg)
        #     # closing the connection from server
        #     response = gatewayapi.delete_connection(ConnectionId=connectionId)
        #     return {"statusCode": 200}
        #client = boto3.client("dynamodb")
        #client.put_item(TableName="punith_temperature", Item={"temperature": {"S":msg},"Medicine":{"S":r_msg}})    
    else:
        # handling if message does not exist
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Message does not exist!"}),
        }


def post_message(doctorid, msg,connectionId):
    gateway_resp = gatewayapi.post_to_connection(
        ConnectionId=doctorid, Data=json.dumps({"message": msg,"id":connectionId})
    )
def post_message1(connectionId, msg):
    gateway_resp = gatewayapi.post_to_connection(
        ConnectionId=connectionId, Data=json.dumps({"message": msg})
    )    