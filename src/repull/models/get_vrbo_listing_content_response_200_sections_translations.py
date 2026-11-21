from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_vrbo_listing_content_response_200_sections_translations_items_item import GetVrboListingContentResponse200SectionsTranslationsItemsItem
  from ..models.get_vrbo_listing_content_response_200_sections_translations_languages_item import GetVrboListingContentResponse200SectionsTranslationsLanguagesItem





T = TypeVar("T", bound="GetVrboListingContentResponse200SectionsTranslations")



@_attrs_define
class GetVrboListingContentResponse200SectionsTranslations:
    """ 
        Attributes:
            items (list[GetVrboListingContentResponse200SectionsTranslationsItemsItem] | Unset):
            languages (list[GetVrboListingContentResponse200SectionsTranslationsLanguagesItem] | Unset):
     """

    items: list[GetVrboListingContentResponse200SectionsTranslationsItemsItem] | Unset = UNSET
    languages: list[GetVrboListingContentResponse200SectionsTranslationsLanguagesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_vrbo_listing_content_response_200_sections_translations_items_item import GetVrboListingContentResponse200SectionsTranslationsItemsItem
        from ..models.get_vrbo_listing_content_response_200_sections_translations_languages_item import GetVrboListingContentResponse200SectionsTranslationsLanguagesItem
        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)



        languages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.languages, Unset):
            languages = []
            for languages_item_data in self.languages:
                languages_item = languages_item_data.to_dict()
                languages.append(languages_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if items is not UNSET:
            field_dict["items"] = items
        if languages is not UNSET:
            field_dict["languages"] = languages

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_vrbo_listing_content_response_200_sections_translations_items_item import GetVrboListingContentResponse200SectionsTranslationsItemsItem
        from ..models.get_vrbo_listing_content_response_200_sections_translations_languages_item import GetVrboListingContentResponse200SectionsTranslationsLanguagesItem
        d = dict(src_dict)
        _items = d.pop("items", UNSET)
        items: list[GetVrboListingContentResponse200SectionsTranslationsItemsItem] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = GetVrboListingContentResponse200SectionsTranslationsItemsItem.from_dict(items_item_data)



                items.append(items_item)


        _languages = d.pop("languages", UNSET)
        languages: list[GetVrboListingContentResponse200SectionsTranslationsLanguagesItem] | Unset = UNSET
        if _languages is not UNSET:
            languages = []
            for languages_item_data in _languages:
                languages_item = GetVrboListingContentResponse200SectionsTranslationsLanguagesItem.from_dict(languages_item_data)



                languages.append(languages_item)


        get_vrbo_listing_content_response_200_sections_translations = cls(
            items=items,
            languages=languages,
        )


        get_vrbo_listing_content_response_200_sections_translations.additional_properties = d
        return get_vrbo_listing_content_response_200_sections_translations

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
