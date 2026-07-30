from enum import Enum

class GetAirbnbListingSettingsType(str, Enum):
    ALL = "all"
    HOSTS = "hosts"
    LOCALES = "locales"
    PERMITS = "permits"

    def __str__(self) -> str:
        return str(self.value)
