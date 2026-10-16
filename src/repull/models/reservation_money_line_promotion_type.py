from enum import Enum

class ReservationMoneyLinePromotionType(str, Enum):
    CUSTOM = "custom"
    MOBILE = "mobile"
    NEW_LISTING = "new_listing"
    TOP_RATED_GUESTS = "top_rated_guests"

    def __str__(self) -> str:
        return str(self.value)
