from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.reservation_updated_payload_previous_attributes import ReservationUpdatedPayloadPreviousAttributes
  from ..models.reservation_webhook_object import ReservationWebhookObject





T = TypeVar("T", bound="ReservationUpdatedPayload")



@_attrs_define
class ReservationUpdatedPayload:
    """ Payload for `reservation.updated`. Dates, status, or any tracked field changed on an existing reservation.
    `data.object` is the post-change snapshot; `data.previousAttributes` lists ONLY the fields that actually moved, with
    their prior values. Fields not in `previousAttributes` did not change.

        Attributes:
            object_ (ReservationWebhookObject): Lightweight reservation snapshot delivered as `data.object` on every
                reservation webhook event. Stable across `reservation.created`, `reservation.updated`, and
                `reservation.cancelled`. Fetch the full reservation via `GET /v1/reservations/{id}` if you need pricing, guest
                contact info, or audit history — those are deliberately omitted to keep deliveries small.
            previous_attributes (ReservationUpdatedPayloadPreviousAttributes | Unset): Sparse map: every key here is a field
                on the reservation snapshot whose value changed in this event, mapped to its prior value. Mirrors the keys of
                `ReservationWebhookObject` (e.g. `checkinDate`, `checkoutDate`, `status`). Receivers can diff `object[k]` vs
                `previousAttributes[k]` to know what moved. Example: {'checkinDate': '2026-06-11', 'checkoutDate':
                '2026-06-16'}.
     """

    object_: ReservationWebhookObject
    previous_attributes: ReservationUpdatedPayloadPreviousAttributes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.reservation_updated_payload_previous_attributes import ReservationUpdatedPayloadPreviousAttributes
        from ..models.reservation_webhook_object import ReservationWebhookObject
        object_ = self.object_.to_dict()

        previous_attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.previous_attributes, Unset):
            previous_attributes = self.previous_attributes.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "object": object_,
        })
        if previous_attributes is not UNSET:
            field_dict["previousAttributes"] = previous_attributes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reservation_updated_payload_previous_attributes import ReservationUpdatedPayloadPreviousAttributes
        from ..models.reservation_webhook_object import ReservationWebhookObject
        d = dict(src_dict)
        object_ = ReservationWebhookObject.from_dict(d.pop("object"))




        _previous_attributes = d.pop("previousAttributes", UNSET)
        previous_attributes: ReservationUpdatedPayloadPreviousAttributes | Unset
        if isinstance(_previous_attributes,  Unset):
            previous_attributes = UNSET
        else:
            previous_attributes = ReservationUpdatedPayloadPreviousAttributes.from_dict(_previous_attributes)




        reservation_updated_payload = cls(
            object_=object_,
            previous_attributes=previous_attributes,
        )


        reservation_updated_payload.additional_properties = d
        return reservation_updated_payload

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
