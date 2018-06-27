from functools import wraps

from flask import request

from api.handlers.return_errors import ReturnHandlers


class Decorate:

    @staticmethod
    def receive_json(fun):
        @wraps(fun)
        def decorated(*args, **kwargs):

            if not request or not request.json:
                return ReturnHandlers.not_json_request()

            return fun(*args, **kwargs)

        return decorated
