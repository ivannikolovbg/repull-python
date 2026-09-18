from enum import Enum

class AirbnbListingDetailsWriteRequestCheckInOptionCategory(str, Enum):
    DOORMAN_ENTRY = "doorman_entry"
    HOST_CHECKIN = "host_checkin"
    KEYPAD = "keypad"
    LOCKBOX = "lockbox"
    OTHER_CHECKIN = "other_checkin"
    SMARTLOCK = "smartlock"

    def __str__(self) -> str:
        return str(self.value)
