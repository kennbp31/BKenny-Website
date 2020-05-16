import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class SendEmail:
    """Email class, use environmental variables to fill in the email setup, may manually feed setup in as well"""
    def __init__(self, from_name="Test", from_email="Test@test.com", message_text="This is a test!", var_to_email=os.environ["to"]
                 , var_from_email=os.environ["from"], subject="Portfolio Inquiry", smtp_address=os.environ["smtp"]
                 , port=os.environ["port"], smtp_username=os.environ["username"], smtp_password=os.environ["pass"]):
        self.from_name = from_name
        self.from_email = from_email
        self.message_text = message_text
        self.var_to_email = var_to_email
        self.var_from_email = var_from_email
        self.subject = subject
        self.smtp_address = smtp_address
        self.port = port
        self.smtp_username = smtp_username
        self.smtp_password = smtp_password

    def build_email(self):
        # Build the simple text message being sent
        msg = MIMEMultipart()
        msg['From'] = self.var_from_email
        msg['To'] = self.var_to_email
        msg['Subject'] = self.subject
        message = ("Name: " + self.from_name + " , Email: " + self.from_email
                   + " , Message: " + self.message_text)
        msg.attach(MIMEText(message))
        return msg

    def send_email(self):
        msg = self.build_email()

        try:
            # Connect to the mail server
            mailserver = smtplib.SMTP(self.smtp_address, self.port)
            mailserver.login(self.smtp_username, self.smtp_password)
            # Send the email
            mailserver.sendmail(self.var_from_email, self.var_to_email, msg.as_string())
            mailserver.quit()
            return 'success'
        except OSError:
            pass
        return 'fail'






            #giving a gross error when failing on the site.
        #except smtplib.SMTPException:
            #return 'fail'


