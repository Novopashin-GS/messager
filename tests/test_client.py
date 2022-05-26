import os
import sys
import unittest
import time
sys.path.insert(0, os.path.join(os.getcwd(), '..'))
from common.variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, ERROR
from client import create_message, process_ans


class ClientTestCase(unittest.TestCase):

    def test_create_message(self):
        test_dict = create_message()
        self.assertEqual({ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: 'Guest'
        }}, test_dict)

    def test_process_message_200(self):
        self.assertEqual(process_ans({RESPONSE: 200}), '200 : OK')

    def test_process_message_400(self):
        self.assertEqual(process_ans({RESPONSE: 400, ERROR: 'Bad request'}), '400 : Bad request')

    def test_raise_process_message(self):
        self.assertRaises(ValueError, process_ans, {ERROR: 'Bad Request'})
