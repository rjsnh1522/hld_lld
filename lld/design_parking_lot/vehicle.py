from abc import ABC


class Vehicle(ABC):
    def __init__(self, license_number, vehicle_type, ticket=None):
        self.__license_number = license_number
        self.__vehicle_type = vehicle_type
        self.__ticket = ticket

    def assign_ticket(self, ticket):
        self__ticket = ticket


class Car(Vehicle):
    def __init__(self, license_number, ticket=None):
        super(Car, self).__init__(license_number, ticket)


class Van(Vehicle):
    def __init__(self, license_number, ticket=None):
        super(Van, self).__init__(license_number, ticket)


class Truck(Vehicle):
    def __init__(self, license_number, ticket=None):
        super(Truck, self,).__init__(license_number, ticket)


class Motorcycle(Vehicle):
    def __init__(self, license_number, ticket=None):
        super(Motorcycle, self,).__init__(license_number, ticket)


class ElectricVehicle(Vehicle):
    def __init__(self, license_number, ticket=None):
        super(ElectricVehicle, self,).__init__(license_number, ticket)
