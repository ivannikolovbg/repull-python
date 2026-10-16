from enum import Enum

class PromotionStatus(str, Enum):
    ACTIVE = "active"
    ELIGIBLE = "eligible"
    EXPIRED = "expired"
    INACTIVE = "inactive"
    SCHEDULED = "scheduled"

    def __str__(self) -> str:
        return str(self.value)
