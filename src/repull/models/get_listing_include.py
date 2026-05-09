from enum import Enum

class GetListingInclude(str, Enum):
    AMENITIES = "amenities"

    def __str__(self) -> str:
        return str(self.value)
