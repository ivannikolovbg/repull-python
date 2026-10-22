from enum import Enum

class CreateConnectSessionBodyMapping(str, Enum):
    API = "api"
    HOSTED = "hosted"

    def __str__(self) -> str:
        return str(self.value)
