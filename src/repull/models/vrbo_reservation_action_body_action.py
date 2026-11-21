from enum import Enum

class VrboReservationActionBodyAction(str, Enum):
    ACCEPT = "accept"
    CANCEL = "cancel"
    CHARGE = "charge"
    DECLINE = "decline"
    REFUND = "refund"

    def __str__(self) -> str:
        return str(self.value)
