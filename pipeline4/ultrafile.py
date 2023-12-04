import boto3
ec2 = boto3.resource('ec2',region_name = 'ap-south-1')


instances = ec2.create_instances(
        ImageId="ami-02a2af70a66af6dfb",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName="K8S"
    )
