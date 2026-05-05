from enum import Enum

class ReservationCancelledPayloadCancelledBy(str, Enum):
    GUEST = "guest"
    HOST = "host"
    PLATFORM = "platform"

    def __str__(self) -> str:
        return str(self.value)
