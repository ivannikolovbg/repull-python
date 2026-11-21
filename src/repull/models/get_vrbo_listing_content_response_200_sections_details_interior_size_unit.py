from enum import Enum

class GetVrboListingContentResponse200SectionsDetailsInteriorSizeUnit(str, Enum):
    SQFT = "sqft"
    SQM = "sqm"

    def __str__(self) -> str:
        return str(self.value)
