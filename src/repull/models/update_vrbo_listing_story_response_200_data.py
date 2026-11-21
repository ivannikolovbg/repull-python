from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_vrbo_listing_story_response_200_data_limits import UpdateVrboListingStoryResponse200DataLimits





T = TypeVar("T", bound="UpdateVrboListingStoryResponse200Data")



@_attrs_define
class UpdateVrboListingStoryResponse200Data:
    """ What Vrbo has stored for the section, read back after the write.

        Attributes:
            about_you (None | str | Unset):
            why_this_property (None | str | Unset):
            unique_benefits (None | str | Unset):
            limits (UpdateVrboListingStoryResponse200DataLimits | Unset):
     """

    about_you: None | str | Unset = UNSET
    why_this_property: None | str | Unset = UNSET
    unique_benefits: None | str | Unset = UNSET
    limits: UpdateVrboListingStoryResponse200DataLimits | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_vrbo_listing_story_response_200_data_limits import UpdateVrboListingStoryResponse200DataLimits
        about_you: None | str | Unset
        if isinstance(self.about_you, Unset):
            about_you = UNSET
        else:
            about_you = self.about_you

        why_this_property: None | str | Unset
        if isinstance(self.why_this_property, Unset):
            why_this_property = UNSET
        else:
            why_this_property = self.why_this_property

        unique_benefits: None | str | Unset
        if isinstance(self.unique_benefits, Unset):
            unique_benefits = UNSET
        else:
            unique_benefits = self.unique_benefits

        limits: dict[str, Any] | Unset = UNSET
        if not isinstance(self.limits, Unset):
            limits = self.limits.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if about_you is not UNSET:
            field_dict["aboutYou"] = about_you
        if why_this_property is not UNSET:
            field_dict["whyThisProperty"] = why_this_property
        if unique_benefits is not UNSET:
            field_dict["uniqueBenefits"] = unique_benefits
        if limits is not UNSET:
            field_dict["limits"] = limits

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_vrbo_listing_story_response_200_data_limits import UpdateVrboListingStoryResponse200DataLimits
        d = dict(src_dict)
        def _parse_about_you(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        about_you = _parse_about_you(d.pop("aboutYou", UNSET))


        def _parse_why_this_property(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        why_this_property = _parse_why_this_property(d.pop("whyThisProperty", UNSET))


        def _parse_unique_benefits(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unique_benefits = _parse_unique_benefits(d.pop("uniqueBenefits", UNSET))


        _limits = d.pop("limits", UNSET)
        limits: UpdateVrboListingStoryResponse200DataLimits | Unset
        if isinstance(_limits,  Unset):
            limits = UNSET
        else:
            limits = UpdateVrboListingStoryResponse200DataLimits.from_dict(_limits)




        update_vrbo_listing_story_response_200_data = cls(
            about_you=about_you,
            why_this_property=why_this_property,
            unique_benefits=unique_benefits,
            limits=limits,
        )


        update_vrbo_listing_story_response_200_data.additional_properties = d
        return update_vrbo_listing_story_response_200_data

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
