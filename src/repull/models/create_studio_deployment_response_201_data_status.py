from enum import Enum

class CreateStudioDeploymentResponse201DataStatus(str, Enum):
    PROVISIONING = "provisioning"

    def __str__(self) -> str:
        return str(self.value)
