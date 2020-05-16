import os
import smtplib
import unittest
from mock import patch, call, Mock
from email_class import SendEmail as SendEmail


class TestEmail(unittest.TestCase):

    # Ensure that environmental variables are defined and loading correctly
    def test_os_variables(self):
        messages = SendEmail()
        messages.from_name = 'Brendan'
        messages.from_email = 'test@test.com'
        messages.message_text = 'This is a test'
        self.assertIn('Portfolio Inquiry', str(messages.build_email()))
        self.assertIn('kennbp31@gmail.com', str(messages.build_email()))

    # Ensure that the message contains concatenated text correctly
    def test_msg(self):
        messages = SendEmail()
        messages.from_name = 'Brendan'
        messages.from_email = 'test@test.com'
        messages.message_text = 'This is a test'
        self.assertIn('Name: Brendan , Email: test@test.com , Message: This is a test', str(messages.build_email()))

    # check that response is true when email is sent correctly
    def test_send_success(self):
        with patch("smtplib.SMTP") as mock_smtp:
            message = SendEmail()
            result = message.send_email()
        instance = mock_smtp.return_value

        # Ensure that sendmail is actually called
        self.assertTrue(instance.sendmail.called)

        # Checks the mock has been called one time
        self.assertEqual(instance.sendmail.call_count, 1)

        # Ensure that the result passed back to the app is true
        self.assertEqual('success', result)

    # Check that response is fail when email is not sent correctly
    def test_send_fail(self):
        with patch("smtplib.SMTP") as mock_smtp:
            mailer = SendEmail()
        instance = mock_smtp.return_value
        instance.mock_smtp.side_effect = OSError

        # Ensure that sendmail was not called
        self.assertFalse(instance.sendmail.called)

        # Checks that sendmail call count = 0
        self.assertEqual(instance.sendmail.call_count, 0)


if __name__ == '__main__':
    unittest.main()

