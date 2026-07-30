from enum import Enum

class ListAirbnbAlterationsType(str, Enum):
    ALL = "all"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
