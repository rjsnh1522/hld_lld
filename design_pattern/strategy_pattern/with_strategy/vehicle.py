from strategy_pattern.with_strategy.strategy.drive_strategy import DriveStrategy


class Vehicle:

    def __init__(self, drive_strategy=DriveStrategy):
        self._drive_strategy = drive_strategy

    def set_drive_strategy(self, drive_strategy=DriveStrategy):
        self._drive_strategy = drive_strategy

    def drive(self):
        self._drive_strategy.drive()
