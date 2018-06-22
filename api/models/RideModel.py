
from api.utils import Utils, JSONSerializable


class RideModel(JSONSerializable):
    def __init__(self, ride_id=1, driver_name=None, contact=0, trip_to=None, cost=0):
        self.ride_id = ride_id
        self.driver_name = driver_name
        self.driver_contact = contact
        self.post_date = Utils.make_date_time()
        self.trip_to = trip_to
        self.cost = cost
        self.status = "available"
        self.taken_by = None
        self.requested = False
        self.requested_by = None
