from enum import Enum

class SubmitMewsCredentialsBodyCredentialsEnvironment(str, Enum):
    DEMO = "demo"
    PRODUCTION = "production"

    def __str__(self) -> str:
        return str(self.value)
