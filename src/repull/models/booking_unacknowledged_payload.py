from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.reservation_webhook_object import ReservationWebhookObject





T = TypeVar("T", bound="BookingUnacknowledgedPayload")



@_attrs_define
class BookingUnacknowledgedPayload:
    """ Payload for `booking.unacknowledged`. A booking changed and your system has not acknowledged the change through the
    revision feed. Sent once per outstanding revision — not once per check — so a booking that keeps waiting does not
    keep alerting. A booking that changes AGAIN mints a new revision and does alert again, because that is a new thing
    to acknowledge. Acknowledging the revision stops it.

        Attributes:
            object_ (ReservationWebhookObject): Lightweight reservation snapshot delivered as `data.object` on every
                reservation webhook event. Stable across `reservation.created`, `reservation.updated`, and
                `reservation.cancelled`. Fetch the full reservation via `GET /v1/reservations/{id}` if you need pricing, guest
                contact info, or audit history — those are deliberately omitted to keep deliveries small.

                **Stay terms are the one exception to that rule.** `cancellationPolicy`, `checkInTime` and `checkOutTime` ride
                on every delivery, because the decisions they drive — is a refund owed, when can housekeeping turn the unit over
                — are made at the moment the webhook lands, not on a follow-up fetch. They are operational parameters of the
                booking, not contact or payment data. Guest email, payment method and payment reference stay off the snapshot;
                see `GET /v1/reservations/{id}`.

                All three are `null` when the source channel did not supply them. They are never defaulted: a fabricated policy
                is worse than a missing one.
            revision_id (UUID): The outstanding revision. Acknowledge this to stop the alert.
            outstanding_since (datetime.datetime): When the booking actually changed — NOT when we noticed. Revisions are
                minted when you first poll the feed, so a mint timestamp would measure how recently you looked rather than how
                long the booking has waited.
            outstanding_hours (int | Unset): Whole hours since `outstandingSince`, for convenience.
     """

    object_: ReservationWebhookObject
    revision_id: UUID
    outstanding_since: datetime.datetime
    outstanding_hours: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.reservation_webhook_object import ReservationWebhookObject
        object_ = self.object_.to_dict()

        revision_id = str(self.revision_id)

        outstanding_since = self.outstanding_since.isoformat()

        outstanding_hours = self.outstanding_hours


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "object": object_,
            "revisionId": revision_id,
            "outstandingSince": outstanding_since,
        })
        if outstanding_hours is not UNSET:
            field_dict["outstandingHours"] = outstanding_hours

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reservation_webhook_object import ReservationWebhookObject
        d = dict(src_dict)
        object_ = ReservationWebhookObject.from_dict(d.pop("object"))




        revision_id = UUID(d.pop("revisionId"))




        outstanding_since = isoparse(d.pop("outstandingSince"))




        outstanding_hours = d.pop("outstandingHours", UNSET)

        booking_unacknowledged_payload = cls(
            object_=object_,
            revision_id=revision_id,
            outstanding_since=outstanding_since,
            outstanding_hours=outstanding_hours,
        )


        booking_unacknowledged_payload.additional_properties = d
        return booking_unacknowledged_payload

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
