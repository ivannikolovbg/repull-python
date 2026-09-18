from enum import Enum

class CreateAirbnbListingRoomBodyRoomType(str, Enum):
    BATHROOM = "bathroom"
    BEDROOM = "bedroom"
    DINING_ROOM = "dining_room"
    ENTRANCE_TO_HOME = "entrance_to_home"
    FAMILY_ROOM = "family_room"
    GARAGE = "garage"
    KITCHEN = "kitchen"
    LAUNDRY_ROOM = "laundry_room"
    LIVING_ROOM = "living_room"
    OFFICE = "office"
    OUTDOOR_SPACE = "outdoor_space"
    RECREATION_AREA = "recreation_area"
    STUDIO = "studio"

    def __str__(self) -> str:
        return str(self.value)
