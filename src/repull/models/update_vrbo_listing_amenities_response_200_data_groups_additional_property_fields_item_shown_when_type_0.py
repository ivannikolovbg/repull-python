from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UpdateVrboListingAmenitiesResponse200DataGroupsAdditionalPropertyFieldsItemShownWhenType0")



@_attrs_define
class UpdateVrboListingAmenitiesResponse200DataGroupsAdditionalPropertyFieldsItemShownWhenType0:
    """ The parent field and value this field is shown under.

        Attributes:
            id (str | Unset):
            value (str | Unset):
     """

    id: str | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        value = self.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        value = d.pop("value", UNSET)

        update_vrbo_listing_amenities_response_200_data_groups_additional_property_fields_item_shown_when_type_0 = cls(
            id=id,
            value=value,
        )


        update_vrbo_listing_amenities_response_200_data_groups_additional_property_fields_item_shown_when_type_0.additional_properties = d
        return update_vrbo_listing_amenities_response_200_data_groups_additional_property_fields_item_shown_when_type_0

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
