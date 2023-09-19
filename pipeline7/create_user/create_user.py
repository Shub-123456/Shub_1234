import boto3
import json

user = boto3.client('iam')

def create_user():
    response = user.create_user(
        UserName='tiger'
    )
create_user()
