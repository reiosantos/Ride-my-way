"""
Error handler class, to handel request exceptions, and other codes.

Noteworthy: None is the `nil' object;.
"""
from flask import jsonify, request


class ErrorHandlers:
    """
    Class ErrorHandler to handle request errors and request codes
    """

    @staticmethod
    def not_found(error):
        """
        Method not found returns nicely formatted 404 message in json format.
        It takes error argument
        :param error:
        :return:
        """
        message = {
            'error_message': str(error) + " " + request.url,
        }
        resp = jsonify(message)
        resp.status_code = 404
        return resp

    @staticmethod
    def bad_request(error):
        """
        Method bad request returns nicely formatted 400 message in json format.
        It takes error as argument
        :param error:
        :return:
        """
        message = {
            'error_message': str(error) + " " + request.url,
        }
        resp = jsonify(message)
        resp.status_code = 400
        return resp

