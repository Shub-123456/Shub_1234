import boto3

from botocore.exceptions import NoCredentialsError

from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart

# AWS SES credentials

aws_access_key = 'AKIAZRICDOIC5FCCXJVL'

aws_secret_key = 'HpM4WuNk7abr3OMkWYvXY45rjewyuoLg/EEfN3Be'

aws_region = 'ap-south-1' # Replace with your AWS region

# Sender and recipient

sender_email = 'shubham.chide@gmail.com'

recipient_email = 'chakarnilkanth@gmail.com'

# Create the email message

subject = 'Hello sir'

message = 'we are students of technobrillient from devops batch!!!'

msg = MIMEMultipart()

msg['From'] = sender_email

msg['To'] = recipient_email

msg['Subject'] = subject

msg.attach(MIMEText(message, 'plain'))

# Connect to the SES service

try:

  ses_client = boto3.client('ses', region_name=aws_region, aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)

  response = ses_client.send_raw_email(Source=sender_email, Destinations=[recipient_email], RawMessage={'Data': msg.as_string()})

  print("Email sent failed! Message ID:", response['MessageId'])

except NoCredentialsError:

  print("AWS credentials not available.")

except Exception as e:

  print("An error occurred:")
