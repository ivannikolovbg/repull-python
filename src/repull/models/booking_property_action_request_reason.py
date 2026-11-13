from enum import Enum

class BookingPropertyActionRequestReason(str, Enum):
    FULLY_BOOKED = "FULLY_BOOKED"
    ISSUES_BOOKING = "ISSUES_BOOKING"
    ISSUES_GUESTS = "ISSUES_GUESTS"
    OTHER = "OTHER"
    PROPERTY_NOT_AVAILABLE = "PROPERTY_NOT_AVAILABLE"
    RENOVATION = "RENOVATION"
    SEASON = "SEASON"
    STRATEGY = "STRATEGY"

    def __str__(self) -> str:
        return str(self.value)
