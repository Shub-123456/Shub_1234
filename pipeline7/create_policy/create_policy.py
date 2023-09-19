import boto3
import json

user = boto3.client('iam')
def create_policy():
    with open('pipeline7/create_policy/policy.json', 'r') as f:
        policy_document = json.load(f)
    response = user.create_policy(
        PolicyName="abc",
        PolicyDocument=json.dumps(policy_document) 
    )
# create_policy()
