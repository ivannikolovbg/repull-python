from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_vrbo_listing_details_response_200_data_interior_size import GetVrboListingDetailsResponse200DataInteriorSize
  from ..models.get_vrbo_listing_details_response_200_data_property_type_options_item import GetVrboListingDetailsResponse200DataPropertyTypeOptionsItem





T = TypeVar("T", bound="GetVrboListingDetailsResponse200Data")



@_attrs_define
class GetVrboListingDetailsResponse200Data:
    """ The section as Vrbo has it.

        Attributes:
            property_type (None | str | Unset):  Example: townhome.
            property_type_options (list[GetVrboListingDetailsResponse200DataPropertyTypeOptionsItem] | Unset):
            property_name (None | str | Unset):
            interior_size (GetVrboListingDetailsResponse200DataInteriorSize | Unset):
            seniors_only (bool | None | Unset):
            long_term_renters_welcome (bool | None | Unset):
     """

    property_type: None | str | Unset = UNSET
    property_type_options: list[GetVrboListingDetailsResponse200DataPropertyTypeOptionsItem] | Unset = UNSET
    property_name: None | str | Unset = UNSET
    interior_size: GetVrboListingDetailsResponse200DataInteriorSize | Unset = UNSET
    seniors_only: bool | None | Unset = UNSET
    long_term_renters_welcome: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_vrbo_listing_details_response_200_data_interior_size import GetVrboListingDetailsResponse200DataInteriorSize
        from ..models.get_vrbo_listing_details_response_200_data_property_type_options_item import GetVrboListingDetailsResponse200DataPropertyTypeOptionsItem
        property_type: None | str | Unset
        if isinstance(self.property_type, Unset):
            property_type = UNSET
        else:
            property_type = self.property_type

        property_type_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.property_type_options, Unset):
            property_type_options = []
            for property_type_options_item_data in self.property_type_options:
                property_type_options_item = property_type_options_item_data.to_dict()
                property_type_options.append(property_type_options_item)



        property_name: None | str | Unset
        if isinstance(self.property_name, Unset):
            property_name = UNSET
        else:
            property_name = self.property_name

        interior_size: dict[str, Any] | Unset = UNSET
        if not isinstance(self.interior_size, Unset):
            interior_size = self.interior_size.to_dict()

        seniors_only: bool | None | Unset
        if isinstance(self.seniors_only, Unset):
            seniors_only = UNSET
        else:
            seniors_only = self.seniors_only

        long_term_renters_welcome: bool | None | Unset
        if isinstance(self.long_term_renters_welcome, Unset):
            long_term_renters_welcome = UNSET
        else:
            long_term_renters_welcome = self.long_term_renters_welcome


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if property_type is not UNSET:
            field_dict["propertyType"] = property_type
        if property_type_options is not UNSET:
            field_dict["propertyTypeOptions"] = property_type_options
        if property_name is not UNSET:
            field_dict["propertyName"] = property_name
        if interior_size is not UNSET:
            field_dict["interiorSize"] = interior_size
        if seniors_only is not UNSET:
            field_dict["seniorsOnly"] = seniors_only
        if long_term_renters_welcome is not UNSET:
            field_dict["longTermRentersWelcome"] = long_term_renters_welcome

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_vrbo_listing_details_response_200_data_interior_size import GetVrboListingDetailsResponse200DataInteriorSize
        from ..models.get_vrbo_listing_details_response_200_data_property_type_options_item import GetVrboListingDetailsResponse200DataPropertyTypeOptionsItem
        d = dict(src_dict)
        def _parse_property_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        property_type = _parse_property_type(d.pop("propertyType", UNSET))


        _property_type_options = d.pop("propertyTypeOptions", UNSET)
        property_type_options: list[GetVrboListingDetailsResponse200DataPropertyTypeOptionsItem] | Unset = UNSET
        if _property_type_options is not UNSET:
            property_type_options = []
            for property_type_options_item_data in _property_type_options:
                property_type_options_item = GetVrboListingDetailsResponse200DataPropertyTypeOptionsItem.from_dict(property_type_options_item_data)



                property_type_options.append(property_type_options_item)


        def _parse_property_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        property_name = _parse_property_name(d.pop("propertyName", UNSET))


        _interior_size = d.pop("interiorSize", UNSET)
        interior_size: GetVrboListingDetailsResponse200DataInteriorSize | Unset
        if isinstance(_interior_size,  Unset):
            interior_size = UNSET
        else:
            interior_size = GetVrboListingDetailsResponse200DataInteriorSize.from_dict(_interior_size)




        def _parse_seniors_only(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        seniors_only = _parse_seniors_only(d.pop("seniorsOnly", UNSET))


        def _parse_long_term_renters_welcome(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        long_term_renters_welcome = _parse_long_term_renters_welcome(d.pop("longTermRentersWelcome", UNSET))


        get_vrbo_listing_details_response_200_data = cls(
            property_type=property_type,
            property_type_options=property_type_options,
            property_name=property_name,
            interior_size=interior_size,
            seniors_only=seniors_only,
            long_term_renters_welcome=long_term_renters_welcome,
        )


        get_vrbo_listing_details_response_200_data.additional_properties = d
        return get_vrbo_listing_details_response_200_data

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
