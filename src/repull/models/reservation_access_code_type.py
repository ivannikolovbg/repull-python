from enum import Enum

class ReservationAccessCodeType(str, Enum):
    BACKUP = "backup"
    GUEST = "guest"
    OTHER = "other"

    def __str__(self) -> str:
        return str(self.value)
