from enum import Enum

class UploadAirbnbListingPhotosBodyPhotosItemCategory(str, Enum):
    LISTING = "listing"
    LISTING_AMENITY = "listing_amenity"
    ROOM = "room"
    ROOM_AMENITY = "room_amenity"

    def __str__(self) -> str:
        return str(self.value)
