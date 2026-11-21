from enum import Enum

class PublishListingToVrboBodySectionsItem(str, Enum):
    AMENITIES = "amenities"
    BOOKING_SETTINGS = "booking-settings"
    CANCELLATION = "cancellation"
    DESCRIPTIONS = "descriptions"
    DETAILS = "details"
    FEES = "fees"
    HOUSE_RULES = "house-rules"
    PRICING = "pricing"
    RATES = "rates"

    def __str__(self) -> str:
        return str(self.value)
