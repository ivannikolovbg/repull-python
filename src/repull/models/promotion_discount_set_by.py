from enum import Enum

class PromotionDiscountSetBy(str, Enum):
    CHANNEL = "channel"
    HOST = "host"

    def __str__(self) -> str:
        return str(self.value)
