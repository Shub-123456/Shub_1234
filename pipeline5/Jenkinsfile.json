import boto3
import json
iam = boto3.client('iam')
def create_policy():
    policy_name = "EC2Permissions-ProfileSummary"
    policy_document = {

        "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "Statement1",
                    "Effect": "Allow",
                    "Action": [
                        "ec2:*",
                        "iam:GetAccountSummary",
                        "iam:GetLoginProfile",
                        "iam:GetUser"
                    ],
                "Resource": "arn:aws:ec2:::*",
                "Resource": "arn:aws:iam:::*"
            }
        ]

    }

    iam_client = boto3.client("iam")

    response = iam_client.create_policy(
        PolicyName=policy_name,
        PolicyDocument=json.dumps(policy_document)
    )

    print("Policy created:")
    print(response)

def create_user():
    response = iam.create_user(
        UserName='bob'
    )
    print(response)

def attach_policy():
    response = iam.attach_user_policy(
    UserName='bob',
    PolicyArn='arn:aws:iam::430912479781:policy/EC2Permissions-ProfileSummary'
)
create_policy()
create_user()
attach_policy()
