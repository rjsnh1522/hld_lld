from strategy_pattern.without_strategy.vehicle import Vehicle


class SportVehicle(Vehicle):

    def __init__(self):
        pass

    def drive(self):
        print("High end drive capability")
