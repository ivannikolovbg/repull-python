from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_vrbo_listing_content_response_200_sections_additional_info_limits import GetVrboListingContentResponse200SectionsAdditionalInfoLimits





T = TypeVar("T", bound="GetVrboListingContentResponse200SectionsAdditionalInfo")



@_attrs_define
class GetVrboListingContentResponse200SectionsAdditionalInfo:
    """ 
        Attributes:
            property_ (None | str | Unset):
            bedrooms (None | str | Unset):
            bathrooms (None | str | Unset):
            limits (GetVrboListingContentResponse200SectionsAdditionalInfoLimits | Unset):
     """

    property_: None | str | Unset = UNSET
    bedrooms: None | str | Unset = UNSET
    bathrooms: None | str | Unset = UNSET
    limits: GetVrboListingContentResponse200SectionsAdditionalInfoLimits | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_vrbo_listing_content_response_200_sections_additional_info_limits import GetVrboListingContentResponse200SectionsAdditionalInfoLimits
        property_: None | str | Unset
        if isinstance(self.property_, Unset):
            property_ = UNSET
        else:
            property_ = self.property_

        bedrooms: None | str | Unset
        if isinstance(self.bedrooms, Unset):
            bedrooms = UNSET
        else:
            bedrooms = self.bedrooms

        bathrooms: None | str | Unset
        if isinstance(self.bathrooms, Unset):
            bathrooms = UNSET
        else:
            bathrooms = self.bathrooms

        limits: dict[str, Any] | Unset = UNSET
        if not isinstance(self.limits, Unset):
            limits = self.limits.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if property_ is not UNSET:
            field_dict["property"] = property_
        if bedrooms is not UNSET:
            field_dict["bedrooms"] = bedrooms
        if bathrooms is not UNSET:
            field_dict["bathrooms"] = bathrooms
        if limits is not UNSET:
            field_dict["limits"] = limits

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_vrbo_listing_content_response_200_sections_additional_info_limits import GetVrboListingContentResponse200SectionsAdditionalInfoLimits
        d = dict(src_dict)
        def _parse_property_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        property_ = _parse_property_(d.pop("property", UNSET))


        def _parse_bedrooms(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bedrooms = _parse_bedrooms(d.pop("bedrooms", UNSET))


        def _parse_bathrooms(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bathrooms = _parse_bathrooms(d.pop("bathrooms", UNSET))


        _limits = d.pop("limits", UNSET)
        limits: GetVrboListingContentResponse200SectionsAdditionalInfoLimits | Unset
        if isinstance(_limits,  Unset):
            limits = UNSET
        else:
            limits = GetVrboListingContentResponse200SectionsAdditionalInfoLimits.from_dict(_limits)




        get_vrbo_listing_content_response_200_sections_additional_info = cls(
            property_=property_,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            limits=limits,
        )


        get_vrbo_listing_content_response_200_sections_additional_info.additional_properties = d
        return get_vrbo_listing_content_response_200_sections_additional_info

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
