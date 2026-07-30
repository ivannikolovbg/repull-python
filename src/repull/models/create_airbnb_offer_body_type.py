from enum import Enum

class CreateAirbnbOfferBodyType(str, Enum):
    OFFER = "offer"
    PREAPPROVAL = "preapproval"

    def __str__(self) -> str:
        return str(self.value)
