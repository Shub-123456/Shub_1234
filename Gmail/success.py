import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# Gmail account details
gmail_user = 'shubham.chide@gmail.com' # Your Gmail address
gmail_app_password = 'Shub_1234' # Use the App Password generated earlier
# Email details
to_email = 'chakarnilkanth@gmail.com' # Recipient's email address
subject = 'Shubham Chide'
message = 'Pipeline run successful.'
# Create a MIMEText object with your message
msg = MIMEMultipart()
msg['From'] = gmail_user
msg['To'] = to_email
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))
# Connect to Gmail's SMTP server
try:
  server = smtplib.SMTP('smtp.elasticemail.com', 2525)
  server.starttls()
  server.login(gmail_user, gmail_app_password)
  # Send the email
  server.sendmail(gmail_user, to_email, msg.as_string())
  print('Email sent successfully!')
except Exception as e:
  print(f'Error: {str(e)}')
finally:
  server.quit()
