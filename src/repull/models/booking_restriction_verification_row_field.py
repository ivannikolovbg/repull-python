from enum import Enum

class BookingRestrictionVerificationRowField(str, Enum):
    CLOSEDTOARRIVAL = "closedToArrival"
    CLOSEDTODEPARTURE = "closedToDeparture"
    MAXSTAY = "maxStay"
    MAXSTAYARRIVAL = "maxStayArrival"
    MINSTAY = "minStay"
    MINSTAYARRIVAL = "minStayArrival"

    def __str__(self) -> str:
        return str(self.value)
