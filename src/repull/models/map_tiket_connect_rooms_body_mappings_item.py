from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MapTiketConnectRoomsBodyMappingsItem")



@_attrs_define
class MapTiketConnectRoomsBodyMappingsItem:
    """ 
        Attributes:
            room_id (int): `rooms[].roomId` from `GET /v1/connect/tiket/rooms`.
            listing_id (int | None | Unset):
            create (bool | Unset):
     """

    room_id: int
    listing_id: int | None | Unset = UNSET
    create: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        room_id = self.room_id

        listing_id: int | None | Unset
        if isinstance(self.listing_id, Unset):
            listing_id = UNSET
        else:
            listing_id = self.listing_id

        create = self.create


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "roomId": room_id,
        })
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if create is not UNSET:
            field_dict["create"] = create

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        room_id = d.pop("roomId")

        def _parse_listing_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        listing_id = _parse_listing_id(d.pop("listingId", UNSET))


        create = d.pop("create", UNSET)

        map_tiket_connect_rooms_body_mappings_item = cls(
            room_id=room_id,
            listing_id=listing_id,
            create=create,
        )


        map_tiket_connect_rooms_body_mappings_item.additional_properties = d
        return map_tiket_connect_rooms_body_mappings_item

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
