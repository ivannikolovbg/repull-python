from enum import Enum

class ReservationCreateRequestStatus(str, Enum):
    CONFIRMED = "confirmed"
    TENTATIVE = "tentative"

    def __str__(self) -> str:
        return str(self.value)
