from enum import Enum

class ListBookingReservationsType(str, Enum):
    DETAILS = "details"
    MODIFIED = "modified"
    NEW = "new"

    def __str__(self) -> str:
        return str(self.value)
