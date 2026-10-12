from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GetHotelResponse200RoomTypesItem")



@_attrs_define
class GetHotelResponse200RoomTypesItem:
    """ 
        Attributes:
            listing_id (str | Unset): The room type's listing id — use it with every /v1/listings, /v1/availability and
                /v1/reservations endpoint.
            name (None | str | Unset):
            unit_count (int | Unset): Rooms of this type.
     """

    listing_id: str | Unset = UNSET
    name: None | str | Unset = UNSET
    unit_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        listing_id = self.listing_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        unit_count = self.unit_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if name is not UNSET:
            field_dict["name"] = name
        if unit_count is not UNSET:
            field_dict["unitCount"] = unit_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        listing_id = d.pop("listingId", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        unit_count = d.pop("unitCount", UNSET)

        get_hotel_response_200_room_types_item = cls(
            listing_id=listing_id,
            name=name,
            unit_count=unit_count,
        )


        get_hotel_response_200_room_types_item.additional_properties = d
        return get_hotel_response_200_room_types_item

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
