from enum import Enum

class PromotionManagedKey(str, Enum):
    MONTHLY_DISCOUNT = "monthly_discount"
    WEEKLY_DISCOUNT = "weekly_discount"

    def __str__(self) -> str:
        return str(self.value)
