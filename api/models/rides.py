from typing import List

from api.models.users import Users
from api.utils.utils import JSONSerializable, Utils


class Rides:

    class RequestStatus:
        pending = "pending"
        accepted = "accepted"
        rejected = "rejected"

    class RideModel(JSONSerializable):
        def __init__(self, driver_id=None, destination=None, cost=0, ride_from=None, departure_time=None):
            self.ride_id = Utils.generate_ride_id()
            self.post_date = Utils.make_date_time()

            self.driver_id = driver_id
            self.destination = destination
            self.departure_time = departure_time
            self.source_location = ride_from
            self.cost = cost
            self.status = "available"

    class RequestModal(JSONSerializable):
        def __init__(self, passenger_id=None, ride_id=None):
            self.request_id = Utils.generate_request_id()
            self.request_date = Utils.make_date_time()

            self.ride_id = ride_id
            self.passenger_id = passenger_id
            self.taken = False
            self.status = Rides.RequestStatus.pending

    rides: List[RideModel] = []
    requests: List[RequestModal] = []

    @staticmethod
    def create_ride(driver_id, trip_to, cost, depart_time) -> RideModel:
        ride = Rides.RideModel(driver_id, trip_to, cost, depart_time)
        Rides.rides.append(ride)
        return ride

    @classmethod
    def find_all_rides(cls) -> List[RideModel]:
        return cls.rides

    @classmethod
    def find_one_ride(cls, ride_id) -> RideModel or None:
        try:
            ride_id = int(ride_id)
        except ValueError:
            return None

        for ride in Rides.rides:
            if ride.ride_id == ride_id:
                return ride
        return None

    @classmethod
    def update_ride(cls, ride_id, cost=0, status=None, trip_to=None, taken_by=None) -> bool:
        ride = cls.find_one_ride(ride_id)
        if not ride:
            return False
        index = cls.rides.index(ride)

        ride.cost = cost
        ride.status = status
        ride.destination = trip_to
        ride.taken_by = taken_by

        cls.rides.insert(index, ride)
        return True

    @classmethod
    def delete_ride(cls, ride_id) -> bool:
        ride = cls.find_one_ride(ride_id)
        if not ride:
            return False

        cls.rides.remove(ride)
        return True

    @classmethod
    def find_all_requests(cls) -> dict:
        all_requests = {}

        for request in cls.requests:
            ride = cls.find_one_ride(request.ride_id)
            if ride:
                passenger = Users.find_user(request.passenger_id)
                if passenger:
                    if ride.ride_id not in all_requests:
                        all_requests[ride.ride_id] = {}
                    all_requests[ride].update(request.__dict__)
                    all_requests[ride].update(ride.__dict__)
                    all_requests[ride].update(passenger.__dict__)

        return all_requests

    @classmethod
    def find_one_request(cls, req_id) -> dict:
        try:
            req_id = int(req_id)
        except ValueError:
            return {}

        for request in Rides.requests:
            if request.request_id == req_id:
                ride = cls.find_one_ride(request.ride_id)
                if ride:
                    passenger = Users.find_user(request.passenger_id)
                    if passenger:
                        request_object = {}
                        request_object.update(request.__dict__)
                        request_object.update(ride.__dict__)
                        request_object.update(passenger.__dict__)
                        return request_object
        return {}

    @classmethod
    def add_request_for_ride(cls, ride_id, passenger_id) -> bool:
        if not ride_id:
            return False

        request_object = cls.RequestModal(ride_id=ride_id, passenger_id=passenger_id)
        cls.requests.append(request_object)
        return True

    @classmethod
    def approve_request_for_ride(cls, ride_id, request_id) -> bool:
        if not ride_id or not request_id:
            return False
        request = cls.find_one_request(request_id)
        if not request:
            return False

        request.status = cls.RequestStatus.accepted
        return True
