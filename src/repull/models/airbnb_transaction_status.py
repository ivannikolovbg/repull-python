from enum import Enum

class AirbnbTransactionStatus(str, Enum):
    COMPLETED = "COMPLETED"
    RELEASED = "RELEASED"
    UPCOMING = "UPCOMING"

    def __str__(self) -> str:
        return str(self.value)
