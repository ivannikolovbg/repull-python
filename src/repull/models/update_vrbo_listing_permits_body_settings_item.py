from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="UpdateVrboListingPermitsBodySettingsItem")



@_attrs_define
class UpdateVrboListingPermitsBodySettingsItem:
    """ 
        Attributes:
            name (str): A `fields[].name` from the read (they differ per jurisdiction).
            value (bool | float | None | str):
     """

    name: str
    value: bool | float | None | str





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        value: bool | float | None | str
        value = self.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "name": name,
            "value": value,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_value(data: object) -> bool | float | None | str:
            if data is None:
                return data
            return cast(bool | float | None | str, data)

        value = _parse_value(d.pop("value"))


        update_vrbo_listing_permits_body_settings_item = cls(
            name=name,
            value=value,
        )

        return update_vrbo_listing_permits_body_settings_item

