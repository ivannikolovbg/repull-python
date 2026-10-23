from enum import Enum

class ImportFromChannexResponse201DataRatePlansItemStatus(str, Enum):
    CREATED = "created"
    MATCHED = "matched"
    NEEDS_ACTION = "needs_action"

    def __str__(self) -> str:
        return str(self.value)
