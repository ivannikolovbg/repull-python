from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="RunMigrationImportResponse202DataQueuedItem")



@_attrs_define
class RunMigrationImportResponse202DataQueuedItem:
    """ 
        Attributes:
            connection_id (str | Unset):
            provider (str | Unset):
            queued (bool | Unset):
            error (str | Unset):
     """

    connection_id: str | Unset = UNSET
    provider: str | Unset = UNSET
    queued: bool | Unset = UNSET
    error: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        connection_id = self.connection_id

        provider = self.provider

        queued = self.queued

        error = self.error


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if connection_id is not UNSET:
            field_dict["connectionId"] = connection_id
        if provider is not UNSET:
            field_dict["provider"] = provider
        if queued is not UNSET:
            field_dict["queued"] = queued
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connection_id = d.pop("connectionId", UNSET)

        provider = d.pop("provider", UNSET)

        queued = d.pop("queued", UNSET)

        error = d.pop("error", UNSET)

        run_migration_import_response_202_data_queued_item = cls(
            connection_id=connection_id,
            provider=provider,
            queued=queued,
            error=error,
        )


        run_migration_import_response_202_data_queued_item.additional_properties = d
        return run_migration_import_response_202_data_queued_item

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
