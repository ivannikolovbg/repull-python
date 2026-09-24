from enum import Enum

class ReservationPendingReason(str, Enum):
    GUEST_PAYMENT = "guest_payment"
    GUEST_VERIFICATION = "guest_verification"
    HOST_APPROVAL = "host_approval"

    def __str__(self) -> str:
        return str(self.value)
