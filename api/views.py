"""
    api.views
    ~~~~~~~~~~~

    This module provides class-based views inspired by the ones in flask.

    :copyright: © 2018 by reio santos.
"""
from flask import jsonify
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
        {"post_date": Utils.make_date_time(), "driver": "Reio", "trip_to": "nakasongola", "cost": 2000,
         "status": "taken", "taken_by": "ssekitto", "ride_id": 1},
        {"post_date": Utils.make_date_time(), "driver": "Santos", "trip_to": "namasagali", "cost": 12000,
         "status": "available", "taken_by": None, "ride_id": 2},
        {"post_date": Utils.make_date_time(), "driver": "Ronald", "trip_to": "nansana", "cost": 5000,
         "status": "available", "taken_by": None, "ride_id": 3},
    ]

    def get(self, ride_id=None):
        if not ride_id:
            return jsonify({"error_message": False, "data": self.rides})

        if not isinstance(ride_id, int):
            return jsonify({"error_message": False, "data": "id is not an integer "})

        # perform some database operations to find the requested ride and return it
        for obj in self.rides:
            if obj['id'] == ride_id:
                return jsonify({"error_message": False, "data": obj})

        return jsonify({"error_message": "Ride not fount", "data": {}}), 404
