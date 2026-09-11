from enum import Enum

class AirbnbTransactionStatus(str, Enum):
    COMPLETED = "COMPLETED"
    UPCOMING = "UPCOMING"

    def __str__(self) -> str:
        return str(self.value)
