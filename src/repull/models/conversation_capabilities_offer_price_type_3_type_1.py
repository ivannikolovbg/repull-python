from enum import Enum

class ConversationCapabilitiesOfferPriceType3Type1(str, Enum):
    BREAKDOWN = "breakdown"
    TOTAL = "total"

    def __str__(self) -> str:
        return str(self.value)
