from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="CustomSchemaMappings")



@_attrs_define
class CustomSchemaMappings:
    """ Field-mapping table. Keys are the output field names emitted in the response payload; values are simple expressions
    referenced against the source `native` payload (dot paths, basic arithmetic, string concatenation). Min 1 entry, max
    50 entries. Each key must be <= 100 chars; each expression must be <= 500 chars and pass the safety check (no
    `eval`, no `function`, no `process`, etc.).

        Example:
            {'listing_id': 'propertyId', 'arrival': 'checkIn', 'departure': 'checkOut', 'guest_name':
                "primaryGuest.firstName + ' ' + primaryGuest.lastName", 'nightly_rate': 'financials.breakdown.basePrice /
                nights'}

     """

    additional_properties: dict[str, str] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        custom_schema_mappings = cls(
        )


        custom_schema_mappings.additional_properties = d
        return custom_schema_mappings

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> str:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: str) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
