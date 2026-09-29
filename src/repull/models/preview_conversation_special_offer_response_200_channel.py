from enum import Enum

class PreviewConversationSpecialOfferResponse200Channel(str, Enum):
    AIRBNB = "airbnb"
    VRBO = "vrbo"

    def __str__(self) -> str:
        return str(self.value)
