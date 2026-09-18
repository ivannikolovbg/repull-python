from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="UpdateAirbnbListingRoomBodyRoomAmenitiesItem")



@_attrs_define
class UpdateAirbnbListingRoomBodyRoomAmenitiesItem:
    """ 
        Attributes:
            id (str):
            name (str | Unset):
            value (bool | float | str | Unset):
     """

    id: str
    name: str | Unset = UNSET
    value: bool | float | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        value: bool | float | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
        })
        if name is not UNSET:
            field_dict["name"] = name
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name", UNSET)

        def _parse_value(data: object) -> bool | float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(bool | float | str | Unset, data)

        value = _parse_value(d.pop("value", UNSET))


        update_airbnb_listing_room_body_room_amenities_item = cls(
            id=id,
            name=name,
            value=value,
        )

        return update_airbnb_listing_room_body_room_amenities_item

