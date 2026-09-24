from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="MigrationImportPayloadResultsItem")



@_attrs_define
class MigrationImportPayloadResultsItem:
    """ 
        Attributes:
            entity_type (str | Unset):
            processed (int | Unset):
            errors (int | Unset):
     """

    entity_type: str | Unset = UNSET
    processed: int | Unset = UNSET
    errors: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        entity_type = self.entity_type

        processed = self.processed

        errors = self.errors


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if entity_type is not UNSET:
            field_dict["entityType"] = entity_type
        if processed is not UNSET:
            field_dict["processed"] = processed
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        entity_type = d.pop("entityType", UNSET)

        processed = d.pop("processed", UNSET)

        errors = d.pop("errors", UNSET)

        migration_import_payload_results_item = cls(
            entity_type=entity_type,
            processed=processed,
            errors=errors,
        )


        migration_import_payload_results_item.additional_properties = d
        return migration_import_payload_results_item

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
