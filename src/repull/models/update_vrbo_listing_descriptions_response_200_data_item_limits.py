from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_vrbo_listing_descriptions_response_200_data_item_limits_description_type_0 import UpdateVrboListingDescriptionsResponse200DataItemLimitsDescriptionType0
  from ..models.update_vrbo_listing_descriptions_response_200_data_item_limits_headline_type_0 import UpdateVrboListingDescriptionsResponse200DataItemLimitsHeadlineType0





T = TypeVar("T", bound="UpdateVrboListingDescriptionsResponse200DataItemLimits")



@_attrs_define
class UpdateVrboListingDescriptionsResponse200DataItemLimits:
    """ On the primary item: the lengths Vrbo allows.

        Attributes:
            headline (None | Unset | UpdateVrboListingDescriptionsResponse200DataItemLimitsHeadlineType0):
            description (None | Unset | UpdateVrboListingDescriptionsResponse200DataItemLimitsDescriptionType0):
     """

    headline: None | Unset | UpdateVrboListingDescriptionsResponse200DataItemLimitsHeadlineType0 = UNSET
    description: None | Unset | UpdateVrboListingDescriptionsResponse200DataItemLimitsDescriptionType0 = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_vrbo_listing_descriptions_response_200_data_item_limits_description_type_0 import UpdateVrboListingDescriptionsResponse200DataItemLimitsDescriptionType0
        from ..models.update_vrbo_listing_descriptions_response_200_data_item_limits_headline_type_0 import UpdateVrboListingDescriptionsResponse200DataItemLimitsHeadlineType0
        headline: dict[str, Any] | None | Unset
        if isinstance(self.headline, Unset):
            headline = UNSET
        elif isinstance(self.headline, UpdateVrboListingDescriptionsResponse200DataItemLimitsHeadlineType0):
            headline = self.headline.to_dict()
        else:
            headline = self.headline

        description: dict[str, Any] | None | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        elif isinstance(self.description, UpdateVrboListingDescriptionsResponse200DataItemLimitsDescriptionType0):
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
        from ..models.update_vrbo_listing_descriptions_response_200_data_item_limits_description_type_0 import UpdateVrboListingDescriptionsResponse200DataItemLimitsDescriptionType0
        from ..models.update_vrbo_listing_descriptions_response_200_data_item_limits_headline_type_0 import UpdateVrboListingDescriptionsResponse200DataItemLimitsHeadlineType0
        d = dict(src_dict)
        def _parse_headline(data: object) -> None | Unset | UpdateVrboListingDescriptionsResponse200DataItemLimitsHeadlineType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                headline_type_0 = UpdateVrboListingDescriptionsResponse200DataItemLimitsHeadlineType0.from_dict(data)



                return headline_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateVrboListingDescriptionsResponse200DataItemLimitsHeadlineType0, data)

        headline = _parse_headline(d.pop("headline", UNSET))


        def _parse_description(data: object) -> None | Unset | UpdateVrboListingDescriptionsResponse200DataItemLimitsDescriptionType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                description_type_0 = UpdateVrboListingDescriptionsResponse200DataItemLimitsDescriptionType0.from_dict(data)



                return description_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateVrboListingDescriptionsResponse200DataItemLimitsDescriptionType0, data)

        description = _parse_description(d.pop("description", UNSET))


        update_vrbo_listing_descriptions_response_200_data_item_limits = cls(
            headline=headline,
            description=description,
        )


        update_vrbo_listing_descriptions_response_200_data_item_limits.additional_properties = d
        return update_vrbo_listing_descriptions_response_200_data_item_limits

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
