from strategy_pattern.without_strategy.vehicle import Vehicle


class NormalVehicle(Vehicle):

    def __init__(self):
        pass

    def drive(self):
        print("Normal Vehicle drive capability")
