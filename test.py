import os


import smtplib
import unittest
from mock import patch, call, Mock
from email_class import EmailSender, EmailBuilder



print(os.environ["username"])