from enum import Enum

class ReviewWebhookObjectReviewerRole(str, Enum):
    GUEST = "guest"
    HOST = "host"

    def __str__(self) -> str:
        return str(self.value)
