import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from enum import Enum


class EmailBuilder:
    """Email class, use environmental variables to create the message being sent, may manually feed setup in as well"""

    def __init__(self, email_msg=MIMEMultipart()):
        self.email_msg = email_msg
        self.email_msg['From'] = os.environ["from"]
        self.email_msg['To'] = os.environ["to"]
        self.email_msg['Subject'] = "Portfolio Inquiry"

    def build_email(self, from_name, from_email, message_text):
        # Build the simple text message being sent using user input
        message = ("Name: " + from_name + " , Email: " + from_email
                   + " , Message: " + message_text)
        self.email_msg.attach(MIMEText(message))


class EmailSender:
    """Class used to send an email, will require a preformatted message, as built in the prior class"""

    def __init__(self, smtp_username=os.environ["username"], smtp_password=os.environ["pass"]
                 , mail_server=smtplib.SMTP(os.environ["smtp"], os.environ["port"])):
        self.smtp_username = smtp_username
        self.smtp_password = smtp_password
        self.mail_server = mail_server

    def send_email(self, built_email):
        try:
            # Connect to the mail server
            self.mail_server.login(self.smtp_username, self.smtp_password)
            # Send the email
            self.mail_server.sendmail(built_email["From"], built_email["To"], str(built_email))
            self.mail_server.quit()
            return Result.success
        except smtplib.SMTPException:
            return Result.fail


class Result(Enum):
    success = 2
    fail = 1
