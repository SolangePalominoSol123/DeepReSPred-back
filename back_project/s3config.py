#from constants import keys
import boto3
import json

#A json file is used due to allow aws credentials change after Back-end services were deployed
def gettingCredentialsFromJson():
    f = open('constants_aws.json')
    data = json.load(f)

    credentials=data['keys']
    f.close()
    return credentials

def getS3config():

    keys = gettingCredentialsFromJson()
    s3 = boto3.client('s3',
                        aws_access_key_id = keys["ACCESS_KEY_ID"],
                        aws_secret_access_key = keys["ACCESS_SECRET_KEY"],
                        aws_session_token = keys["AWS_SESSION_TOKEN"]
                    )
    return s3