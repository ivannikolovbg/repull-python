from enum import Enum

class AirbnbPricingWriteRequestModelType(str, Enum):
    LOS_RECORD = "LOS_RECORD"
    RATE_PLAN = "RATE_PLAN"
    STANDARD = "STANDARD"

    def __str__(self) -> str:
        return str(self.value)
