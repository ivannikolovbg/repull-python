from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="TiketMapListingsRequestMappingsItem")



@_attrs_define
class TiketMapListingsRequestMappingsItem:
    """ 
        Attributes:
            room_type_code (str): tiket.com room type id (`rooms[].roomTypeCode` on `GET
                /v1/channels/tiket/properties/{id}/rooms`).
            listing_id (int | None | Unset): Listing to map the room to. `null` unmaps it.
            create (bool | Unset): `true` creates a new listing from the room, with tiket.com's calendar. Do not send
                `listingId` with it.
     """

    room_type_code: str
    listing_id: int | None | Unset = UNSET
    create: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        room_type_code = self.room_type_code

        listing_id: int | None | Unset
        if isinstance(self.listing_id, Unset):
            listing_id = UNSET
        else:
            listing_id = self.listing_id

        create = self.create


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "roomTypeCode": room_type_code,
        })
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if create is not UNSET:
            field_dict["create"] = create

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        room_type_code = d.pop("roomTypeCode")

        def _parse_listing_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        listing_id = _parse_listing_id(d.pop("listingId", UNSET))


        create = d.pop("create", UNSET)

        tiket_map_listings_request_mappings_item = cls(
            room_type_code=room_type_code,
            listing_id=listing_id,
            create=create,
        )


        tiket_map_listings_request_mappings_item.additional_properties = d
        return tiket_map_listings_request_mappings_item

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
