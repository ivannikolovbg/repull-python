from enum import Enum

class AirbnbListingDetailsWriteRequestPropertyTypeGroup(str, Enum):
    APARTMENTS = "apartments"
    BNB = "bnb"
    BOUTIQUE_HOTELS_AND_MORE = "boutique_hotels_and_more"
    HOUSES = "houses"
    SECONDARY_UNITS = "secondary_units"
    UNIQUE_HOMES = "unique_homes"

    def __str__(self) -> str:
        return str(self.value)
