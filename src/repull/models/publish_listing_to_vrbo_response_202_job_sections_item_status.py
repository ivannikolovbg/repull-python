from enum import Enum

class PublishListingToVrboResponse202JobSectionsItemStatus(str, Enum):
    DONE = "done"
    FAILED = "failed"
    PENDING = "pending"
    REJECTED = "rejected"
    RUNNING = "running"

    def __str__(self) -> str:
        return str(self.value)
