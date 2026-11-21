from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="UpdateVrboListingProtectionResponse200DataOptionsItem")



@_attrs_define
class UpdateVrboListingProtectionResponse200DataOptionsItem:
    """ 
        Attributes:
            id (str | Unset):
            selected (bool | None | Unset):
            name (None | str | Unset):
            limit (Any | Unset):
     """

    id: str | Unset = UNSET
    selected: bool | None | Unset = UNSET
    name: None | str | Unset = UNSET
    limit: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        selected: bool | None | Unset
        if isinstance(self.selected, Unset):
            selected = UNSET
        else:
            selected = self.selected

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        limit = self.limit


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if selected is not UNSET:
            field_dict["selected"] = selected
        if name is not UNSET:
            field_dict["name"] = name
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_selected(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        selected = _parse_selected(d.pop("selected", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        limit = d.pop("limit", UNSET)

        update_vrbo_listing_protection_response_200_data_options_item = cls(
            id=id,
            selected=selected,
            name=name,
            limit=limit,
        )


        update_vrbo_listing_protection_response_200_data_options_item.additional_properties = d
        return update_vrbo_listing_protection_response_200_data_options_item

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
