from enum import Enum

class ListAirbnbTransactionsStatus(str, Enum):
    COMPLETED = "COMPLETED"
    RELEASED = "RELEASED"
    UPCOMING = "UPCOMING"

    def __str__(self) -> str:
        return str(self.value)
