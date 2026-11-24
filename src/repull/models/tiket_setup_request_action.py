from enum import Enum

class TiketSetupRequestAction(str, Enum):
    ADD_RATE_PLAN = "add-rate-plan"
    ADD_ROOM = "add-room"
    CHECK_ACTIVATION = "check-activation"
    CONFIRM_CONTENT_MAPPING = "confirm-content-mapping"
    CREATE_PROPERTY = "create-property"
    DISCONNECT = "disconnect"
    REFRESH = "refresh"
    REQUEST_ACTIVATION = "request-activation"
    REQUEST_CONTENT_MAPPING = "request-content-mapping"
    REQUEST_REGISTRATION = "request-registration"
    SET_PUSH_RATE_PLANS = "set-push-rate-plans"
    SET_SYNC = "set-sync"
    SET_TIKET_HOTEL_ID = "set-tiket-hotel-id"

    def __str__(self) -> str:
        return str(self.value)
