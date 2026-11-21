from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UpdateVrboListingAdditionalInfoBody")



@_attrs_define
class UpdateVrboListingAdditionalInfoBody:
    """ 
        Attributes:
            property_ (str | Unset):
            bedrooms (str | Unset):
            bathrooms (str | Unset):
     """

    property_: str | Unset = UNSET
    bedrooms: str | Unset = UNSET
    bathrooms: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        property_ = self.property_

        bedrooms = self.bedrooms

        bathrooms = self.bathrooms


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if property_ is not UNSET:
            field_dict["property"] = property_
        if bedrooms is not UNSET:
            field_dict["bedrooms"] = bedrooms
        if bathrooms is not UNSET:
            field_dict["bathrooms"] = bathrooms

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        property_ = d.pop("property", UNSET)

        bedrooms = d.pop("bedrooms", UNSET)

        bathrooms = d.pop("bathrooms", UNSET)

        update_vrbo_listing_additional_info_body = cls(
            property_=property_,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
        )

        return update_vrbo_listing_additional_info_body

