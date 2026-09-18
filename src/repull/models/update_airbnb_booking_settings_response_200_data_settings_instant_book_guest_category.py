from enum import Enum

class UpdateAirbnbBookingSettingsResponse200DataSettingsInstantBookGuestCategory(str, Enum):
    EVERYONE = "everyone"
    EXPERIENCED_GUESTS_ONLY = "experienced_guests_only"
    OFF = "off"
    RECOMMENDED_GUESTS_ONLY = "recommended_guests_only"

    def __str__(self) -> str:
        return str(self.value)
