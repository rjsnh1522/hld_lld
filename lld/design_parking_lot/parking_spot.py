from abc import ABC

from enums.parking_spot_type import ParkingSpotType


class ParkingSpot(ABC):
    def __init__(self, number, parking_spot_type):
        self.__number = number
        self.__parking_spot_type = parking_spot_type
        self.__free = True
        self.__vehicle = None

    def is_free(self):
        return self.__free

    def assign_vehicle(self, vehicle):
        self.__vehicle = vehicle
        self.__free = False

    def remove_vehicle(self):
        self.__vehicle = None
        self.__free = True


class HandicappedSpot(ParkingSpot):
    def __init__(self, number):
        super(HandicappedSpot, self).__init__(number, ParkingSpotType.HANDICAPPED)


class CompactSpot(ParkingSpot):
    def __init__(self, number):
        super(CompactSpot, self).__init__(number, ParkingSpotType.COMPACT)


class LargeSpot(ParkingSpot):
    def __init__(self, number):
        super(LargeSpot, self).__init__(number, ParkingSpotType.LARGE)


class MotorbikeSpot(ParkingSpot):
    def __init__(self, number):
        super(MotorbikeSpot, self).__init__(number, ParkingSpotType.MOTORCYCLE)


class ElectricSpot(ParkingSpot):
    def __init__(self, number):
        super(ElectricSpot, self).__init__(number, ParkingSpotType.ELECTRIC)
