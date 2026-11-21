from enum import Enum

class PublishListingToVrboBodySectionsItem(str, Enum):
    AMENITIES = "amenities"
    BOOKING_SETTINGS = "booking-settings"
    CANCELLATION = "cancellation"
    DESCRIPTION = "description"
    FEES = "fees"
    HOUSE_RULES = "house-rules"
    PRICING = "pricing"
    PROPERTY = "property"
    RATES = "rates"

    def __str__(self) -> str:
        return str(self.value)
