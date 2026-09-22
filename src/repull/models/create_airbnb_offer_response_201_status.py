from enum import Enum

class CreateAirbnbOfferResponse201Status(str, Enum):
    ACCEPTED = "accepted"
    ACTIVE = "active"
    DECLINED = "declined"
    EXPIRED = "expired"
    PENDING = "pending"
    VOIDED = "voided"

    def __str__(self) -> str:
        return str(self.value)
