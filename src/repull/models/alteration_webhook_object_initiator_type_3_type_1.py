from enum import Enum

class AlterationWebhookObjectInitiatorType3Type1(str, Enum):
    GUEST = "guest"
    HOST = "host"

    def __str__(self) -> str:
        return str(self.value)
