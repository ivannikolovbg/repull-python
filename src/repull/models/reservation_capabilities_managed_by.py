from enum import Enum

class ReservationCapabilitiesManagedBy(str, Enum):
    PMS = "pms"
    REPULL = "repull"

    def __str__(self) -> str:
        return str(self.value)
