from strategy_pattern.with_strategy.strategy.sport_drive_strategy import SportDriveStrategy
from strategy_pattern.with_strategy.vehicle import Vehicle


class SportVehicle(Vehicle):

    def __init__(self):
        super(SportVehicle, self).__init__(drive_strategy=SportDriveStrategy)

    def drive(self):
        print("High end drive capability")
