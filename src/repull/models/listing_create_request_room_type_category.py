from enum import Enum

class ListingCreateRequestRoomTypeCategory(str, Enum):
    ENTIRE_HOME = "entire_home"
    HOTEL_ROOM = "hotel_room"
    PRIVATE_ROOM = "private_room"
    SHARED_ROOM = "shared_room"

    def __str__(self) -> str:
        return str(self.value)
