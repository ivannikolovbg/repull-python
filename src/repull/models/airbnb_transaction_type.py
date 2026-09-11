from enum import Enum

class AirbnbTransactionType(str, Enum):
    PAYOUT = "Payout"
    RESERVATION = "Reservation"
    RESOLUTION_ADJUSTMENT = "Resolution_Adjustment"

    def __str__(self) -> str:
        return str(self.value)
