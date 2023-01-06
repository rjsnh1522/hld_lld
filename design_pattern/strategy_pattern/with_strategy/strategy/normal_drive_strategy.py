from strategy_pattern.with_strategy.strategy.drive_strategy import DriveStrategy


class NormalDriveStrategy(DriveStrategy):

    def drive(self):
        print("Normal drive strategy")
