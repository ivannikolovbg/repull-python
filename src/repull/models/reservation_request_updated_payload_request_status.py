from enum import Enum

class ReservationRequestUpdatedPayloadRequestStatus(str, Enum):
    ACCEPTED = "accepted"
    DECLINED = "declined"
    EXPIRED = "expired"
    VOIDED = "voided"

    def __str__(self) -> str:
        return str(self.value)
