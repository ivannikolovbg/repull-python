from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UpdateVrboListingDescriptionBody")



@_attrs_define
class UpdateVrboListingDescriptionBody:
    """ 
        Attributes:
            headline (str | Unset):
            description (str | Unset):
     """

    headline: str | Unset = UNSET
    description: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        headline = self.headline

        description = self.description


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if headline is not UNSET:
            field_dict["headline"] = headline
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        headline = d.pop("headline", UNSET)

        description = d.pop("description", UNSET)

        update_vrbo_listing_description_body = cls(
            headline=headline,
            description=description,
        )

        return update_vrbo_listing_description_body

