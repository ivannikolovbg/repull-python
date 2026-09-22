from enum import Enum

class ReviewCreatedEventEvent(str, Enum):
    REVIEW_CREATED = "review.created"

    def __str__(self) -> str:
        return str(self.value)
