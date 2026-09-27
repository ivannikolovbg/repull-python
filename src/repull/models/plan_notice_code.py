from enum import Enum

class PlanNoticeCode(str, Enum):
    LISTINGS_HELD_BACK = "listings_held_back"

    def __str__(self) -> str:
        return str(self.value)
