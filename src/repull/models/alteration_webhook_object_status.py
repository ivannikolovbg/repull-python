from enum import Enum

class AlterationWebhookObjectStatus(str, Enum):
    ACCEPTED = "accepted"
    CANCELLED = "cancelled"
    DECLINED = "declined"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
