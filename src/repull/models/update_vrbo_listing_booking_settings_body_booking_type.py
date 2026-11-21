from enum import Enum

class UpdateVrboListingBookingSettingsBodyBookingType(str, Enum):
    INSTANT = "INSTANT"
    QUOTEHOLD = "QUOTEHOLD"

    def __str__(self) -> str:
        return str(self.value)
