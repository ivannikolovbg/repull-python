from enum import Enum

class ReservationStatusDetail(str, Enum):
    REQUEST_EXPIRED = "request_expired"

    def __str__(self) -> str:
        return str(self.value)
