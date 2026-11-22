from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_vrbo_listing_settings_response_200_data_type_2_fields_item import GetVrboListingSettingsResponse200DataType2FieldsItem





T = TypeVar("T", bound="GetVrboListingSettingsResponse200DataType2")



@_attrs_define
class GetVrboListingSettingsResponse200DataType2:
    """ 
        Attributes:
            status (None | str | Unset):
            fields (list[GetVrboListingSettingsResponse200DataType2FieldsItem] | Unset):
     """

    status: None | str | Unset = UNSET
    fields: list[GetVrboListingSettingsResponse200DataType2FieldsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_vrbo_listing_settings_response_200_data_type_2_fields_item import GetVrboListingSettingsResponse200DataType2FieldsItem
        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

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
        if status is not UNSET:
            field_dict["status"] = status
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_vrbo_listing_settings_response_200_data_type_2_fields_item import GetVrboListingSettingsResponse200DataType2FieldsItem
        d = dict(src_dict)
        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        _fields = d.pop("fields", UNSET)
        fields: list[GetVrboListingSettingsResponse200DataType2FieldsItem] | Unset = UNSET
        if _fields is not UNSET:
            fields = []
            for fields_item_data in _fields:
                fields_item = GetVrboListingSettingsResponse200DataType2FieldsItem.from_dict(fields_item_data)



                fields.append(fields_item)


        get_vrbo_listing_settings_response_200_data_type_2 = cls(
            status=status,
            fields=fields,
        )


        get_vrbo_listing_settings_response_200_data_type_2.additional_properties = d
        return get_vrbo_listing_settings_response_200_data_type_2

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
