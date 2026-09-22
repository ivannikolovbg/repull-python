from enum import Enum

class BookingPropertyListingsItemMappedVia(str, Enum):
    PROPERTY = "property"
    ROOM = "room"

    def __str__(self) -> str:
        return str(self.value)
