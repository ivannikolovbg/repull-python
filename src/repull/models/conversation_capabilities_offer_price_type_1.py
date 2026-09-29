from enum import Enum

class ConversationCapabilitiesOfferPriceType1(str, Enum):
    BREAKDOWN = "breakdown"
    TOTAL = "total"

    def __str__(self) -> str:
        return str(self.value)
