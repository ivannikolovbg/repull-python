from enum import Enum

class GetAirbnbBookingSettingsResponse200DataCheckInStartType1(str, Enum):
    FLEXIBLE = "FLEXIBLE"

    def __str__(self) -> str:
        return str(self.value)
