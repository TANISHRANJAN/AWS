import json
import uuid
import boto3
from datetime import datetime
import os

# Initialize DynamoDB
dynamodb = boto3.resource('dynamodb')
TABLE_NAME = os.environ.get('TABLE_NAME', 'UserSubmissions')  # DynamoDB table name
table = dynamodb.Table(TABLE_NAME)
CORS_ORIGIN = os.environ.get('CORS_ORIGIN', '*')  # For CORS

def lambda_handler(event, context):
    try:
        # Parse request body
        body = event.get('body')
        if isinstance(body, str):
            data = json.loads(body)
        else:
            data = body or {}

        name = (data.get('name') or '').strip()
        email = (data.get('email') or '').strip()
        message = (data.get('message') or '').strip()

        # Validate required fields
        if not name or not email or not message:
            return {
                "statusCode": 400,
                "headers": {
                    "Access-Control-Allow-Origin": CORS_ORIGIN,
                    "Access-Control-Allow-Methods": "OPTIONS,POST",
                    "Access-Control-Allow-Headers": "*"
                },
                "body": json.dumps({"error":"name, email and message are required"})
            }

        # Create unique submission ID
        submission_id = str(uuid.uuid4())
        now = datetime.utcnow().isoformat() + 'Z'

        # DynamoDB item (key must match table partition key)
        item = {
            "submissionId": submission_id,  # <-- must match table's primary key
            "name": name,
            "email": email,
            "message": message,
            "submissionDate": now,
            "status": "NEW"
        }

        # Insert into DynamoDB
        table.put_item(Item=item)

        # Return response with ID for frontend
        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": CORS_ORIGIN,
                "Access-Control-Allow-Methods": "OPTIONS,POST",
                "Access-Control-Allow-Headers": "*"
            },
            "body": json.dumps({
                "message": "✅ Submitted!",
                "id": submission_id   # <-- frontend can now show this ID
            })
        }

    except Exception as e:
        print("Error:", e)
        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": CORS_ORIGIN,
                "Access-Control-Allow-Methods": "OPTIONS,POST",
                "Access-Control-Allow-Headers": "*"
            },
            "body": json.dumps({"error":"Internal server error"})
        }
