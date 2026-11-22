from enum import Enum

class ListVrboReviewsStatus(str, Enum):
    ALL = "all"
    RESPONDED = "responded"
    UNANSWERED = "unanswered"

    def __str__(self) -> str:
        return str(self.value)
