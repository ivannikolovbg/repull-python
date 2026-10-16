from enum import Enum

class PromotionManagedBy(str, Enum):
    API = "api"
    CHANNEL = "channel"

    def __str__(self) -> str:
        return str(self.value)
