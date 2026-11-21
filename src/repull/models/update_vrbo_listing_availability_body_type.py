from enum import Enum

class UpdateVrboListingAvailabilityBodyType(str, Enum):
    CALENDAR = "calendar"

    def __str__(self) -> str:
        return str(self.value)
