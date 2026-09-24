from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.migration_import_payload_status import MigrationImportPayloadStatus
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.migration_import_payload_results_item import MigrationImportPayloadResultsItem





T = TypeVar("T", bound="MigrationImportPayload")



@_attrs_define
class MigrationImportPayload:
    """ One import run into a migration workspace.

        Attributes:
            workspace_id (int | Unset):
            provider (str | Unset):  Example: guesty.
            connection_id (int | Unset):
            status (MigrationImportPayloadStatus | Unset):
            started_at (datetime.datetime | Unset):
            finished_at (datetime.datetime | Unset):
            entities (list[str] | Unset):
            results (list[MigrationImportPayloadResultsItem] | Unset):
            error (str | Unset): Present on `migration.failed`.
     """

    workspace_id: int | Unset = UNSET
    provider: str | Unset = UNSET
    connection_id: int | Unset = UNSET
    status: MigrationImportPayloadStatus | Unset = UNSET
    started_at: datetime.datetime | Unset = UNSET
    finished_at: datetime.datetime | Unset = UNSET
    entities: list[str] | Unset = UNSET
    results: list[MigrationImportPayloadResultsItem] | Unset = UNSET
    error: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.migration_import_payload_results_item import MigrationImportPayloadResultsItem
        workspace_id = self.workspace_id

        provider = self.provider

        connection_id = self.connection_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        started_at: str | Unset = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()

        finished_at: str | Unset = UNSET
        if not isinstance(self.finished_at, Unset):
            finished_at = self.finished_at.isoformat()

        entities: list[str] | Unset = UNSET
        if not isinstance(self.entities, Unset):
            entities = self.entities



        results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()
                results.append(results_item)



        error = self.error


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id
        if provider is not UNSET:
            field_dict["provider"] = provider
        if connection_id is not UNSET:
            field_dict["connectionId"] = connection_id
        if status is not UNSET:
            field_dict["status"] = status
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if finished_at is not UNSET:
            field_dict["finishedAt"] = finished_at
        if entities is not UNSET:
            field_dict["entities"] = entities
        if results is not UNSET:
            field_dict["results"] = results
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.migration_import_payload_results_item import MigrationImportPayloadResultsItem
        d = dict(src_dict)
        workspace_id = d.pop("workspaceId", UNSET)

        provider = d.pop("provider", UNSET)

        connection_id = d.pop("connectionId", UNSET)

        _status = d.pop("status", UNSET)
        status: MigrationImportPayloadStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = MigrationImportPayloadStatus(_status)




        _started_at = d.pop("startedAt", UNSET)
        started_at: datetime.datetime | Unset
        if isinstance(_started_at,  Unset):
            started_at = UNSET
        else:
            started_at = isoparse(_started_at)




        _finished_at = d.pop("finishedAt", UNSET)
        finished_at: datetime.datetime | Unset
        if isinstance(_finished_at,  Unset):
            finished_at = UNSET
        else:
            finished_at = isoparse(_finished_at)




        entities = cast(list[str], d.pop("entities", UNSET))


        _results = d.pop("results", UNSET)
        results: list[MigrationImportPayloadResultsItem] | Unset = UNSET
        if _results is not UNSET:
            results = []
            for results_item_data in _results:
                results_item = MigrationImportPayloadResultsItem.from_dict(results_item_data)



                results.append(results_item)


        error = d.pop("error", UNSET)

        migration_import_payload = cls(
            workspace_id=workspace_id,
            provider=provider,
            connection_id=connection_id,
            status=status,
            started_at=started_at,
            finished_at=finished_at,
            entities=entities,
            results=results,
            error=error,
        )


        migration_import_payload.additional_properties = d
        return migration_import_payload

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
