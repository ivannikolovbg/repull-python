from enum import Enum

class ListingCreateRequestCancellationPolicy(str, Enum):
    FLEXIBLE = "flexible"
    MODERATE = "moderate"
    STRICT = "strict"
    SUPER_STRICT = "super_strict"

    def __str__(self) -> str:
        return str(self.value)
