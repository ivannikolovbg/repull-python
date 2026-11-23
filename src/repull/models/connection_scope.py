from enum import Enum

class ConnectionScope(str, Enum):
    LISTINGS = "listings"
    WORKSPACE = "workspace"

    def __str__(self) -> str:
        return str(self.value)
