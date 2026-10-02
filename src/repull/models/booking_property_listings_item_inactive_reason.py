from enum import Enum

class BookingPropertyListingsItemInactiveReason(str, Enum):
    DEACTIVATED = "deactivated"
    PLAN_LIMIT = "plan_limit"
    UNLISTED_ON_AIRBNB = "unlisted_on_airbnb"

    def __str__(self) -> str:
        return str(self.value)
