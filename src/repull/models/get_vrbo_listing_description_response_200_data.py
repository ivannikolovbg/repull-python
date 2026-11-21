from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_vrbo_listing_description_response_200_data_limits import GetVrboListingDescriptionResponse200DataLimits





T = TypeVar("T", bound="GetVrboListingDescriptionResponse200Data")



@_attrs_define
class GetVrboListingDescriptionResponse200Data:
    """ The section as Vrbo has it now.

        Attributes:
            headline (None | str | Unset):
            description (None | str | Unset):
            limits (GetVrboListingDescriptionResponse200DataLimits | Unset):
     """

    headline: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    limits: GetVrboListingDescriptionResponse200DataLimits | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_vrbo_listing_description_response_200_data_limits import GetVrboListingDescriptionResponse200DataLimits
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

        limits: dict[str, Any] | Unset = UNSET
        if not isinstance(self.limits, Unset):
            limits = self.limits.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if headline is not UNSET:
            field_dict["headline"] = headline
        if description is not UNSET:
            field_dict["description"] = description
        if limits is not UNSET:
            field_dict["limits"] = limits

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_vrbo_listing_description_response_200_data_limits import GetVrboListingDescriptionResponse200DataLimits
        d = dict(src_dict)
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


        _limits = d.pop("limits", UNSET)
        limits: GetVrboListingDescriptionResponse200DataLimits | Unset
        if isinstance(_limits,  Unset):
            limits = UNSET
        else:
            limits = GetVrboListingDescriptionResponse200DataLimits.from_dict(_limits)




        get_vrbo_listing_description_response_200_data = cls(
            headline=headline,
            description=description,
            limits=limits,
        )


        get_vrbo_listing_description_response_200_data.additional_properties = d
        return get_vrbo_listing_description_response_200_data

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
