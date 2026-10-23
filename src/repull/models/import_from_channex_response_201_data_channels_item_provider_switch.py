from enum import Enum

class ImportFromChannexResponse201DataChannelsItemProviderSwitch(str, Enum):
    REQUIRED = "required"
    SWITCHED = "switched"
    UNSUPPORTED = "unsupported"

    def __str__(self) -> str:
        return str(self.value)
