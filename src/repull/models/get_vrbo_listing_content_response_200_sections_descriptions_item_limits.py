from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_vrbo_listing_content_response_200_sections_descriptions_item_limits_description_type_0 import GetVrboListingContentResponse200SectionsDescriptionsItemLimitsDescriptionType0
  from ..models.get_vrbo_listing_content_response_200_sections_descriptions_item_limits_headline_type_0 import GetVrboListingContentResponse200SectionsDescriptionsItemLimitsHeadlineType0





T = TypeVar("T", bound="GetVrboListingContentResponse200SectionsDescriptionsItemLimits")



@_attrs_define
class GetVrboListingContentResponse200SectionsDescriptionsItemLimits:
    """ On the primary item: the lengths Vrbo allows.

        Attributes:
            headline (GetVrboListingContentResponse200SectionsDescriptionsItemLimitsHeadlineType0 | None | Unset):
            description (GetVrboListingContentResponse200SectionsDescriptionsItemLimitsDescriptionType0 | None | Unset):
     """

    headline: GetVrboListingContentResponse200SectionsDescriptionsItemLimitsHeadlineType0 | None | Unset = UNSET
    description: GetVrboListingContentResponse200SectionsDescriptionsItemLimitsDescriptionType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_vrbo_listing_content_response_200_sections_descriptions_item_limits_description_type_0 import GetVrboListingContentResponse200SectionsDescriptionsItemLimitsDescriptionType0
        from ..models.get_vrbo_listing_content_response_200_sections_descriptions_item_limits_headline_type_0 import GetVrboListingContentResponse200SectionsDescriptionsItemLimitsHeadlineType0
        headline: dict[str, Any] | None | Unset
        if isinstance(self.headline, Unset):
            headline = UNSET
        elif isinstance(self.headline, GetVrboListingContentResponse200SectionsDescriptionsItemLimitsHeadlineType0):
            headline = self.headline.to_dict()
        else:
            headline = self.headline

        description: dict[str, Any] | None | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        elif isinstance(self.description, GetVrboListingContentResponse200SectionsDescriptionsItemLimitsDescriptionType0):
            description = self.description.to_dict()
        else:
            description = self.description


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if headline is not UNSET:
            field_dict["headline"] = headline
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_vrbo_listing_content_response_200_sections_descriptions_item_limits_description_type_0 import GetVrboListingContentResponse200SectionsDescriptionsItemLimitsDescriptionType0
        from ..models.get_vrbo_listing_content_response_200_sections_descriptions_item_limits_headline_type_0 import GetVrboListingContentResponse200SectionsDescriptionsItemLimitsHeadlineType0
        d = dict(src_dict)
        def _parse_headline(data: object) -> GetVrboListingContentResponse200SectionsDescriptionsItemLimitsHeadlineType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                headline_type_0 = GetVrboListingContentResponse200SectionsDescriptionsItemLimitsHeadlineType0.from_dict(data)



                return headline_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetVrboListingContentResponse200SectionsDescriptionsItemLimitsHeadlineType0 | None | Unset, data)

        headline = _parse_headline(d.pop("headline", UNSET))


        def _parse_description(data: object) -> GetVrboListingContentResponse200SectionsDescriptionsItemLimitsDescriptionType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                description_type_0 = GetVrboListingContentResponse200SectionsDescriptionsItemLimitsDescriptionType0.from_dict(data)



                return description_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetVrboListingContentResponse200SectionsDescriptionsItemLimitsDescriptionType0 | None | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        get_vrbo_listing_content_response_200_sections_descriptions_item_limits = cls(
            headline=headline,
            description=description,
        )


        get_vrbo_listing_content_response_200_sections_descriptions_item_limits.additional_properties = d
        return get_vrbo_listing_content_response_200_sections_descriptions_item_limits

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
