from enum import Enum

class StudioDeploymentStatus(str, Enum):
    BUILDING = "building"
    FAILED = "failed"
    LIVE = "live"
    PROVISIONING = "provisioning"
    SUSPENDED = "suspended"

    def __str__(self) -> str:
        return str(self.value)
