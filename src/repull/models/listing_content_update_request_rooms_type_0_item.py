from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.listing_content_update_request_rooms_type_0_item_beds_type_0_item import ListingContentUpdateRequestRoomsType0ItemBedsType0Item





T = TypeVar("T", bound="ListingContentUpdateRequestRoomsType0Item")



@_attrs_define
class ListingContentUpdateRequestRoomsType0Item:
    """ 
        Attributes:
            room_type (str): e.g. `bedroom`, `full_bathroom`, `half_bathroom`, `living_room`, `kitchen`. Not a closed list —
                Airbnb validates it at publish and its refusal comes back in the publish result. Example: bedroom.
            room_name (None | str | Unset): Your own label, e.g. "Primary bedroom".
            room_number (int | None | Unset): Order among rooms of the same type, from 1.
            is_private (bool | None | Unset): Whether the room is private to the guest.
            beds (list[ListingContentUpdateRequestRoomsType0ItemBedsType0Item] | None | Unset):
     """

    room_type: str
    room_name: None | str | Unset = UNSET
    room_number: int | None | Unset = UNSET
    is_private: bool | None | Unset = UNSET
    beds: list[ListingContentUpdateRequestRoomsType0ItemBedsType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.listing_content_update_request_rooms_type_0_item_beds_type_0_item import ListingContentUpdateRequestRoomsType0ItemBedsType0Item
        room_type = self.room_type

        room_name: None | str | Unset
        if isinstance(self.room_name, Unset):
            room_name = UNSET
        else:
            room_name = self.room_name

        room_number: int | None | Unset
        if isinstance(self.room_number, Unset):
            room_number = UNSET
        else:
            room_number = self.room_number

        is_private: bool | None | Unset
        if isinstance(self.is_private, Unset):
            is_private = UNSET
        else:
            is_private = self.is_private

        beds: list[dict[str, Any]] | None | Unset
        if isinstance(self.beds, Unset):
            beds = UNSET
        elif isinstance(self.beds, list):
            beds = []
            for beds_type_0_item_data in self.beds:
                beds_type_0_item = beds_type_0_item_data.to_dict()
                beds.append(beds_type_0_item)


        else:
            beds = self.beds


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "roomType": room_type,
        })
        if room_name is not UNSET:
            field_dict["roomName"] = room_name
        if room_number is not UNSET:
            field_dict["roomNumber"] = room_number
        if is_private is not UNSET:
            field_dict["isPrivate"] = is_private
        if beds is not UNSET:
            field_dict["beds"] = beds

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.listing_content_update_request_rooms_type_0_item_beds_type_0_item import ListingContentUpdateRequestRoomsType0ItemBedsType0Item
        d = dict(src_dict)
        room_type = d.pop("roomType")

        def _parse_room_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        room_name = _parse_room_name(d.pop("roomName", UNSET))


        def _parse_room_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        room_number = _parse_room_number(d.pop("roomNumber", UNSET))


        def _parse_is_private(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_private = _parse_is_private(d.pop("isPrivate", UNSET))


        def _parse_beds(data: object) -> list[ListingContentUpdateRequestRoomsType0ItemBedsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                beds_type_0 = []
                _beds_type_0 = data
                for beds_type_0_item_data in (_beds_type_0):
                    beds_type_0_item = ListingContentUpdateRequestRoomsType0ItemBedsType0Item.from_dict(beds_type_0_item_data)



                    beds_type_0.append(beds_type_0_item)

                return beds_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ListingContentUpdateRequestRoomsType0ItemBedsType0Item] | None | Unset, data)

        beds = _parse_beds(d.pop("beds", UNSET))


        listing_content_update_request_rooms_type_0_item = cls(
            room_type=room_type,
            room_name=room_name,
            room_number=room_number,
            is_private=is_private,
            beds=beds,
        )


        listing_content_update_request_rooms_type_0_item.additional_properties = d
        return listing_content_update_request_rooms_type_0_item

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
