from enum import Enum

class BookingSetupBodyAction(str, Enum):
    ADD_ROOM = "add-room"
    ADD_UNIT = "add-unit"
    ADVANCE = "advance"
    CHECK_LEGAL_STATUS = "check-legal-status"
    CHECK_READINESS = "check-readiness"
    CREATE_LEGAL_ENTITY = "create-legal-entity"
    CREATE_PROPERTY = "create-property"
    OPEN_PROPERTY = "open-property"
    SET_CONTACTS = "set-contacts"
    SET_POLICIES = "set-policies"

    def __str__(self) -> str:
        return str(self.value)
