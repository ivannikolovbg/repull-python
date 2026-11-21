from enum import Enum

class GetVrboListingVideosSource(str, Enum):
    LIVE = "live"
    STORED = "stored"

    def __str__(self) -> str:
        return str(self.value)
