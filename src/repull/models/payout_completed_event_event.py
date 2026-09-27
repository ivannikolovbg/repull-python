from enum import Enum

class PayoutCompletedEventEvent(str, Enum):
    PAYOUT_COMPLETED = "payout.completed"

    def __str__(self) -> str:
        return str(self.value)
