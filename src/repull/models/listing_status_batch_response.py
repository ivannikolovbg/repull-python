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





T = TypeVar("T", bound="ListingStatusBatchResponse")



@_attrs_define
class ListingStatusBatchResponse:
    """ 
        Attributes:
            active (bool): The state every listing in the request is now in.
            updated (list[str]): Listing ids whose state this call changed, in request order.
            unchanged (list[str]): Listing ids that were already in the requested state, in request order.
            booking_properties (list[BookingPropertyOpenResult] | Unset): Only when `active` is true: one entry per
                Booking.com property the listings in the request are mapped to, saying whether it was opened. Every listing in
                the request counts, including those in `unchanged`, so sending `active: true` again retries an open Booking.com
                refused. Empty when none of the listings has a Booking.com property.
     """

    active: bool
    updated: list[str]
    unchanged: list[str]
    booking_properties: list[BookingPropertyOpenResult] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.booking_property_open_result import BookingPropertyOpenResult
        active = self.active

        updated = self.updated



        unchanged = self.unchanged



        booking_properties: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.booking_properties, Unset):
            booking_properties = []
            for booking_properties_item_data in self.booking_properties:
                booking_properties_item = booking_properties_item_data.to_dict()
                booking_properties.append(booking_properties_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "active": active,
            "updated": updated,
            "unchanged": unchanged,
        })
        if booking_properties is not UNSET:
            field_dict["bookingProperties"] = booking_properties

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.booking_property_open_result import BookingPropertyOpenResult
        d = dict(src_dict)
        active = d.pop("active")

        updated = cast(list[str], d.pop("updated"))


        unchanged = cast(list[str], d.pop("unchanged"))


        _booking_properties = d.pop("bookingProperties", UNSET)
        booking_properties: list[BookingPropertyOpenResult] | Unset = UNSET
        if _booking_properties is not UNSET:
            booking_properties = []
            for booking_properties_item_data in _booking_properties:
                booking_properties_item = BookingPropertyOpenResult.from_dict(booking_properties_item_data)



                booking_properties.append(booking_properties_item)


        listing_status_batch_response = cls(
            active=active,
            updated=updated,
            unchanged=unchanged,
            booking_properties=booking_properties,
        )


        listing_status_batch_response.additional_properties = d
        return listing_status_batch_response

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
