from enum import Enum

class ListReviewsPlatform(str, Enum):
    AIRBNB = "airbnb"
    BOOKING = "booking"
    VRBO = "vrbo"

    def __str__(self) -> str:
        return str(self.value)
