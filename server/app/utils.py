import random
import string

from flask import make_response, jsonify, request


def rand_str(length):
    return ''.join(
        random.SystemRandom().choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in
        range(length))


class APICode:
    OK = 0
    ERR = 1


def api_body(code, data=None, message=None, http_code=200):
    if not message:
        if code == 0:
            message = "ok"
        else:
            message = "err"

    response = {
        'code': code,
        'msg': str(message),
        'data': data
    }

    response_body = make_response(jsonify(response), http_code)
    return response_body


def get_real_ip():
    return request.remote_addr
