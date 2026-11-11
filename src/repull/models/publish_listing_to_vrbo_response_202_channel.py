from enum import Enum

class PublishListingToVrboResponse202Channel(str, Enum):
    VRBO = "vrbo"

    def __str__(self) -> str:
        return str(self.value)
