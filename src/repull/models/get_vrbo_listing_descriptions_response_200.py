from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_vrbo_listing_descriptions_response_200_data_freshness import GetVrboListingDescriptionsResponse200DataFreshness
  from ..models.get_vrbo_listing_descriptions_response_200_data_item import GetVrboListingDescriptionsResponse200DataItem
  from ..models.get_vrbo_listing_descriptions_response_200_languages_item import GetVrboListingDescriptionsResponse200LanguagesItem





T = TypeVar("T", bound="GetVrboListingDescriptionsResponse200")



@_attrs_define
class GetVrboListingDescriptionsResponse200:
    """ 
        Attributes:
            data (list[GetVrboListingDescriptionsResponse200DataItem]): The section as Vrbo has it.
            data_freshness (GetVrboListingDescriptionsResponse200DataFreshness):
            vrbo_listing_number (str): The Vrbo listing number this is about.
            languages (list[GetVrboListingDescriptionsResponse200LanguagesItem] | Unset): The languages a translation can be
                written in (`value` is the `locale`).
     """

    data: list[GetVrboListingDescriptionsResponse200DataItem]
    data_freshness: GetVrboListingDescriptionsResponse200DataFreshness
    vrbo_listing_number: str
    languages: list[GetVrboListingDescriptionsResponse200LanguagesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_vrbo_listing_descriptions_response_200_data_freshness import GetVrboListingDescriptionsResponse200DataFreshness
        from ..models.get_vrbo_listing_descriptions_response_200_data_item import GetVrboListingDescriptionsResponse200DataItem
        from ..models.get_vrbo_listing_descriptions_response_200_languages_item import GetVrboListingDescriptionsResponse200LanguagesItem
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)



        data_freshness = self.data_freshness.to_dict()

        vrbo_listing_number = self.vrbo_listing_number

        languages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.languages, Unset):
            languages = []
            for languages_item_data in self.languages:
                languages_item = languages_item_data.to_dict()
                languages.append(languages_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "data": data,
            "dataFreshness": data_freshness,
            "vrboListingNumber": vrbo_listing_number,
        })
        if languages is not UNSET:
            field_dict["languages"] = languages

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_vrbo_listing_descriptions_response_200_data_freshness import GetVrboListingDescriptionsResponse200DataFreshness
        from ..models.get_vrbo_listing_descriptions_response_200_data_item import GetVrboListingDescriptionsResponse200DataItem
        from ..models.get_vrbo_listing_descriptions_response_200_languages_item import GetVrboListingDescriptionsResponse200LanguagesItem
        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in (_data):
            data_item = GetVrboListingDescriptionsResponse200DataItem.from_dict(data_item_data)



            data.append(data_item)


        data_freshness = GetVrboListingDescriptionsResponse200DataFreshness.from_dict(d.pop("dataFreshness"))




        vrbo_listing_number = d.pop("vrboListingNumber")

        _languages = d.pop("languages", UNSET)
        languages: list[GetVrboListingDescriptionsResponse200LanguagesItem] | Unset = UNSET
        if _languages is not UNSET:
            languages = []
            for languages_item_data in _languages:
                languages_item = GetVrboListingDescriptionsResponse200LanguagesItem.from_dict(languages_item_data)



                languages.append(languages_item)


        get_vrbo_listing_descriptions_response_200 = cls(
            data=data,
            data_freshness=data_freshness,
            vrbo_listing_number=vrbo_listing_number,
            languages=languages,
        )


        get_vrbo_listing_descriptions_response_200.additional_properties = d
        return get_vrbo_listing_descriptions_response_200

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
