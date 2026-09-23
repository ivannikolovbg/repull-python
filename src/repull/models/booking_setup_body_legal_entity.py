from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="BookingSetupBodyLegalEntity")



@_attrs_define
class BookingSetupBodyLegalEntity:
    """ Used by `create-property` ONLY when this workspace has no legal entity yet — one is registered with Booking.com from
    these details and used for the property. Ignored when the workspace already has one, so a second is never
    registered.

        Attributes:
            company_name (str):
            legal_contact_name (str):
            legal_contact_email (str):
            country (str | Unset):
            city (str | Unset):
     """

    company_name: str
    legal_contact_name: str
    legal_contact_email: str
    country: str | Unset = UNSET
    city: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        company_name = self.company_name

        legal_contact_name = self.legal_contact_name

        legal_contact_email = self.legal_contact_email

        country = self.country

        city = self.city


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "company_name": company_name,
            "legal_contact_name": legal_contact_name,
            "legal_contact_email": legal_contact_email,
        })
        if country is not UNSET:
            field_dict["country"] = country
        if city is not UNSET:
            field_dict["city"] = city

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        company_name = d.pop("company_name")

        legal_contact_name = d.pop("legal_contact_name")

        legal_contact_email = d.pop("legal_contact_email")

        country = d.pop("country", UNSET)

        city = d.pop("city", UNSET)

        booking_setup_body_legal_entity = cls(
            company_name=company_name,
            legal_contact_name=legal_contact_name,
            legal_contact_email=legal_contact_email,
            country=country,
            city=city,
        )


        booking_setup_body_legal_entity.additional_properties = d
        return booking_setup_body_legal_entity

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
