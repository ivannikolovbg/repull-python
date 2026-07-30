from enum import Enum

class GetUsageLogsStatus(str, Enum):
    VALUE_0 = "2xx"
    VALUE_1 = "3xx"
    VALUE_2 = "4xx"
    VALUE_3 = "5xx"

    def __str__(self) -> str:
        return str(self.value)
