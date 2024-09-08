import json
import traceback
from datetime import datetime as dt

import boto3

TABLE_NAME = ""

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(TABLE_NAME)


def lambda_handler(event, context):
    try:
        response_body = {
            "message": dt.now().strftime("%Y-%m-%d %H:%M:%S"),
            "val": "undefined",
        }

        http_method = event["httpMethod"]
        if http_method == "POST":
            if not event.get("body"):
                return {"statusCode": 400, "body": json.dumps("Bad Request missing body")}
            body = json.loads(event["body"])
            if not body.get("val"):
                return {"statusCode": 400, "body": json.dumps("Bad Request missing val")}
            result = save_value(body["val"])
            response_body["val"] = str(result)

        elif http_method == "GET":
            val = get_value()
            response_body["val"] = str(val)

        return {"statusCode": 200, "body": json.dumps(response_body)}
    except:
        return {"statusCode": 500, "body": json.dumps(str(traceback.format_exc()))}


def save_value(value):
    item = {"id": "value-item", "val": value}

    table.put_item(Item=item)
    return item["val"]


def get_value():
    response = table.get_item(Key={"id": "value-item"})
    item = response.get("Item")
    if item:
        return item.get("val")
    else:
        return None
