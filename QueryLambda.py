import json
import boto3
import os
from boto3.dynamodb.conditions import Key, Attr

# Initialize DynamoDB
dynamodb = boto3.resource('dynamodb')
TABLE_NAME = os.environ.get('TABLE_NAME', 'UserSubmissions')
table = dynamodb.Table(TABLE_NAME)
GSI_NAME = os.environ.get('GSI_NAME', 'EmailIndex')  # Optional GSI on email
CORS_ORIGIN = os.environ.get('CORS_ORIGIN', '*')  # For CORS

def lambda_handler(event, context):
    try:
        # Get query string parameters
        params = event.get('queryStringParameters') or {}
        email = params.get('email') if params else None

        items = []

        if email:
            # Try querying using GSI first (if defined)
            try:
                resp = table.query(
                    IndexName=GSI_NAME,
                    KeyConditionExpression=Key('email').eq(email)
                )
                items = resp.get('Items', [])
            except Exception as e:
                print(f"GSI query failed: {e}. Falling back to scan.")
                # Fallback: scan table with filter
                resp = table.scan(FilterExpression=Attr('email').eq(email))
                items = resp.get('Items', [])
        else:
            # No email filter: return all items (careful if table is large)
            resp = table.scan()
            items = resp.get('Items', [])

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": CORS_ORIGIN,
                "Access-Control-Allow-Methods": "OPTIONS,GET",
                "Access-Control-Allow-Headers": "*"
            },
            "body": json.dumps(items, default=str)
        }

    except Exception as e:
        print("Error:", e)
        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": CORS_ORIGIN,
                "Access-Control-Allow-Methods": "OPTIONS,GET",
                "Access-Control-Allow-Headers": "*"
            },
            "body": json.dumps({"error":"Internal server error"})
        }
