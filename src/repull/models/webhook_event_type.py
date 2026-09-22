from enum import Enum

class WebhookEventType(str, Enum):
    ACCOUNT_CREATED = "account.created"
    ACCOUNT_DISCONNECTED = "account.disconnected"
    AI_OPERATION_COMPLETED = "ai.operation.completed"
    AI_OPERATION_FAILED = "ai.operation.failed"
    CALENDAR_UPDATED = "calendar.updated"
    LISTING_CREATED = "listing.created"
    LISTING_DELETED = "listing.deleted"
    LISTING_REACTIVATED = "listing.reactivated"
    LISTING_SUSPENDED = "listing.suspended"
    LISTING_UPDATED = "listing.updated"
    PAYMENT_COMPLETED = "payment.completed"
    PAYMENT_REFUNDED = "payment.refunded"
    REPULL_PING = "repull.ping"
    RESERVATION_ALTERATION_CREATED = "reservation.alteration.created"
    RESERVATION_ALTERATION_RESPONDED = "reservation.alteration.responded"
    RESERVATION_CANCELLED = "reservation.cancelled"
    RESERVATION_CREATED = "reservation.created"
    RESERVATION_MESSAGE_RECEIVED = "reservation.message.received"
    RESERVATION_UPDATED = "reservation.updated"
    REVIEW_CREATED = "review.created"
    REVIEW_RESPONDED = "review.responded"
    USAGE_QUOTA_WARNING = "usage.quota.warning"

    def __str__(self) -> str:
        return str(self.value)
