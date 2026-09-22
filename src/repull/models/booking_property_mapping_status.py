from enum import Enum

class BookingPropertyMappingStatus(str, Enum):
    MAPPED = "mapped"
    UNMAPPED = "unmapped"

    def __str__(self) -> str:
        return str(self.value)
