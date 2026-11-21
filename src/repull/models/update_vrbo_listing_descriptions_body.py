from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UpdateVrboListingDescriptionsBody")



@_attrs_define
class UpdateVrboListingDescriptionsBody:
    """ 
        Attributes:
            locale (str | Unset): Leave out for the listing's own language. A language code (one of `languages` in the read)
                writes that language's hand-written translation, which replaces Vrbo's automatic one. Example: fr-FR.
            headline (str | Unset):
            description (str | Unset):
     """

    locale: str | Unset = UNSET
    headline: str | Unset = UNSET
    description: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        locale = self.locale

        headline = self.headline

        description = self.description


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if locale is not UNSET:
            field_dict["locale"] = locale
        if headline is not UNSET:
            field_dict["headline"] = headline
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        locale = d.pop("locale", UNSET)

        headline = d.pop("headline", UNSET)

        description = d.pop("description", UNSET)

        update_vrbo_listing_descriptions_body = cls(
            locale=locale,
            headline=headline,
            description=description,
        )

        return update_vrbo_listing_descriptions_body

