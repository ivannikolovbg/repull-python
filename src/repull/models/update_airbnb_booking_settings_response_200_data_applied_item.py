from enum import Enum

class UpdateAirbnbBookingSettingsResponse200DataAppliedItem(str, Enum):
    AVAILABILITYRULES = "availabilityRules"
    BOOKINGSETTINGS = "bookingSettings"

    def __str__(self) -> str:
        return str(self.value)
