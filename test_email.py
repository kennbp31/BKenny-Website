import os
import smtplib
import unittest
from mock import patch, call, Mock
from email_class import SendEmail as SendEmail, BuildEmail as BuildEmail


class TestEmail(unittest.TestCase):
    """Series of unit tests ensuring that emails are built and sent correctly."""
    # Ensure that environmental variables are defined and loading correctly
    def test_osvariables(self):
        build_e = BuildEmail()
        self.assertIn('Portfolio Inquiry', str(build_e.build_email()))
        self.assertIn('kennbp31@gmail.com', str(build_e.build_email()))

    def test_message_concatentaion(self):
        name = "Brendan Test"
        email = "Test@Email.com"
        message = "Test Messages are great!"
        build_e = BuildEmail(name,email,message)
        self.assertIn( 'Name: Brendan Test , Email: Test@Email.com , Message: Test Messages are great!', str(build_e.build_email()))

    # check that function returns success when there is not an SMTP Exception
    def test_send_success(self):
        with patch("smtplib.SMTP.sendmail") as mock_smtp, patch("smtplib.SMTP.login") as mock_login:
            mailer = SendEmail()
            result = mailer.send_email()
            # Ensure that our smtplib was properly mocked
            self.assertTrue(mock_smtp.called)
            self.assertTrue(mock_login.called)
            self.assertEqual(mock_smtp.call_count, 1)
            # Ensure that success is returned
            self.assertEqual("success", result)
            # Ensure the OS variables are loading and used as expected
            self.assertEqual(os.environ["from"], mailer.var_from_email)
            mock_login.assert_called_with(os.environ["username"], os.environ["pass"])

    # check that function returns fail when there is an SMTP Exception
    def test_send_fail(self):
        with patch("smtplib.SMTP.login") as mock_login:
            mailer = SendEmail()
            mock_login.SMTPException = True
            result = mailer.send_email()
            # Ensure that our smtplib was properly mocked
            self.assertTrue(mock_login.called)
            # Ensure that exceptions trigger a failed response
            self.assertEqual("fail", result)


if __name__ == '__main__':
    unittest.main()

