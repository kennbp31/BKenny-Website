import unittest
from unittest import mock
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

    # TODO check that response is true when email is sent correctly

    # TODO check that response is fail when email is not sent correctly


if __name__ == '__main__':
    unittest.main()

