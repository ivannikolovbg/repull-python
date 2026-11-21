from enum import Enum

class GetVrboListingDescriptionsSource(str, Enum):
    LIVE = "live"
    STORED = "stored"

    def __str__(self) -> str:
        return str(self.value)
