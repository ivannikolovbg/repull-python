from enum import Enum

class UpdateVrboListingPropertyResponse200DataInteriorSizeUnit(str, Enum):
    SQFT = "sqft"
    SQM = "sqm"

    def __str__(self) -> str:
        return str(self.value)
