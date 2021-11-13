from constants import keys
import boto3

def getS3config():
    s3 = boto3.client('s3',
                        aws_access_key_id = keys["ACCESS_KEY_ID"],
                        aws_secret_access_key = keys["ACCESS_SECRET_KEY"],
                        aws_session_token = keys["AWS_SESSION_TOKEN"]
                    )
    return s3