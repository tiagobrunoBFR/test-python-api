import json


def hello(event, context):
    body = {
        "message": "Test serverless api!",
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
