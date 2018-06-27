from flask import jsonify, request

from api.handlers.errors import ErrorHandlers


class ReturnHandlers:

    @staticmethod
    def invalid_contact():
        return jsonify({"error_message": "driver contact {0} is wrong. should be in"
                                         " the form, (0789******) and between 10 and 13 "
                                         "digits".format(request.json['driver_contact']),
                        "data": request.json}), 400

    @staticmethod
    def invalid_amount():
        return jsonify({"error_message": "Supplied amount {0} is wrong."
                                         " should be a number and greater than 0"
                       .format(request.json['driver_contact']),
                        "data": request.json}), 400

    @staticmethod
    def missing_fields(keys):
        return jsonify({"error_message": "some of these fields are missing",
                        "data": keys}), 400

    @staticmethod
    def empty_fields():
        return jsonify({"error_message": "some of these fields have empty/no values",
                        "data": request.json}), 400

    @staticmethod
    def ride_not_found(key):
        return jsonify({"error_message": "The requested ride {0} is not found".format(key),
                        "data": False}), 404

    @staticmethod
    def ride_already_requested():
        return jsonify({"error_message": "Ride {0} has been requested by another person"
                                         "".format(request.json['ride_id']),
                        "data": request.json}), 409

    @staticmethod
    def not_json_request():
        return ErrorHandlers.bad_request("Not a json request")

    @staticmethod
    def could_not_process_request():
        return jsonify({"error_message": "Request could not be processed.", "data": False}), 204
