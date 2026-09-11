from enum import Enum

class ReviewRespondedEventType(str, Enum):
    REVIEW_RESPONDED = "review.responded"

    def __str__(self) -> str:
        return str(self.value)
