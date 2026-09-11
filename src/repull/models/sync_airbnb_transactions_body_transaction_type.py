from enum import Enum

class SyncAirbnbTransactionsBodyTransactionType(str, Enum):
    COMPLETED = "COMPLETED"
    UPCOMING = "UPCOMING"

    def __str__(self) -> str:
        return str(self.value)
