from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_vrbo_listing_content_response_200_sections_amenities_groups_additional_property_fields_item import GetVrboListingContentResponse200SectionsAmenitiesGroupsAdditionalPropertyFieldsItem





T = TypeVar("T", bound="GetVrboListingContentResponse200SectionsAmenitiesGroupsAdditionalProperty")



@_attrs_define
class GetVrboListingContentResponse200SectionsAmenitiesGroupsAdditionalProperty:
    """ 
        Attributes:
            group_id (str | Unset):
            fields (list[GetVrboListingContentResponse200SectionsAmenitiesGroupsAdditionalPropertyFieldsItem] | Unset):
     """

    group_id: str | Unset = UNSET
    fields: list[GetVrboListingContentResponse200SectionsAmenitiesGroupsAdditionalPropertyFieldsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_vrbo_listing_content_response_200_sections_amenities_groups_additional_property_fields_item import GetVrboListingContentResponse200SectionsAmenitiesGroupsAdditionalPropertyFieldsItem
        group_id = self.group_id

        fields: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()
                fields.append(fields_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_vrbo_listing_content_response_200_sections_amenities_groups_additional_property_fields_item import GetVrboListingContentResponse200SectionsAmenitiesGroupsAdditionalPropertyFieldsItem
        d = dict(src_dict)
        group_id = d.pop("groupId", UNSET)

        _fields = d.pop("fields", UNSET)
        fields: list[GetVrboListingContentResponse200SectionsAmenitiesGroupsAdditionalPropertyFieldsItem] | Unset = UNSET
        if _fields is not UNSET:
            fields = []
            for fields_item_data in _fields:
                fields_item = GetVrboListingContentResponse200SectionsAmenitiesGroupsAdditionalPropertyFieldsItem.from_dict(fields_item_data)



                fields.append(fields_item)


        get_vrbo_listing_content_response_200_sections_amenities_groups_additional_property = cls(
            group_id=group_id,
            fields=fields,
        )


        get_vrbo_listing_content_response_200_sections_amenities_groups_additional_property.additional_properties = d
        return get_vrbo_listing_content_response_200_sections_amenities_groups_additional_property

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
