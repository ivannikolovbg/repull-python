from enum import Enum

class UpdateAirbnbBookingSettingsResponse200DataSettingsCancellationShortStayPolicy(str, Enum):
    FIRM = "firm"
    FLEXIBLE = "flexible"
    MODERATE = "moderate"
    STRICT = "strict"
    SUPER_STRICT = "super_strict"

    def __str__(self) -> str:
        return str(self.value)
