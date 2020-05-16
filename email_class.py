import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class BuildEmail:
    """Email class, use environmental variables to create the message being sent, may manually feed setup in as well"""
    def __init__(self, from_name="Test", from_email="Test@test.com", message_text="This is a test!", msg=MIMEMultipart()):
        self.from_name = from_name
        self.from_email = from_email
        self.message_text = message_text
        self.msg = msg
        msg['From'] = os.environ["from"]
        msg['To'] = os.environ["to"]
        msg['Subject'] = "Portfolio Inquiry"

    def build_email(self):
        # Build the simple text message being sent using user input
        message = ("Name: " + self.from_name + " , Email: " + self.from_email
                   + " , Message: " + self.message_text)
        self.msg.attach(MIMEText(message))
        return self.msg


class SendEmail:
    """Class used to send an email, will require a preformatted message, as built in the prior class"""
    def __init__(self, smtp_username=os.environ["username"], smtp_password=os.environ["pass"], var_to_email=os.environ["to"], var_from_email=os.environ["from"]
                 , message='No message provided', mail_server=smtplib.SMTP(os.environ["smtp"], os.environ["port"])):
        self.smtp_username = smtp_username
        self.smtp_password = smtp_password
        self.var_to_email = var_to_email
        self.var_from_email = var_from_email
        self.message = message
        self.mail_server = mail_server

    def send_email(self):
        try:
            # Connect to the mail server
            self.mail_server.login(self.smtp_username, self.smtp_password)
            # Send the email
            self.mail_server.sendmail(self.var_from_email, self.var_to_email, self.message)
            self.mail_server.quit()
            return 'success'
        except smtplib.SMTPException:
            return 'fail'


