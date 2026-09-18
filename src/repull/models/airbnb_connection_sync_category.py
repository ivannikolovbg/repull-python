from enum import Enum

class AirbnbConnectionSyncCategory(str, Enum):
    NONE = "none"
    SYNC_ALL = "sync_all"
    SYNC_RATES_AND_AVAILABILITY = "sync_rates_and_availability"

    def __str__(self) -> str:
        return str(self.value)
