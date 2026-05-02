from enum import Enum

class ConnectProviderCategory(str, Enum):
    OTA = "ota"
    PMS = "pms"

    def __str__(self) -> str:
        return str(self.value)
