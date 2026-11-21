from enum import Enum

class GetVrboListingPropertyResponse200DataInteriorSizeUnit(str, Enum):
    SQFT = "sqft"
    SQM = "sqm"

    def __str__(self) -> str:
        return str(self.value)
