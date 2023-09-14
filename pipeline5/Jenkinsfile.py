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
				"lambda:ListCodeSigningConfigs",
				"s3-object-lambda:*"
			],
			"Resource": []
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
