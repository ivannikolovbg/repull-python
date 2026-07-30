from enum import Enum

class UpdateAirbnbMessageBodyAction(str, Enum):
    EDIT = "edit"
    REACT = "react"
    READ = "read"
    UNSEND = "unsend"

    def __str__(self) -> str:
        return str(self.value)
