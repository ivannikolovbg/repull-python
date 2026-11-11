from enum import Enum

class GetReservationSummaryResponse200Basis(str, Enum):
    BOOKED = "booked"
    CHECK_IN = "check_in"
    STAY = "stay"

    def __str__(self) -> str:
        return str(self.value)
