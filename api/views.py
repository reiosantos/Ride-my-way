"""
    api.views
    ~~~~~~~~~~~

    This module provides class-based views inspired by the ones in flask.

    :copyright: © 2018 by reio santos.
"""

from flask.views import MethodView


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
