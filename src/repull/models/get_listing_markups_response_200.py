from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_listing_markups_response_200_airbnb_item import GetListingMarkupsResponse200AirbnbItem
  from ..models.get_listing_markups_response_200_booking_item import GetListingMarkupsResponse200BookingItem





T = TypeVar("T", bound="GetListingMarkupsResponse200")



@_attrs_define
class GetListingMarkupsResponse200:
    """ 
        Attributes:
            id (str | Unset): Repull listing id.
            airbnb (list[GetListingMarkupsResponse200AirbnbItem] | Unset):
            booking (list[GetListingMarkupsResponse200BookingItem] | Unset):
     """

    id: str | Unset = UNSET
    airbnb: list[GetListingMarkupsResponse200AirbnbItem] | Unset = UNSET
    booking: list[GetListingMarkupsResponse200BookingItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_listing_markups_response_200_airbnb_item import GetListingMarkupsResponse200AirbnbItem
        from ..models.get_listing_markups_response_200_booking_item import GetListingMarkupsResponse200BookingItem
        id = self.id

        airbnb: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.airbnb, Unset):
            airbnb = []
            for airbnb_item_data in self.airbnb:
                airbnb_item = airbnb_item_data.to_dict()
                airbnb.append(airbnb_item)



        booking: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.booking, Unset):
            booking = []
            for booking_item_data in self.booking:
                booking_item = booking_item_data.to_dict()
                booking.append(booking_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if airbnb is not UNSET:
            field_dict["airbnb"] = airbnb
        if booking is not UNSET:
            field_dict["booking"] = booking

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_listing_markups_response_200_airbnb_item import GetListingMarkupsResponse200AirbnbItem
        from ..models.get_listing_markups_response_200_booking_item import GetListingMarkupsResponse200BookingItem
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _airbnb = d.pop("airbnb", UNSET)
        airbnb: list[GetListingMarkupsResponse200AirbnbItem] | Unset = UNSET
        if _airbnb is not UNSET:
            airbnb = []
            for airbnb_item_data in _airbnb:
                airbnb_item = GetListingMarkupsResponse200AirbnbItem.from_dict(airbnb_item_data)



                airbnb.append(airbnb_item)


        _booking = d.pop("booking", UNSET)
        booking: list[GetListingMarkupsResponse200BookingItem] | Unset = UNSET
        if _booking is not UNSET:
            booking = []
            for booking_item_data in _booking:
                booking_item = GetListingMarkupsResponse200BookingItem.from_dict(booking_item_data)



                booking.append(booking_item)


        get_listing_markups_response_200 = cls(
            id=id,
            airbnb=airbnb,
            booking=booking,
        )


        get_listing_markups_response_200.additional_properties = d
        return get_listing_markups_response_200

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
