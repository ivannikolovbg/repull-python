from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="TiketSetupRequestContactsItem")



@_attrs_define
class TiketSetupRequestContactsItem:
    """ 
        Attributes:
            profile_type (str | Unset):
            name (str | Unset):
            position_id (int | Unset):
            phone (str | Unset):
            country_access_code (str | Unset):
            email (str | Unset):
     """

    profile_type: str | Unset = UNSET
    name: str | Unset = UNSET
    position_id: int | Unset = UNSET
    phone: str | Unset = UNSET
    country_access_code: str | Unset = UNSET
    email: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        profile_type = self.profile_type

        name = self.name

        position_id = self.position_id

        phone = self.phone

        country_access_code = self.country_access_code

        email = self.email


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if profile_type is not UNSET:
            field_dict["profile_type"] = profile_type
        if name is not UNSET:
            field_dict["name"] = name
        if position_id is not UNSET:
            field_dict["position_id"] = position_id
        if phone is not UNSET:
            field_dict["phone"] = phone
        if country_access_code is not UNSET:
            field_dict["country_access_code"] = country_access_code
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        profile_type = d.pop("profile_type", UNSET)

        name = d.pop("name", UNSET)

        position_id = d.pop("position_id", UNSET)

        phone = d.pop("phone", UNSET)

        country_access_code = d.pop("country_access_code", UNSET)

        email = d.pop("email", UNSET)

        tiket_setup_request_contacts_item = cls(
            profile_type=profile_type,
            name=name,
            position_id=position_id,
            phone=phone,
            country_access_code=country_access_code,
            email=email,
        )


        tiket_setup_request_contacts_item.additional_properties = d
        return tiket_setup_request_contacts_item

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
