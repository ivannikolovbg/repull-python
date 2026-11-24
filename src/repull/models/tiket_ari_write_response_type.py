from enum import Enum

class TiketAriWriteResponseType(str, Enum):
    AVAILABILITY = "availability"
    RATES = "rates"
    RESTRICTIONS = "restrictions"

    def __str__(self) -> str:
        return str(self.value)
