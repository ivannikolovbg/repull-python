from enum import Enum

class HospitableWebhookStatus(str, Enum):
    NOT_CONFIGURED = "not_configured"
    RECEIVING = "receiving"
    STALE = "stale"

    def __str__(self) -> str:
        return str(self.value)
