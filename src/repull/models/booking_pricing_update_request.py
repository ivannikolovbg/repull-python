from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.booking_pricing_rate_update import BookingPricingRateUpdate





T = TypeVar("T", bound="BookingPricingUpdateRequest")



@_attrs_define
class BookingPricingUpdateRequest:
    """ Body for `PUT /v1/channels/booking/listings/{id}/pricing`. Pricing on Booking is per-room/per-rate-plan, so
    `room_id` + `rate_id` are required on every update.

        Attributes:
            updates (list[BookingPricingRateUpdate]):
     """

    updates: list[BookingPricingRateUpdate]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.booking_pricing_rate_update import BookingPricingRateUpdate
        updates = []
        for updates_item_data in self.updates:
            updates_item = updates_item_data.to_dict()
            updates.append(updates_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "updates": updates,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.booking_pricing_rate_update import BookingPricingRateUpdate
        d = dict(src_dict)
        updates = []
        _updates = d.pop("updates")
        for updates_item_data in (_updates):
            updates_item = BookingPricingRateUpdate.from_dict(updates_item_data)



            updates.append(updates_item)


        booking_pricing_update_request = cls(
            updates=updates,
        )


        booking_pricing_update_request.additional_properties = d
        return booking_pricing_update_request

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
