from enum import Enum

class WebhookSubscriptionStatus(str, Enum):
    ACTIVE = "active"
    DISABLED = "disabled"
    PAUSED = "paused"

    def __str__(self) -> str:
        return str(self.value)
