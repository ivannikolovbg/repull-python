from enum import Enum

class GetVrboReservationResponse200DataFreshnessSource(str, Enum):
    LIVE = "live"

    def __str__(self) -> str:
        return str(self.value)
