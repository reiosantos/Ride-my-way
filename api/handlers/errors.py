"""
Error handler class, to handel request exceptions, and other codes.

Noteworthy: None is the `nil' object;.
"""
from flask import jsonify, request


class ErrorHandlers:
    """
    Class ErrorHandler to handle request errors and request codes
    """
    message = {
        'error_message': "{0} {1}",
    }

    @staticmethod
    def not_found(error):
        """
        Method not found returns nicely formatted 404 message in json format.
        It takes error argument
        :param error:
        :return:
        """
        return jsonify({"error_message": ErrorHandlers.message['error_message'].format(
            error, request.url)}), 404

    @staticmethod
    def bad_request(error):
        """
        Method bad request returns nicely formatted 400 message in json format.
        It takes error as argument
        :param error:
        :return:
        """
        return jsonify({"error_message": ErrorHandlers.message['error_message'].format(
            error, request.url)}), 400
