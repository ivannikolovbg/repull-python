from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_vrbo_listing_permits_response_200_data_fields_item import GetVrboListingPermitsResponse200DataFieldsItem





T = TypeVar("T", bound="GetVrboListingPermitsResponse200Data")



@_attrs_define
class GetVrboListingPermitsResponse200Data:
    """ The section as Vrbo has it.

        Attributes:
            status (None | str | Unset):
            fields (list[GetVrboListingPermitsResponse200DataFieldsItem] | Unset):
     """

    status: None | str | Unset = UNSET
    fields: list[GetVrboListingPermitsResponse200DataFieldsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_vrbo_listing_permits_response_200_data_fields_item import GetVrboListingPermitsResponse200DataFieldsItem
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
        from ..models.get_vrbo_listing_permits_response_200_data_fields_item import GetVrboListingPermitsResponse200DataFieldsItem
        d = dict(src_dict)
        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        _fields = d.pop("fields", UNSET)
        fields: list[GetVrboListingPermitsResponse200DataFieldsItem] | Unset = UNSET
        if _fields is not UNSET:
            fields = []
            for fields_item_data in _fields:
                fields_item = GetVrboListingPermitsResponse200DataFieldsItem.from_dict(fields_item_data)



                fields.append(fields_item)


        get_vrbo_listing_permits_response_200_data = cls(
            status=status,
            fields=fields,
        )


        get_vrbo_listing_permits_response_200_data.additional_properties = d
        return get_vrbo_listing_permits_response_200_data

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
