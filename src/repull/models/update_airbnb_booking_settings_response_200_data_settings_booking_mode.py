from enum import Enum

class UpdateAirbnbBookingSettingsResponse200DataSettingsBookingMode(str, Enum):
    INSTANT_BOOK = "instant_book"
    REQUEST_TO_BOOK = "request_to_book"

    def __str__(self) -> str:
        return str(self.value)
