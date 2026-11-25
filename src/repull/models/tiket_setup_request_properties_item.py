from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="TiketSetupRequestPropertiesItem")



@_attrs_define
class TiketSetupRequestPropertiesItem:
    """ 
        Attributes:
            name (str | Unset):
            hotel_id (str | Unset):
            email (str | Unset):
            address (str | Unset):
     """

    name: str | Unset = UNSET
    hotel_id: str | Unset = UNSET
    email: str | Unset = UNSET
    address: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        hotel_id = self.hotel_id

        email = self.email

        address = self.address


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if hotel_id is not UNSET:
            field_dict["hotel_id"] = hotel_id
        if email is not UNSET:
            field_dict["email"] = email
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        hotel_id = d.pop("hotel_id", UNSET)

        email = d.pop("email", UNSET)

        address = d.pop("address", UNSET)

        tiket_setup_request_properties_item = cls(
            name=name,
            hotel_id=hotel_id,
            email=email,
            address=address,
        )


        tiket_setup_request_properties_item.additional_properties = d
        return tiket_setup_request_properties_item

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
