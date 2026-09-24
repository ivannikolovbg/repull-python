from enum import Enum

class ListingContentUpdateRequestCheckoutTasksType0ItemTaskType(str, Enum):
    ADDITIONAL_REQUESTS = "additional_requests"
    GATHER_TOWELS = "gather_towels"
    LOCK_UP = "lock_up"
    RETURN_KEYS = "return_keys"
    THROW_TRASH = "throw_trash"
    TURN_THINGS_OFF = "turn_things_off"

    def __str__(self) -> str:
        return str(self.value)
