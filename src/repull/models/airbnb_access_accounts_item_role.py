from enum import Enum

class AirbnbAccessAccountsItemRole(str, Enum):
    COHOST = "cohost"
    OWNER = "owner"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
