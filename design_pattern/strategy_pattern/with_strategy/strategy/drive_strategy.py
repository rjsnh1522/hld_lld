import abc


class DriveStrategy(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def drive(self):
        pass
