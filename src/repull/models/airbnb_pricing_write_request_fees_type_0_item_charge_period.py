from enum import Enum

class AirbnbPricingWriteRequestFeesType0ItemChargePeriod(str, Enum):
    PER_BOOKING = "PER_BOOKING"
    PER_NIGHT = "PER_NIGHT"

    def __str__(self) -> str:
        return str(self.value)
