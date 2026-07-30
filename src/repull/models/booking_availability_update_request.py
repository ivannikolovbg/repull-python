from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.booking_availability_update_request_type import BookingAvailabilityUpdateRequestType
from typing import cast

if TYPE_CHECKING:
  from ..models.booking_availability_update import BookingAvailabilityUpdate
  from ..models.booking_pricing_rate_update import BookingPricingRateUpdate





T = TypeVar("T", bound="BookingAvailabilityUpdateRequest")



@_attrs_define
class BookingAvailabilityUpdateRequest:
    """ Body for `PUT /v1/channels/booking/availability`. Selects one of Booking's three ARI write paths via `type` and
    forwards `updates` verbatim to the connector.

        Attributes:
            type_ (BookingAvailabilityUpdateRequestType): `rates` → price + restrictions (`updateRates`); `availability` →
                inventory + stop-sell + restrictions (`updateAvailability`); `derived-pricing` → occupancy-derived pricing rules
                (`updateDerivedPricing`).
            property_id (int | str): Booking.com hotel/property id (numeric; accepted as int or numeric string).
            updates (list[BookingAvailabilityUpdate | BookingPricingRateUpdate]): For `type: "rates"` each item is a
                `BookingPricingRateUpdate`; for `type: "availability"` a `BookingAvailabilityUpdate`; for `type: "derived-
                pricing"` a derived-price rule set.
     """

    type_: BookingAvailabilityUpdateRequestType
    property_id: int | str
    updates: list[BookingAvailabilityUpdate | BookingPricingRateUpdate]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.booking_availability_update import BookingAvailabilityUpdate
        from ..models.booking_pricing_rate_update import BookingPricingRateUpdate
        type_ = self.type_.value

        property_id: int | str
        property_id = self.property_id

        updates = []
        for updates_item_data in self.updates:
            updates_item: dict[str, Any]
            if isinstance(updates_item_data, BookingPricingRateUpdate):
                updates_item = updates_item_data.to_dict()
            else:
                updates_item = updates_item_data.to_dict()

            updates.append(updates_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
            "property_id": property_id,
            "updates": updates,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.booking_availability_update import BookingAvailabilityUpdate
        from ..models.booking_pricing_rate_update import BookingPricingRateUpdate
        d = dict(src_dict)
        type_ = BookingAvailabilityUpdateRequestType(d.pop("type"))




        def _parse_property_id(data: object) -> int | str:
            return cast(int | str, data)

        property_id = _parse_property_id(d.pop("property_id"))


        updates = []
        _updates = d.pop("updates")
        for updates_item_data in (_updates):
            def _parse_updates_item(data: object) -> BookingAvailabilityUpdate | BookingPricingRateUpdate:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    updates_item_type_0 = BookingPricingRateUpdate.from_dict(data)



                    return updates_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                updates_item_type_1 = BookingAvailabilityUpdate.from_dict(data)



                return updates_item_type_1

            updates_item = _parse_updates_item(updates_item_data)

            updates.append(updates_item)


        booking_availability_update_request = cls(
            type_=type_,
            property_id=property_id,
            updates=updates,
        )


        booking_availability_update_request.additional_properties = d
        return booking_availability_update_request

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
