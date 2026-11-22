from enum import Enum

class GetVrboListingSettingsType(str, Enum):
    ALL = "all"
    LOCALES = "locales"
    PERMITS = "permits"

    def __str__(self) -> str:
        return str(self.value)
