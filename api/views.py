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
         "ride_id": 1},
        {"post_date": Utils.make_date_time(), "driver": "Santos", "driver_contact": "0779104144",
         "trip_to": "namasagali", "cost": 12000, "status": "available", "taken_by": None,
         "ride_id": 2},
        {"post_date": Utils.make_date_time(), "driver": "Ronald", "driver_contact": "0779104144",
         "trip_to": "nansana", "cost": 5000, "status": "available", "taken_by": None, "ride_id": 3},
    ]

    def post(self):
        """
        responds to post requests
        :return:
        """
        if not request or not request.json:
            return jsonify({"error_message": "not a json request", "data": str(request.data)}), 400

        keys = ("driver", "trip_to", "cost", "driver_contact")
        if not set(keys).issubset(set(request.json)):
            return jsonify({"error_message": "some of these fields are missing", "data": keys}), 206

        if not request.json["driver"] or not request.json["cost"] or not request.json["trip_to"]\
                or not request.json["driver_contact"]:

            return jsonify({"error_message": "some of these fields have empty/no values",
                            "data": request.json}), 206

        ride = {
            "driver": request.json['driver'],
            "driver_contact": request.json['driver_contact'],
            "trip_to": request.json['trip_to'],
            "cost": request.json['cost'],
            "status": "available",
            "taken_by": None,
            "post_date": Utils.make_date_time(),
            "ride_id": len(self.rides) + 1,
        }
        self.rides.append(ride)

        return jsonify({"success_message": "successfully added to entry to rides", "data": True})
