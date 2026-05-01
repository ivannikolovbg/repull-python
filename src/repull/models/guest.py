from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="Guest")



@_attrs_define
class Guest:
    """ 
        Attributes:
            id (int | Unset):
            first_name (str | Unset):  Example: Jane.
            last_name (str | Unset):  Example: Doe.
            email (str | Unset):
            phone (str | Unset):
            total_stays (int | Unset):
            total_revenue (float | Unset):
     """

    id: int | Unset = UNSET
    first_name: str | Unset = UNSET
    last_name: str | Unset = UNSET
    email: str | Unset = UNSET
    phone: str | Unset = UNSET
    total_stays: int | Unset = UNSET
    total_revenue: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        first_name = self.first_name

        last_name = self.last_name

        email = self.email

        phone = self.phone

        total_stays = self.total_stays

        total_revenue = self.total_revenue


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if email is not UNSET:
            field_dict["email"] = email
        if phone is not UNSET:
            field_dict["phone"] = phone
        if total_stays is not UNSET:
            field_dict["totalStays"] = total_stays
        if total_revenue is not UNSET:
            field_dict["totalRevenue"] = total_revenue

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        email = d.pop("email", UNSET)

        phone = d.pop("phone", UNSET)

        total_stays = d.pop("totalStays", UNSET)

        total_revenue = d.pop("totalRevenue", UNSET)

        guest = cls(
            id=id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            total_stays=total_stays,
            total_revenue=total_revenue,
        )


        guest.additional_properties = d
        return guest

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
