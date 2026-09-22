from enum import Enum

class AiOperationCompletedEventEvent(str, Enum):
    AI_OPERATION_COMPLETED = "ai.operation.completed"

    def __str__(self) -> str:
        return str(self.value)
