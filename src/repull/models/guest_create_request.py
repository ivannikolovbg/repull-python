from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GuestCreateRequest")



@_attrs_define
class GuestCreateRequest:
    """ 
        Attributes:
            first_name (str):  Example: Ada.
            last_name (str | Unset):  Example: Lovelace.
            email (str | Unset):  Example: ada@example.com.
            phone (str | Unset): E.164 preferred. Stored normalised. Example: +14035551234.
            language (str | Unset): BCP-47 tag. Example: en-GB.
            currency (str | Unset):  Example: GBP.
            is_business_traveler (bool | Unset):  Default: False.
     """

    first_name: str
    last_name: str | Unset = UNSET
    email: str | Unset = UNSET
    phone: str | Unset = UNSET
    language: str | Unset = UNSET
    currency: str | Unset = UNSET
    is_business_traveler: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        first_name = self.first_name

        last_name = self.last_name

        email = self.email

        phone = self.phone

        language = self.language

        currency = self.currency

        is_business_traveler = self.is_business_traveler


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "firstName": first_name,
        })
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if email is not UNSET:
            field_dict["email"] = email
        if phone is not UNSET:
            field_dict["phone"] = phone
        if language is not UNSET:
            field_dict["language"] = language
        if currency is not UNSET:
            field_dict["currency"] = currency
        if is_business_traveler is not UNSET:
            field_dict["isBusinessTraveler"] = is_business_traveler

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        first_name = d.pop("firstName")

        last_name = d.pop("lastName", UNSET)

        email = d.pop("email", UNSET)

        phone = d.pop("phone", UNSET)

        language = d.pop("language", UNSET)

        currency = d.pop("currency", UNSET)

        is_business_traveler = d.pop("isBusinessTraveler", UNSET)

        guest_create_request = cls(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            language=language,
            currency=currency,
            is_business_traveler=is_business_traveler,
        )


        guest_create_request.additional_properties = d
        return guest_create_request

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
