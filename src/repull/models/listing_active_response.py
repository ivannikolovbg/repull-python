from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.booking_property_open_result import BookingPropertyOpenResult





T = TypeVar("T", bound="ListingActiveResponse")



@_attrs_define
class ListingActiveResponse:
    """ 
        Attributes:
            id (str | Unset): The listing id (id fields are serialized as strings to preserve precision).
            active (bool | Unset): The resulting active state after the toggle.
            booking_properties (list[BookingPropertyOpenResult] | Unset): Only when activating: what happened to the
                Booking.com properties this listing is mapped to. Activating a listing opens its Booking.com property if
                Booking.com still has it in a build stage. Empty when the listing has no Booking.com property.
     """

    id: str | Unset = UNSET
    active: bool | Unset = UNSET
    booking_properties: list[BookingPropertyOpenResult] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.booking_property_open_result import BookingPropertyOpenResult
        id = self.id

        active = self.active

        booking_properties: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.booking_properties, Unset):
            booking_properties = []
            for booking_properties_item_data in self.booking_properties:
                booking_properties_item = booking_properties_item_data.to_dict()
                booking_properties.append(booking_properties_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if active is not UNSET:
            field_dict["active"] = active
        if booking_properties is not UNSET:
            field_dict["bookingProperties"] = booking_properties

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.booking_property_open_result import BookingPropertyOpenResult
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        active = d.pop("active", UNSET)

        _booking_properties = d.pop("bookingProperties", UNSET)
        booking_properties: list[BookingPropertyOpenResult] | Unset = UNSET
        if _booking_properties is not UNSET:
            booking_properties = []
            for booking_properties_item_data in _booking_properties:
                booking_properties_item = BookingPropertyOpenResult.from_dict(booking_properties_item_data)



                booking_properties.append(booking_properties_item)


        listing_active_response = cls(
            id=id,
            active=active,
            booking_properties=booking_properties,
        )


        listing_active_response.additional_properties = d
        return listing_active_response

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
