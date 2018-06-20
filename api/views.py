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

    def get(self, ride_id=None):
        """
        responds to get requests
        :param ride_id:
        :return:
        """
        if not ride_id:
            return jsonify({"error_message": False, "data": self.rides})

        if not isinstance(ride_id, int):
            return jsonify({"error_message": False, "data": "id is not an integer "})

        # perform some database operations to find the requested ride and return it
        for obj in self.rides:
            if obj['ride_id'] == ride_id:
                return jsonify({"error_message": False, "data": obj})

        return jsonify({"error_message": "Ride not fount", "data": {}}), 404

    def post(self):
        """
        responds to post requests
        :return:
        """
        if not request or not request.json:
            return jsonify({"error_message": "not a json request", "data": str(request.data)}), 400

        if str(request.url_rule) == "/api/v1/rides/":
            return self.handel_post_new_ride()

        if str(request.url_rule) == "/api/v1/rides/requests/join/":
            return self.handle_request_ride()

        return jsonify({"error_message": "Request could not be processed.", "data": False}), 204

    def handel_post_new_ride(self):
        """
        function break down to handle specifically requests to add new rode offers
        it breaks down from the main post function, but its still called from post
        handler
        :return:
        """
        keys = ("driver", "trip_to", "cost", "driver_contact")
        if not set(keys).issubset(set(request.json)):
            return jsonify({"error_message": "some of these fields are missing",
                            "data": keys}), 206

        if not request.json["driver"] or not request.json["cost"] or not \
                request.json["trip_to"] or not request.json["driver_contact"]:
            return jsonify({"error_message": "some of these fields have empty/no values",
                            "data": request.json}), 206

        if not Utils.validate_contact(str(request.json['driver_contact'])):
            return jsonify({"error_message": "driver contact {0} is wrong. should be in"
                                             " the form, (0789******) and between 10 and 13 "
                                             "digits".format(request.json['driver_contact']),
                            "data": request.json}), 206

        if not Utils.validate_number(str(request.json['cost'])):
            return jsonify({"error_message": "Supplied amount {0} is wrong."
                                             " should be a number and greater than 0"
                                             .format(request.json['driver_contact']),
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

        return jsonify({"success_message": "successfully added to entry to rides",
                        "data": True})

    def handle_request_ride(self):
        """
        function break down to handle specifically requests to for response to
        ride offers from passengers offer offers
        it breaks down from the main post function, but its still called from post
        handler
        :return:
        """

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
                                           " shall be responding to you shortly", "data": True})

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

    def delete(self, ride_id):
        """
        responds to update requests
        :return:
        """
        if not request or not ride_id:
            return jsonify({"error_message": "URL is invalid. Ride id is missing a value",
                            "data": str(request.url_rule)}), 400
        if str(request.url_rule) == "/api/v1/rides/delete/<int:ride_id>/":

            ride_index = 0
            exists = False
            for ride in self.rides:
                if ride['ride_id'] == ride_id:
                    exists = True
                    break
                ride_index += 1

            if not exists:
                return jsonify({"error_message": "The requested ride {0} is not found"
                                                 .format(ride_id),
                                "data": False}), 404

            self.rides.remove(self.rides[ride_index])

            return jsonify({"success_message": "Ride has been deleted.", "data": True})

        return jsonify({"error_message": "Request could not be processed.", "data": False}), 204
