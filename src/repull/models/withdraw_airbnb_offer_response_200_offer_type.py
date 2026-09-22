from enum import Enum

class WithdrawAirbnbOfferResponse200OfferType(str, Enum):
    PREAPPROVAL = "preapproval"
    SPECIAL_OFFER = "special_offer"

    def __str__(self) -> str:
        return str(self.value)
