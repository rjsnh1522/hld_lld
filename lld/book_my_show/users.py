from abc import ABC

from constants import AccountStatus


class Account:
    def __init__(self, id, password, status=AccountStatus.ACTIVE):
        self.__id = id
        self.__password = password
        self.__status = status

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, new_id):
        self.__id = new_id

    def reset_password(self):
        pass


class Person(ABC):
    def __init__(self, name, address, email, phone, account):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__account = account


class Customer(Person):
    def make_booking(self, booking):
        pass

    def get_bookings(self):
        pass


class Admin(Person):
    def add_movie(self, movie):
        pass

    def add_show(self, show):
        pass

    def block_user(self, customer):
        pass


class FrontDeskOfficer(Person):
    def create_booking(self, booking):
        pass


class Guest:
    def register_account(self):
        pass
