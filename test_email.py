import os
import unittest
from mock import patch

# Load environment variables used in email classes and methods, they need to be loaded
# prior to the email_class being imported.
os.environ["smtp"] = "smtp.sendgrid.net"
os.environ["port"] = "587"
os.environ["username"] = "apikey"
os.environ["pass"] = "ABCDEF65432!!"
os.environ["to"] = "kennbp31@gmail.com"
os.environ["from"] = "kennbp31@gmail.com"
from email_class import EmailSender, EmailBuilder, Result


class TestEmail(unittest.TestCase):
    """Series of unit tests ensuring that emails are built and sent correctly."""
    @classmethod
    def setUpClass(cls):
        cls.build = EmailBuilder()
        cls.build.build_email("Test Name", "test@example.com", "Test Message!")

    # Ensure that environmental variables are defined and loading correctly
    def test_osvariables(self):
        self.assertEqual('Portfolio Inquiry', self.build.email_msg["Subject"])

    def test_message_concatenation(self):
        self.assertIn('Name: Test Name , Email: test@example.com , Message: Test Message!'
                      , str(self.build.email_msg))

    # check that function returns success when there is not an SMTP Exception
    def test_send_success(self):
        with patch("smtplib.SMTP.sendmail") as mock_smtp, patch("smtplib.SMTP.login") as mock_login:
            mailer = EmailSender()
            result = mailer.send_email(self.build.email_msg)
            # Ensure that our smtplib was properly mocked
            self.assertTrue(mock_smtp.called)
            self.assertTrue(mock_login.called)
            # Ensure that success is returned
            self.assertEqual(Result.success, result)

    def test_check_user_pass(self):
        with patch("smtplib.SMTP.login") as mock_login:
            mailer = EmailSender()
            result = mailer.send_email(self.build.email_msg)
            # Ensure that our smtplib was properly mocked
            self.assertTrue(mock_login.called)
            # Ensure that the login is called with proper variables
            mock_login.assert_called_with(os.environ["username"], os.environ["pass"])

    # check that function returns fail when there is an SMTP Exception
    def test_send_fail(self):
        with patch("smtplib.SMTP.login") as mock_login:
            mailer = EmailSender()
            mock_login.SMTPException = True
            result = mailer.send_email(self.build.email_msg)

            # Ensure that our smtplib was properly mocked
            self.assertTrue(mock_login.called)
            # Ensure that exceptions trigger a failed response
            self.assertEqual(Result.fail, result)


if __name__ == '__main__':
    unittest.main()
