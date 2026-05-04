from enum import Enum

class ListAirbnbReservationsStatus(str, Enum):
    ACCEPTED = "accepted"
    CANCELLED = "cancelled"
    COMPLETED = "completed"
    DENIED = "denied"
    FAILED_VERIFICATION = "failed_verification"
    PENDING = "pending"
    REQUEST_VOIDED = "request_voided"

    def __str__(self) -> str:
        return str(self.value)
