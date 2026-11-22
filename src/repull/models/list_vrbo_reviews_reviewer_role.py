from enum import Enum

class ListVrboReviewsReviewerRole(str, Enum):
    ALL = "all"
    GUEST = "guest"
    HOST = "host"

    def __str__(self) -> str:
        return str(self.value)
