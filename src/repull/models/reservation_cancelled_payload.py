from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.reservation_cancelled_payload_cancelled_by import ReservationCancelledPayloadCancelledBy
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.reservation_webhook_object import ReservationWebhookObject





T = TypeVar("T", bound="ReservationCancelledPayload")



@_attrs_define
class ReservationCancelledPayload:
    """ Payload for `reservation.cancelled`. A reservation was cancelled by the guest, host, or platform. `data.object`
    reflects the post-cancel snapshot (status will be `cancelled`); top-level fields capture cancellation metadata.

        Attributes:
            object_ (ReservationWebhookObject): Lightweight reservation snapshot delivered as `data.object` on every
                reservation webhook event. Stable across `reservation.created`, `reservation.updated`, and
                `reservation.cancelled`. Fetch the full reservation via `GET /v1/reservations/{id}` if you need pricing, guest
                contact info, or audit history — those are deliberately omitted to keep deliveries small.
            cancelled_at (datetime.datetime | Unset): When the cancellation was recorded. Example: 2026-05-01T14:00:00.000Z.
            cancelled_by (ReservationCancelledPayloadCancelledBy | Unset): Who initiated the cancellation. Example: guest.
            reason (None | str | Unset): Free-form cancellation reason from the source channel, if available. Example:
                guest_requested.
     """

    object_: ReservationWebhookObject
    cancelled_at: datetime.datetime | Unset = UNSET
    cancelled_by: ReservationCancelledPayloadCancelledBy | Unset = UNSET
    reason: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.reservation_webhook_object import ReservationWebhookObject
        object_ = self.object_.to_dict()

        cancelled_at: str | Unset = UNSET
        if not isinstance(self.cancelled_at, Unset):
            cancelled_at = self.cancelled_at.isoformat()

        cancelled_by: str | Unset = UNSET
        if not isinstance(self.cancelled_by, Unset):
            cancelled_by = self.cancelled_by.value


        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "object": object_,
        })
        if cancelled_at is not UNSET:
            field_dict["cancelledAt"] = cancelled_at
        if cancelled_by is not UNSET:
            field_dict["cancelledBy"] = cancelled_by
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reservation_webhook_object import ReservationWebhookObject
        d = dict(src_dict)
        object_ = ReservationWebhookObject.from_dict(d.pop("object"))




        _cancelled_at = d.pop("cancelledAt", UNSET)
        cancelled_at: datetime.datetime | Unset
        if isinstance(_cancelled_at,  Unset):
            cancelled_at = UNSET
        else:
            cancelled_at = isoparse(_cancelled_at)




        _cancelled_by = d.pop("cancelledBy", UNSET)
        cancelled_by: ReservationCancelledPayloadCancelledBy | Unset
        if isinstance(_cancelled_by,  Unset):
            cancelled_by = UNSET
        else:
            cancelled_by = ReservationCancelledPayloadCancelledBy(_cancelled_by)




        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))


        reservation_cancelled_payload = cls(
            object_=object_,
            cancelled_at=cancelled_at,
            cancelled_by=cancelled_by,
            reason=reason,
        )


        reservation_cancelled_payload.additional_properties = d
        return reservation_cancelled_payload

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
