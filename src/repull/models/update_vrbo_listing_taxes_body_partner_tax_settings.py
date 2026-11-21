from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="UpdateVrboListingTaxesBodyPartnerTaxSettings")



@_attrs_define
class UpdateVrboListingTaxesBodyPartnerTaxSettings:
    """ 
        Attributes:
            category (str):
            attributes (list[Any] | Unset):
     """

    category: str
    attributes: list[Any] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        category = self.category

        attributes: list[Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "category": category,
        })
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category = d.pop("category")

        attributes = cast(list[Any], d.pop("attributes", UNSET))


        update_vrbo_listing_taxes_body_partner_tax_settings = cls(
            category=category,
            attributes=attributes,
        )


        update_vrbo_listing_taxes_body_partner_tax_settings.additional_properties = d
        return update_vrbo_listing_taxes_body_partner_tax_settings

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
