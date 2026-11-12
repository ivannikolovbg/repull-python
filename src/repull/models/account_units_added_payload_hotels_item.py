from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="AccountUnitsAddedPayloadHotelsItem")



@_attrs_define
class AccountUnitsAddedPayloadHotelsItem:
    """ 
        Attributes:
            hotel_id (str): Booking.com property ID.
            name (None | str):
            is_new (bool): `true` when the login had no unit on this property before; `false` when rooms were added to a
                property it already had.
     """

    hotel_id: str
    name: None | str
    is_new: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        hotel_id = self.hotel_id

        name: None | str
        name = self.name

        is_new = self.is_new


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "hotelId": hotel_id,
            "name": name,
            "isNew": is_new,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hotel_id = d.pop("hotelId")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))


        is_new = d.pop("isNew")

        account_units_added_payload_hotels_item = cls(
            hotel_id=hotel_id,
            name=name,
            is_new=is_new,
        )


        account_units_added_payload_hotels_item.additional_properties = d
        return account_units_added_payload_hotels_item

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
