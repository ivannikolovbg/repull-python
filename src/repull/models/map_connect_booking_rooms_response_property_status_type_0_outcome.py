from enum import Enum

class MapConnectBookingRoomsResponsePropertyStatusType0Outcome(str, Enum):
    BLOCKED = "blocked"
    FAILED = "failed"
    NOT_NEEDED = "not_needed"
    OPENED = "opened"
    STATUS_UNKNOWN = "status_unknown"

    def __str__(self) -> str:
        return str(self.value)
