from enum import Enum

class ReviewCreatedEventType(str, Enum):
    REVIEW_CREATED = "review.created"

    def __str__(self) -> str:
        return str(self.value)
