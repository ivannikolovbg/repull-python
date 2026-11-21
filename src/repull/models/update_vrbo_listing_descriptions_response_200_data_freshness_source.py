from enum import Enum

class UpdateVrboListingDescriptionsResponse200DataFreshnessSource(str, Enum):
    LIVE = "live"
    STORED = "stored"

    def __str__(self) -> str:
        return str(self.value)
