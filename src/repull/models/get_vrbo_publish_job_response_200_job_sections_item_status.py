from enum import Enum

class GetVrboPublishJobResponse200JobSectionsItemStatus(str, Enum):
    DONE = "done"
    FAILED = "failed"
    PENDING = "pending"
    REJECTED = "rejected"
    RUNNING = "running"

    def __str__(self) -> str:
        return str(self.value)
