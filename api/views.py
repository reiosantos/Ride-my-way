"""
    api.views
    ~~~~~~~~~~~

    This module provides class-based views inspired by the ones in flask.

    :copyright: © 2018 by reio santos.
"""
from flask import request, jsonify
from flask.views import MethodView

from api.utils import Utils


class Rides(MethodView):
    """A class-based view that dispatches request methods to the corresponding
       class methods. For example, if you implement a ``get`` method, it will be
       used to handle ``GET`` requests. ::

           class Rides(MethodView):
               def get(self, ride=None):
                   return make_response(jsonify({"data": False, "error_message": False}))

               def post(self):
                   return make_response(jsonify({"data": False, "error_message": False}))

           app.add_url_rule('/api/v1/rides/', view_func=Rides.as_view('get_rides'))
    """
    rides = [
        {"post_date": Utils.make_date_time(), "driver": "Reio", "driver_contact": "0779104144",
         "trip_to": "nakasongola", "cost": 2000, "status": "taken", "taken_by": "ssekitto",
         "ride_id": 1, "requested": True, "Requested_by": "ssekitto"},
        {"post_date": Utils.make_date_time(), "driver": "Santos", "driver_contact": "0779104144",
         "trip_to": "namasagali", "cost": 12000, "status": "available", "taken_by": None,
         "ride_id": 2, "requested": False, "requested_by": None},
        {"post_date": Utils.make_date_time(), "driver": "Ronald", "driver_contact": "0779104144",
         "trip_to": "nansana", "cost": 5000, "status": "available", "taken_by": None,
         "ride_id": 3, "requested": False, "requested_by": None},
    ]

    def post(self):
        """
        responds to post requests
        :return:
        """
        if not request or not request.json:
            return jsonify({"error_message": "not a json request", "data": str(request.data)}), 400

        if str(request.url_rule) == "/api/v1/rides/requests/join/":

            keys = ("ride_id", "passenger", "passenger_contact")
            if not set(keys).issubset(set(request.json)):
                return jsonify({"error_message": "some of these fields are missing",
                                "data": keys}), 206

            if not request.json["ride_id"] or not request.json["passenger"] or \
                    not request.json["passenger_contact"]:
                return jsonify({"error_message": "some of these fields have empty/no values",
                                "data": request.json}), 206

            key = request.json["ride_id"]
            ride_index = 0
            exists = False
            for ride in self.rides:
                if ride['ride_id'] == key:
                    exists = True
                    break
                ride_index += 1

            if not exists:
                return jsonify({"error_message": "The requested ride {0} is not found".format(key),
                                "data": False}), 404

            if not Utils.validate_contact(str(request.json['passenger_contact'])):
                return jsonify({"error_message": "passenger contact {0} is wrong. should be in"
                                                 " the form, (0789******) and between 10 and 13 "
                                                 "digits".format(request.json['passenger_contact']),
                                "data": request.json}), 206

            ride = {
                "requested": request.json["passenger"],
                "requested_by": request.json["passenger_contact"],
            }
            self.rides[ride_index].update(ride)

            return jsonify({"success_message": "Your request has been successful. The driver"
                                               " shall be responding to you shortly",
                            "data": True})

        return jsonify({"error_message": "Request could not be processed.", "data": False}), 204
