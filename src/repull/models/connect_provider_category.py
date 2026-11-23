from enum import Enum

class ConnectProviderCategory(str, Enum):
    APP = "app"
    OTA = "ota"
    PMS = "pms"

    def __str__(self) -> str:
        return str(self.value)
