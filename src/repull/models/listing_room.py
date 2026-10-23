from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.listing_room_beds_item import ListingRoomBedsItem





T = TypeVar("T", bound="ListingRoom")



@_attrs_define
class ListingRoom:
    """ 
        Attributes:
            type_ (str | Unset): Room kind, Airbnb spelling: `bedroom`, `living_room`, `full_bathroom`, `kitchen`, …
                Example: bedroom.
            name (None | str | Unset):
            number (int | None | Unset): Position among rooms of the same type (bedroom 1, 2, …).
            is_private (bool | None | Unset):
            beds (list[ListingRoomBedsItem] | Unset):
     """

    type_: str | Unset = UNSET
    name: None | str | Unset = UNSET
    number: int | None | Unset = UNSET
    is_private: bool | None | Unset = UNSET
    beds: list[ListingRoomBedsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.listing_room_beds_item import ListingRoomBedsItem
        type_ = self.type_

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        number: int | None | Unset
        if isinstance(self.number, Unset):
            number = UNSET
        else:
            number = self.number

        is_private: bool | None | Unset
        if isinstance(self.is_private, Unset):
            is_private = UNSET
        else:
            is_private = self.is_private

        beds: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.beds, Unset):
            beds = []
            for beds_item_data in self.beds:
                beds_item = beds_item_data.to_dict()
                beds.append(beds_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if type_ is not UNSET:
            field_dict["type"] = type_
        if name is not UNSET:
            field_dict["name"] = name
        if number is not UNSET:
            field_dict["number"] = number
        if is_private is not UNSET:
            field_dict["isPrivate"] = is_private
        if beds is not UNSET:
            field_dict["beds"] = beds

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.listing_room_beds_item import ListingRoomBedsItem
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        number = _parse_number(d.pop("number", UNSET))


        def _parse_is_private(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_private = _parse_is_private(d.pop("isPrivate", UNSET))


        _beds = d.pop("beds", UNSET)
        beds: list[ListingRoomBedsItem] | Unset = UNSET
        if _beds is not UNSET:
            beds = []
            for beds_item_data in _beds:
                beds_item = ListingRoomBedsItem.from_dict(beds_item_data)



                beds.append(beds_item)


        listing_room = cls(
            type_=type_,
            name=name,
            number=number,
            is_private=is_private,
            beds=beds,
        )


        listing_room.additional_properties = d
        return listing_room

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
