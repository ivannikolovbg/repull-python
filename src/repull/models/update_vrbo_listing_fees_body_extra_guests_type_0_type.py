from enum import Enum

class UpdateVrboListingFeesBodyExtraGuestsType0Type(str, Enum):
    PER_NIGHT_PER_GUEST = "PER_NIGHT_PER_GUEST"
    PER_STAY_PER_GUEST = "PER_STAY_PER_GUEST"

    def __str__(self) -> str:
        return str(self.value)
