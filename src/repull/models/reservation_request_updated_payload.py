from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.reservation_request_updated_payload_request_status import ReservationRequestUpdatedPayloadRequestStatus
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.reservation_request_updated_payload_previous_attributes import ReservationRequestUpdatedPayloadPreviousAttributes
  from ..models.reservation_webhook_object import ReservationWebhookObject





T = TypeVar("T", bound="ReservationRequestUpdatedPayload")



@_attrs_define
class ReservationRequestUpdatedPayload:
    """ Payload for `reservation.request.updated`. A booking request stopped waiting on the host. `requestStatus` says how;
    `data.object` is the reservation after the change (`status` `confirmed` once accepted, `cancelled` otherwise). An
    accepted request also fires `reservation.created`. Fires when the channel reports the outcome, whoever acted — the
    API, a connected app or the channel's own app.

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
            request_status (ReservationRequestUpdatedPayloadRequestStatus): `accepted` — it is a booking now; `declined` —
                by the host; `expired` — nobody answered in time; `voided` — withdrawn by the guest, or voided by the channel
                (for example the guest failed verification). Example: accepted.
            previous_attributes (ReservationRequestUpdatedPayloadPreviousAttributes): Fields of `object` that moved, with
                their prior values — always `{ "status": "pending" }` here. Example: {'status': 'pending'}.
            source_status (None | str | Unset): The channel's own status value, unmapped (Airbnb: `accept`, `deny`,
                `timeout`, `pending_voided`, …) — for reconciling against the channel. Example: accept.
            occurred_at (datetime.datetime | Unset):  Example: 2026-09-22T11:42:10.000Z.
            revision (datetime.datetime | None | Unset):
     """

    object_: ReservationWebhookObject
    request_status: ReservationRequestUpdatedPayloadRequestStatus
    previous_attributes: ReservationRequestUpdatedPayloadPreviousAttributes
    source_status: None | str | Unset = UNSET
    occurred_at: datetime.datetime | Unset = UNSET
    revision: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.reservation_request_updated_payload_previous_attributes import ReservationRequestUpdatedPayloadPreviousAttributes
        from ..models.reservation_webhook_object import ReservationWebhookObject
        object_ = self.object_.to_dict()

        request_status = self.request_status.value

        previous_attributes = self.previous_attributes.to_dict()

        source_status: None | str | Unset
        if isinstance(self.source_status, Unset):
            source_status = UNSET
        else:
            source_status = self.source_status

        occurred_at: str | Unset = UNSET
        if not isinstance(self.occurred_at, Unset):
            occurred_at = self.occurred_at.isoformat()

        revision: None | str | Unset
        if isinstance(self.revision, Unset):
            revision = UNSET
        elif isinstance(self.revision, datetime.datetime):
            revision = self.revision.isoformat()
        else:
            revision = self.revision


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "object": object_,
            "requestStatus": request_status,
            "previousAttributes": previous_attributes,
        })
        if source_status is not UNSET:
            field_dict["sourceStatus"] = source_status
        if occurred_at is not UNSET:
            field_dict["occurredAt"] = occurred_at
        if revision is not UNSET:
            field_dict["revision"] = revision

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reservation_request_updated_payload_previous_attributes import ReservationRequestUpdatedPayloadPreviousAttributes
        from ..models.reservation_webhook_object import ReservationWebhookObject
        d = dict(src_dict)
        object_ = ReservationWebhookObject.from_dict(d.pop("object"))




        request_status = ReservationRequestUpdatedPayloadRequestStatus(d.pop("requestStatus"))




        previous_attributes = ReservationRequestUpdatedPayloadPreviousAttributes.from_dict(d.pop("previousAttributes"))




        def _parse_source_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_status = _parse_source_status(d.pop("sourceStatus", UNSET))


        _occurred_at = d.pop("occurredAt", UNSET)
        occurred_at: datetime.datetime | Unset
        if isinstance(_occurred_at,  Unset):
            occurred_at = UNSET
        else:
            occurred_at = isoparse(_occurred_at)




        def _parse_revision(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                revision_type_0 = isoparse(data)



                return revision_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        revision = _parse_revision(d.pop("revision", UNSET))


        reservation_request_updated_payload = cls(
            object_=object_,
            request_status=request_status,
            previous_attributes=previous_attributes,
            source_status=source_status,
            occurred_at=occurred_at,
            revision=revision,
        )


        reservation_request_updated_payload.additional_properties = d
        return reservation_request_updated_payload

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
