from enum import Enum

class AirbnbReservationStatus(str, Enum):
    ACCEPTED = "accepted"
    CANCELLED = "cancelled"
    DENIED = "denied"
    ERROR = "error"
    EXPIRED = "expired"
    FAILED_VERIFICATION = "failed_verification"
    PENDING = "pending"
    REQUEST_VOIDED = "request_voided"

    def __str__(self) -> str:
        return str(self.value)
