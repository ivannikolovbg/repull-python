from enum import Enum

class GetReservationSummaryResponse200GroupByItem(str, Enum):
    CHANNEL = "channel"
    LISTING = "listing"
    MONTH = "month"

    def __str__(self) -> str:
        return str(self.value)
