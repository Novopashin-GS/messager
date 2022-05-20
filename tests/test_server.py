import os
import sys
import unittest
import time
sys.path.insert(0, os.path.join(os.getcwd(), '..'))
from common.variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, ERROR
from server import process_client_message


class ServerTestCase(unittest.TestCase):
    ok_dict = {
        RESPONSE: 200
    }
    error_dict = {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }

    def test_process_message_without_action(self):
        self.assertEqual(process_client_message({
            TIME: time.time(),
            USER: {
                ACCOUNT_NAME: 'Guest'
            }
        }), self.error_dict)

    def test_process_message_with_wrong_action(self):
        self.assertEqual(process_client_message({
            ACTION: 'Wrong',
            TIME: time.time(),
            USER: {
                ACCOUNT_NAME: 'Guest'
            }
        }), self.error_dict)

    def test_process_message_without_time(self):
        self.assertEqual(process_client_message({
            ACTION: PRESENCE,
            USER: {
                ACCOUNT_NAME: 'Guest'
            }
        }), self.error_dict)

    def test_process_message_without_user(self):
        self.assertEqual(process_client_message({
            ACTION: 'Wrong',
            TIME: time.time(),
        }), self.error_dict)

    def test_process_message_with_wrong_user(self):
        self.assertEqual(process_client_message({
            ACTION: PRESENCE,
            TIME: time.time(),
            USER: {
                ACCOUNT_NAME: 'Guest2'
            }
        }), self.error_dict)

    def test_process_message_ok(self):
        self.assertEqual(process_client_message({
            ACTION: PRESENCE,
            TIME: time.time(),
            USER: {
                ACCOUNT_NAME: 'Guest'
            }
        }), self.ok_dict)
