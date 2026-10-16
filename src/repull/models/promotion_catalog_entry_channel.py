from enum import Enum

class PromotionCatalogEntryChannel(str, Enum):
    AIRBNB = "airbnb"
    BOOKING = "booking"

    def __str__(self) -> str:
        return str(self.value)
