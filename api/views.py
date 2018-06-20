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

    def put(self):
        """
        responds to update requests
        :return:
        """
        if not request or not request.json:
            return jsonify({"error_message": "not a json request", "data": str(request.data)}), 400

        if str(request.url_rule) == "/api/v1/rides/update/":

            keys = ("ride_id", "trip_to", "status", "cost", "taken_by")
            if not set(keys).issubset(set(request.json)):
                return jsonify({"error_message": "some of these fields are missing",
                                "data": keys}), 206

            if not request.json["ride_id"]:
                return jsonify({"error_message": "Ride id is missing a value",
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

            def_ride = self.rides[ride_index]

            ride = {
                "cost": request.json["cost"] or def_ride['cost'],
                "status": request.json["status"] or def_ride['status'],
                "trip_to": request.json["trip_to"] or def_ride['trip_to'],
                "taken_by": request.json["taken_by"] or def_ride['taken_by'],
            }
            self.rides[ride_index].update(ride)

            return jsonify({"success_message": "Update has been successful.", "data": True})

        return jsonify({"error_message": "Request could not be processed.", "data": False}), 204
