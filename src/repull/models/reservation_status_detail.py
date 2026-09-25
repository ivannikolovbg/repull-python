from enum import Enum

class ReservationStatusDetail(str, Enum):
    CANCELLED_BY_GUEST = "cancelled_by_guest"
    CANCELLED_BY_HOST = "cancelled_by_host"
    CANCELLED_BY_PLATFORM = "cancelled_by_platform"
    DECLINED = "declined"
    HOLD_VOIDED = "hold_voided"
    REQUEST_EXPIRED = "request_expired"
    REQUEST_VOIDED = "request_voided"
    VERIFICATION_FAILED = "verification_failed"

    def __str__(self) -> str:
        return str(self.value)
