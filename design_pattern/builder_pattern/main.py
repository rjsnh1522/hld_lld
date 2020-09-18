from abc import ABC


class Builder(ABC):
    pass

    @property
    def project(self) -> None:
        pass

    @property
    def produce_part_a(self) -> None:
        pass

    @property
    def produce_part_b(self) -> None:
        pass

    @property
    def produce_part_c(self) -> None:
        pass
