from enum import Enum

class ChargePer(str, Enum):
    GUEST = "guest"
    GUEST_NIGHT = "guest_night"
    NIGHT = "night"
    STAY = "stay"

    def __str__(self) -> str:
        return str(self.value)
