from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="TiketPropertyListingsItem")



@_attrs_define
class TiketPropertyListingsItem:
    """ 
        Attributes:
            listing_id (str | Unset):
            room_id (str | Unset):
            room_type_code (str | Unset):
            room_name (None | str | Unset):
     """

    listing_id: str | Unset = UNSET
    room_id: str | Unset = UNSET
    room_type_code: str | Unset = UNSET
    room_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        listing_id = self.listing_id

        room_id = self.room_id

        room_type_code = self.room_type_code

        room_name: None | str | Unset
        if isinstance(self.room_name, Unset):
            room_name = UNSET
        else:
            room_name = self.room_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if room_id is not UNSET:
            field_dict["roomId"] = room_id
        if room_type_code is not UNSET:
            field_dict["roomTypeCode"] = room_type_code
        if room_name is not UNSET:
            field_dict["roomName"] = room_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        listing_id = d.pop("listingId", UNSET)

        room_id = d.pop("roomId", UNSET)

        room_type_code = d.pop("roomTypeCode", UNSET)

        def _parse_room_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        room_name = _parse_room_name(d.pop("roomName", UNSET))


        tiket_property_listings_item = cls(
            listing_id=listing_id,
            room_id=room_id,
            room_type_code=room_type_code,
            room_name=room_name,
        )


        tiket_property_listings_item.additional_properties = d
        return tiket_property_listings_item

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
