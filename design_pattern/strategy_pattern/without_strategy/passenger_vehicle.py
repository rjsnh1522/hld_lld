from strategy_pattern.without_strategy.vehicle import Vehicle


class PassengerVehicle(Vehicle):

    def __init__(self):
        pass

    def drive(self):
        print("Passenger drive capability")
