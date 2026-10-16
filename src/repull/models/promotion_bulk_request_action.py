from enum import Enum

class PromotionBulkRequestAction(str, Enum):
    ADD = "add"
    REMOVE = "remove"

    def __str__(self) -> str:
        return str(self.value)
