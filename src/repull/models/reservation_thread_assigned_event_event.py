from enum import Enum

class ReservationThreadAssignedEventEvent(str, Enum):
    RESERVATION_THREAD_ASSIGNED = "reservation.thread.assigned"

    def __str__(self) -> str:
        return str(self.value)
