"""
Urls class , to handel request urls,
"""
from api.views import Rides


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
        app.add_url_rule('/api/v1/rides/', view_func=Rides.as_view('get_and_post_rides'), methods=['GET'],
                         strict_slashes=False)