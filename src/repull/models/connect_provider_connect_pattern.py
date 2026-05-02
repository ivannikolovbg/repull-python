from enum import Enum

class ConnectProviderConnectPattern(str, Enum):
    ACTIVATION = "activation"
    CLAIM = "claim"
    CREDENTIALS = "credentials"
    OAUTH = "oauth"

    def __str__(self) -> str:
        return str(self.value)
