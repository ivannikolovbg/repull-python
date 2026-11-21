from enum import Enum

class ListVrboTransactionsStatus(str, Enum):
    COMPLETED = "COMPLETED"
    UPCOMING = "UPCOMING"

    def __str__(self) -> str:
        return str(self.value)
