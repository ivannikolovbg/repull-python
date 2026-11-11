from enum import Enum

class ConnectSessionAbandonedPayloadReason(str, Enum):
    CREDENTIALS_REJECTED = "credentials_rejected"
    FAILED = "failed"
    MAPPING_NOT_FINISHED = "mapping_not_finished"
    NOT_FINISHED = "not_finished"
    PROVIDER_APPROVAL_PENDING = "provider_approval_pending"

    def __str__(self) -> str:
        return str(self.value)
