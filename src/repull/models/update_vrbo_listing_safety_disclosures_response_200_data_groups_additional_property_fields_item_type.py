from enum import Enum

class UpdateVrboListingSafetyDisclosuresResponse200DataGroupsAdditionalPropertyFieldsItemType(str, Enum):
    CHECKBOX = "checkbox"
    CHECKBOXGROUP = "checkboxGroup"
    CHOICE = "choice"
    MEASUREMENT = "measurement"
    NUMBER = "number"
    TEXT = "text"

    def __str__(self) -> str:
        return str(self.value)
