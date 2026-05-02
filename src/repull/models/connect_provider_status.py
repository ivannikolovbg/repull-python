from enum import Enum

class ConnectProviderStatus(str, Enum):
    BETA = "beta"
    COMING_SOON = "coming-soon"
    LIVE = "live"

    def __str__(self) -> str:
        return str(self.value)
