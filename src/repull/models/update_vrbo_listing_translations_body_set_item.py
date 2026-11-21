from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="UpdateVrboListingTranslationsBodySetItem")



@_attrs_define
class UpdateVrboListingTranslationsBodySetItem:
    """ 
        Attributes:
            locale (str):
            headline (None | str | Unset):
            description (None | str | Unset):
     """

    locale: str
    headline: None | str | Unset = UNSET
    description: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        locale = self.locale

        headline: None | str | Unset
        if isinstance(self.headline, Unset):
            headline = UNSET
        else:
            headline = self.headline

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "locale": locale,
        })
        if headline is not UNSET:
            field_dict["headline"] = headline
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        locale = d.pop("locale")

        def _parse_headline(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        headline = _parse_headline(d.pop("headline", UNSET))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        update_vrbo_listing_translations_body_set_item = cls(
            locale=locale,
            headline=headline,
            description=description,
        )

        return update_vrbo_listing_translations_body_set_item

