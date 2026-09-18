from enum import Enum

class AirbnbSafetyDisclosureType(str, Enum):
    ANIMALS = "animals"
    CLIMBING_OR_PLAY_STRUCTURE = "climbing_or_play_structure"
    HAS_PETS = "has_pets"
    HEIGHTS_WITH_NO_FENCE = "heights_with_no_fence"
    LAKE_OR_RIVER_OR_WATER_BODY = "lake_or_river_or_water_body"
    LIMITED_AMENITIES = "limited_amenities"
    LIMITED_PARKING = "limited_parking"
    NOISE_MONITOR = "noise_monitor"
    POOL_OR_JACUZZI_WITH_NO_FENCE = "pool_or_jacuzzi_with_no_fence"
    POTENTIAL_NOISE = "potential_noise"
    REQUIRES_STAIRS = "requires_stairs"
    SHARED_SPACES = "shared_spaces"
    SURVEILLANCE = "surveillance"
    WEAPONS = "weapons"

    def __str__(self) -> str:
        return str(self.value)
