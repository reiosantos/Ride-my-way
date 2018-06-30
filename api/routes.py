"""
Urls class , to handel request urls,
"""
from api.controllers.rides_controller import RidesController


class Urls:
    """
    Class to generate urls via static method generate
    """
    @staticmethod
    def generate(app):
        """
        Generate urls on the app context
        It takes no argument
        :param: app: takes in the app variable
        :return: urls
        """
        app.add_url_rule('/api/v1/rides/', view_func=RidesController.as_view('get_rides'), methods=['GET'],
                         strict_slashes=False)
        app.add_url_rule('/api/v1/rides/<int:ride_id>/', view_func=RidesController.as_view('get_one_ride'),
                         methods=['GET'], strict_slashes=False)
        app.add_url_rule('/api/v1/rides/', view_func=RidesController.as_view('post_rides'), methods=["POST"],
                         strict_slashes=False)
        app.add_url_rule('/api/v1/rides/<int:ride_id>/requests/', view_func=RidesController.
                         as_view('request_join_ride'), methods=['POST'], strict_slashes=False)
        app.add_url_rule('/api/v1/rides/', view_func=RidesController.as_view('update_one_ride'),
                         methods=['PUT'], strict_slashes=False)
        app.add_url_rule('/api/v1/rides/<int:ride_id>/', view_func=RidesController.as_view('delete_ride'),
                         methods=['DELETE'], strict_slashes=False)
