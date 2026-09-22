from enum import Enum

class WithdrawAirbnbOfferResponse200Status(str, Enum):
    ACCEPTED = "accepted"
    ACTIVE = "active"
    DECLINED = "declined"
    EXPIRED = "expired"
    PENDING = "pending"
    VOIDED = "voided"

    def __str__(self) -> str:
        return str(self.value)
