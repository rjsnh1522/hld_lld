from strategy_pattern.with_strategy.strategy.drive_strategy import DriveStrategy


class SportDriveStrategy(DriveStrategy):

    def drive(self):
        print("Sport drive strategy")
