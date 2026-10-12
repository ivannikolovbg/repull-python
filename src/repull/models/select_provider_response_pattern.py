from enum import Enum

class SelectProviderResponsePattern(str, Enum):
    ACTIVATION = "activation"
    CLAIM = "claim"
    CREDENTIALS = "credentials"
    EXTRANET = "extranet"
    OAUTH = "oauth"

    def __str__(self) -> str:
        return str(self.value)
