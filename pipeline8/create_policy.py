import boto3
import json

user = boto3.client('iam')
def create_policy():
    with open('pipeline8/policy.json', 'r') as f:
        policy_document = json.load(f)
    response = iam.create_policy(
        PolicyName="abcd",
        PolicyDocument=json.dumps(policy_document) 
    )
def create_user():
    response = user.create_user(
        UserName='jawan'
    )
create_user()
def attach_policy():
    response = user.attach_user_policy(
    UserName= 'boburao',
    PolicyArn='arn:aws:iam::190616427825:policy/All_Policy'
)
# attach_policy()
# create_policy()
