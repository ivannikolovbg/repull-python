from enum import Enum

class UpdateAirbnbBookingSettingsBodyCheckInStartType1(str, Enum):
    FLEXIBLE = "FLEXIBLE"

    def __str__(self) -> str:
        return str(self.value)
