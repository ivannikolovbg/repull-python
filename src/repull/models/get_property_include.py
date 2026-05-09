from enum import Enum

class GetPropertyInclude(str, Enum):
    AMENITIES = "amenities"

    def __str__(self) -> str:
        return str(self.value)
