from enum import Enum

class GetVrboListingAdditionalInfoSource(str, Enum):
    LIVE = "live"
    STORED = "stored"

    def __str__(self) -> str:
        return str(self.value)
