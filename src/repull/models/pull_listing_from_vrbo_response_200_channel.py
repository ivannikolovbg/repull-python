from enum import Enum

class PullListingFromVrboResponse200Channel(str, Enum):
    VRBO = "vrbo"

    def __str__(self) -> str:
        return str(self.value)
