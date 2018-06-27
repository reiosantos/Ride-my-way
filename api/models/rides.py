from typing import List

from api.utils.utils import JSONSerializable, Utils


class Rides:

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

    rides: List[RideModel] = []

    @staticmethod
    def create_ride(ride_id=1, driver_name=None, contact=0, trip_to=None, cost=0) -> RideModel:
        ride = Rides.RideModel(ride_id, driver_name, contact, trip_to, cost)
        Rides.rides.append(ride)
        return ride

    @classmethod
    def get_all_rides(cls) -> List[RideModel]:
        return cls.rides

    @classmethod
    def get_one_ride(cls, ride_id) -> RideModel or None:
        try:
            ride_id = int(ride_id)
        except ValueError:
            return None

        for ride in Rides.rides:
            if ride.ride_id == ride_id:
                return ride
        return None

    @classmethod
    def request_for_ride(cls, ride: RideModel, contact, names) -> bool:
        ride.requested = True
        ride.requested_by = names + " @ " + contact
        return True

    @classmethod
    def update_ride(cls, ride: RideModel, cost=0, status=None, trip_to=None, taken_by=None) -> bool:
        ride.cost = cost
        ride.status = status
        ride.trip_to = trip_to
        ride.taken_by = taken_by
        return True

    @classmethod
    def delete_ride(cls, m_ride) -> bool:
        for ride in cls.rides:
            if ride.ride_id == m_ride.ride_id:
                cls.rides.remove(ride)
                return True
        return False
