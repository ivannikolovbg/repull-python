from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GetVrboListingTranslationsResponse200DataItemsItem")



@_attrs_define
class GetVrboListingTranslationsResponse200DataItemsItem:
    """ 
        Attributes:
            locale (str | Unset):  Example: fr-FR.
            headline (None | str | Unset):
            description (None | str | Unset):
     """

    locale: str | Unset = UNSET
    headline: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





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
        field_dict.update(self.additional_properties)
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


        get_vrbo_listing_translations_response_200_data_items_item = cls(
            locale=locale,
            headline=headline,
            description=description,
        )


        get_vrbo_listing_translations_response_200_data_items_item.additional_properties = d
        return get_vrbo_listing_translations_response_200_data_items_item

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
