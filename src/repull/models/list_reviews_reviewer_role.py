from enum import Enum

class ListReviewsReviewerRole(str, Enum):
    ALL = "all"
    GUEST = "guest"
    HOST = "host"

    def __str__(self) -> str:
        return str(self.value)
