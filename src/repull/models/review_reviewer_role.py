from enum import Enum

class ReviewReviewerRole(str, Enum):
    GUEST = "guest"
    HOST = "host"

    def __str__(self) -> str:
        return str(self.value)
