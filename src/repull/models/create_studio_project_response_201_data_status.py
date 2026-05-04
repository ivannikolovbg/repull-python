from enum import Enum

class CreateStudioProjectResponse201DataStatus(str, Enum):
    ARCHIVED = "archived"
    BUILDING = "building"
    DRAFT = "draft"
    LIVE = "live"

    def __str__(self) -> str:
        return str(self.value)
