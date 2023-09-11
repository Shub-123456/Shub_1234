import boto3
ec2 = boto3.resource('ec2',region_name = 'ap-south-1')


instances = ec2.create_instances(
        ImageId="ami-06f621d90fa29f6d0",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName="sammy"
    )
