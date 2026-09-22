from enum import Enum

class AiOperationFailedEventEvent(str, Enum):
    AI_OPERATION_FAILED = "ai.operation.failed"

    def __str__(self) -> str:
        return str(self.value)
