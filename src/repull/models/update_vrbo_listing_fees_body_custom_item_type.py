from enum import Enum

class UpdateVrboListingFeesBodyCustomItemType(str, Enum):
    PER_NIGHT = "PER_NIGHT"
    PER_STAY = "PER_STAY"

    def __str__(self) -> str:
        return str(self.value)
