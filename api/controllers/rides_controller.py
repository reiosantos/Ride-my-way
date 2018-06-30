"""
    api.views
    ~~~~~~~~~~~

    This module provides class-based views inspired by the ones in flask.

    :copyright: © 2018 by reio santos.
"""
from flask import request, jsonify
from flask.views import MethodView

from api.handlers.return_errors import ReturnHandlers
from api.models.rides import Rides
from api.utils.decorators import Decorate
from api.utils.validators import Validators


class RidesController(MethodView):
    """A class-based view that dispatches request methods to the corresponding
       class methods. For example, if you implement a ``get`` method, it will be
       used to handle ``GET`` requests. :
    """

    def get(self, ride_id=None):
        """
        responds to get requests
        :param ride_id:
        :return:
        """
        if ride_id:
            # perform some database operations to find the requested ride and return it

            for obj in Rides.find_all_rides():
                if obj.ride_id == ride_id:
                    return jsonify({"error_message": False, "data": obj.__dict__})

            return ReturnHandlers.ride_not_found(ride_id)

        return jsonify({"error_message": False, "data": [o.__dict__ for o in Rides.find_all_rides()]})

    @Decorate.receive_json
    def post(self, ride_id=None):
        """
        responds to post requests. Creating new rides
        :return:
        """
        if str(request.url_rule) == "/api/v1/rides/":
            return RidesController.handel_post_new_ride()

        if str(request.url_rule) == "/api/v1/rides/<int:ride_id>/requests/":
            return RidesController.handle_request_ride(ride_id)

        return ReturnHandlers.could_not_process_request()

    @staticmethod
    def handel_post_new_ride():
        """
        function break down to handle specifically requests to add new rode offers
        it breaks down from the main post function, but its still called from post
        handler
        :return:
        """
        keys = ("driver", "trip_to", "cost", "driver_contact")
        if not set(keys).issubset(set(request.json)):
            return ReturnHandlers.missing_fields(keys)

        if not request.json["driver"] or not request.json["cost"] or not \
                request.json["trip_to"] or not request.json["driver_contact"]:
            return ReturnHandlers.empty_fields()

        if not Validators.validate_contact(str(request.json['driver_contact'])):
            return ReturnHandlers.invalid_contact()

        if not Validators.validate_number(str(request.json['cost'])):
            return ReturnHandlers.invalid_amount()

        Rides.create_ride(len(Rides.rides), driver_name=request.json['driver'],
                          contact=request.json['driver_contact'], trip_to=request.json['trip_to'],
                          cost=request.json['cost'])

        return jsonify({"success_message": "successfully added a new ride.", "data": True}), 201

    @staticmethod
    def handle_request_ride(ride_id):
        """
        function break down to handle specifically requests to for response to
        ride offers from passengers offer offers
        it breaks down from the main post function, but its still called from post
        handler
        :return:
        """

        keys = ("passenger", "passenger_contact")
        if not set(keys).issubset(set(request.json)):
            return ReturnHandlers.missing_fields(keys)

        if not ride_id or not request.json["passenger"] or \
                not request.json["passenger_contact"]:
            return ReturnHandlers.empty_fields()

        if not Validators.validate_contact(str(request.json['passenger_contact'])):
            return ReturnHandlers.invalid_contact()

        ride = Rides.find_one_ride(ride_id)
        if not ride:
            return ReturnHandlers.ride_not_found(keys)

        if ride.requested:
            return ReturnHandlers.ride_already_requested()

        names = request.json["passenger"]
        contact = request.json["passenger_contact"]
        Rides.add_request_for_ride(ride, contact, names)

        return jsonify({"success_message": "Your request has been successful. The driver"
                                           " shall be responding to you shortly", "data": True}), 201

    @Decorate.receive_json
    def put(self):
        """
        responds to update requests
        It allows the driver to respond to passenger requests
        :return:
        """
        keys = ("ride_id", "trip_to", "status", "cost", "taken_by")
        if not set(keys).issubset(set(request.json)):
            return ReturnHandlers.missing_fields(keys)

        if not request.json["ride_id"]:
            return ReturnHandlers.empty_fields()

        ride_id = request.json["ride_id"]
        ride = Rides.find_one_ride(ride_id)
        if not ride:
            return ReturnHandlers.ride_not_found(ride_id)

        update = Rides.update_ride(ride, request.json["cost"], request.json["status"],
                                   request.json["trip_to"], request.json["taken_by"])
        if update:
            return jsonify({"success_message": "Update has been successful.", "data": True})

        return ReturnHandlers.could_not_process_request()

    def delete(self, ride_id):
        """
        responds to update requests
        :return:
        """
        ride = Rides.find_one_ride(ride_id)
        if not ride:
            return ReturnHandlers.ride_not_found(ride_id)

        if Rides.delete_ride(ride):
            return jsonify({"success_message": "Ride {0} has been deleted.".format(ride_id), "data": True})

        return jsonify({"error_message": "Ride {0} has not been deleted.".format(ride_id), "data": False})
