import json

from common.variables import ENCODING, MAX_PACKAGE_LENGTH


def send_message(sock, message):
    if not isinstance(message, dict):
        raise TypeError
    message = json.dumps(message)
    encode_message = message.encode(ENCODING)
    sock.send(encode_message)


def get_message(sock):
    encode_message = sock.recv(MAX_PACKAGE_LENGTH)
    if isinstance(encode_message, bytes):
        data = encode_message.decode(ENCODING)
        if isinstance(data, str):
            jim = json.loads(data)
            if isinstance(jim, dict):
                return jim
            raise ValueError
        raise ValueError
    raise ValueError
