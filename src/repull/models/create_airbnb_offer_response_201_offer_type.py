from enum import Enum

class CreateAirbnbOfferResponse201OfferType(str, Enum):
    PREAPPROVAL = "preapproval"
    SPECIAL_OFFER = "special_offer"

    def __str__(self) -> str:
        return str(self.value)
