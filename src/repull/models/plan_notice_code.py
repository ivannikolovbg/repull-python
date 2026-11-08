from enum import Enum

class PlanNoticeCode(str, Enum):
    LISTINGS_HELD_BACK = "listings_held_back"
    LISTINGS_OVER_PLAN = "listings_over_plan"

    def __str__(self) -> str:
        return str(self.value)
