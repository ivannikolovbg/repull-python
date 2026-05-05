from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.reservation_webhook_object import ReservationWebhookObject





T = TypeVar("T", bound="ReservationCreatedPayload")



@_attrs_define
class ReservationCreatedPayload:
    """ Payload for `reservation.created`. A new reservation arrived from any connected channel or direct booking. Stripe-
    pattern envelope: `data.object` carries the reservation snapshot.

        Attributes:
            object_ (ReservationWebhookObject): Lightweight reservation snapshot delivered as `data.object` on every
                reservation webhook event. Stable across `reservation.created`, `reservation.updated`, and
                `reservation.cancelled`. Fetch the full reservation via `GET /v1/reservations/{id}` if you need pricing, guest
                contact info, or audit history — those are deliberately omitted to keep deliveries small.
     """

    object_: ReservationWebhookObject
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.reservation_webhook_object import ReservationWebhookObject
        object_ = self.object_.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "object": object_,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reservation_webhook_object import ReservationWebhookObject
        d = dict(src_dict)
        object_ = ReservationWebhookObject.from_dict(d.pop("object"))




        reservation_created_payload = cls(
            object_=object_,
        )


        reservation_created_payload.additional_properties = d
        return reservation_created_payload

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
