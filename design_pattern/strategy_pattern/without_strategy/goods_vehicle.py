from strategy_pattern.without_strategy.vehicle import Vehicle


class GoodsVehicle(Vehicle):

    def __init__(self):
        pass

    def drive(self):
        print("Goods drive capability")
