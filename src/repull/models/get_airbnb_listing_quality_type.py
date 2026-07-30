from enum import Enum

class GetAirbnbListingQualityType(str, Enum):
    ALL = "all"
    ISSUES = "issues"
    STANDARDS = "standards"
    STATS = "stats"

    def __str__(self) -> str:
        return str(self.value)
