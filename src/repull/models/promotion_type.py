from enum import Enum

class PromotionType(str, Enum):
    CAMPAIGN = "campaign"
    COUNTRY = "country"
    CUSTOM = "custom"
    DEAL = "deal"
    EARLY_BOOKER = "early_booker"
    LAST_MINUTE = "last_minute"
    MOBILE = "mobile"
    NEW_LISTING = "new_listing"
    TOP_RATED_GUESTS = "top_rated_guests"

    def __str__(self) -> str:
        return str(self.value)
