import boto3
import json

user = boto3.client('iam')
def create_policy():
    with open('pipeline6/jenkinsfile1.json', 'r') as f:
        policy_document = json.load(f)
    response = user.create_policy(
        PolicyName="abc",
        PolicyDocument=json.dumps(policy_document) 
    )
def create_user():
    response = user.create_user(
        UserName='bob'
    )
# create_user()
def attach_policy():
    response = user.attach_user_policy(
    UserName= 'bob',
    PolicyArn='arn:aws:iam::190616427825:policy/All_Policy'
)
# attach_policy()
# create_policy()
