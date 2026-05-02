from enum import Enum

class ListWebhookDeliveriesStatus(str, Enum):
    ALL = "all"
    FAILURE = "failure"
    SUCCESS = "success"

    def __str__(self) -> str:
        return str(self.value)
