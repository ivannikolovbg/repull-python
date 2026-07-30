from enum import Enum

class AirbnbPricingWriteRequestType(str, Enum):
    CALENDAR = "calendar"
    CURRENCY = "currency"
    FEES = "fees"
    LOS = "los"
    MODEL = "model"
    RATE_PLAN = "rate-plan"
    RULE = "rule"
    STANDARD = "standard"

    def __str__(self) -> str:
        return str(self.value)
