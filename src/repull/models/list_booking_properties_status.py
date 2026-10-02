from enum import Enum

class ListBookingPropertiesStatus(str, Enum):
    ACTIVE = "active"
    ALL = "all"
    INACTIVE = "inactive"

    def __str__(self) -> str:
        return str(self.value)
