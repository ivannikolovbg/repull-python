from enum import Enum

class AccountDisconnectedPayloadReason(str, Enum):
    AUTH_EXPIRED = "auth_expired"
    MANUAL_DISCONNECT = "manual_disconnect"
    REFRESH_TOKEN_REJECTED = "refresh_token_rejected"
    REVOKED_UPSTREAM = "revoked_upstream"

    def __str__(self) -> str:
        return str(self.value)
