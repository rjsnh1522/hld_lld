from strategy_pattern.with_strategy.normal_vehicle import NormalVehicle
from strategy_pattern.with_strategy.sport_vehicle import SportVehicle
from strategy_pattern.with_strategy.vehicle import Vehicle



if __name__ == "__main__":
    vehicle = Vehicle(SportVehicle())
    vehicle.drive()

    vehicle.set_drive_strategy(NormalVehicle())
    vehicle.drive()
