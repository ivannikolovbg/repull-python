from enum import Enum

class ListingKind(str, Enum):
    HOME = "home"
    ROOM_TYPE = "room_type"

    def __str__(self) -> str:
        return str(self.value)
