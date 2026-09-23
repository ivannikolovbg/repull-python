from enum import Enum

class ListingPublishBookingResponseChannel(str, Enum):
    BOOKING = "booking"

    def __str__(self) -> str:
        return str(self.value)
