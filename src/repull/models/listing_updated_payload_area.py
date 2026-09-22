from enum import Enum

class ListingUpdatedPayloadArea(str, Enum):
    AVAILABILITY = "availability"
    BOOKING_SETTINGS = "booking_settings"
    CONTENT = "content"
    PRICING = "pricing"
    RULES = "rules"
    SYNC_SETTINGS = "sync_settings"

    def __str__(self) -> str:
        return str(self.value)
