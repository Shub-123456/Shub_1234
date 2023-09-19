import boto3
import json

user = boto3.client('iam')

def create_user():
    response = user.create_user(
        UserName='tiger'
    )
create_user()
def attach_policy():
    response = user.attach_user_policy(
    UserName= 'tiger',
    PolicyArn='arn:aws:iam::655523803653:policy/abc'
)
attach_policy()

