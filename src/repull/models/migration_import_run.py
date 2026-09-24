from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.migration_import_run_status import MigrationImportRunStatus
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.migration_import_run_results_type_0_item import MigrationImportRunResultsType0Item





T = TypeVar("T", bound="MigrationImportRun")



@_attrs_define
class MigrationImportRun:
    """ The last import run on a connection.

        Attributes:
            status (MigrationImportRunStatus | Unset):
            started_at (datetime.datetime | None | Unset):
            finished_at (datetime.datetime | None | Unset):
            entities (list[str] | None | Unset):
            results (list[MigrationImportRunResultsType0Item] | None | Unset):
            error (None | str | Unset):
     """

    status: MigrationImportRunStatus | Unset = UNSET
    started_at: datetime.datetime | None | Unset = UNSET
    finished_at: datetime.datetime | None | Unset = UNSET
    entities: list[str] | None | Unset = UNSET
    results: list[MigrationImportRunResultsType0Item] | None | Unset = UNSET
    error: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.migration_import_run_results_type_0_item import MigrationImportRunResultsType0Item
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        started_at: None | str | Unset
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        elif isinstance(self.started_at, datetime.datetime):
            started_at = self.started_at.isoformat()
        else:
            started_at = self.started_at

        finished_at: None | str | Unset
        if isinstance(self.finished_at, Unset):
            finished_at = UNSET
        elif isinstance(self.finished_at, datetime.datetime):
            finished_at = self.finished_at.isoformat()
        else:
            finished_at = self.finished_at

        entities: list[str] | None | Unset
        if isinstance(self.entities, Unset):
            entities = UNSET
        elif isinstance(self.entities, list):
            entities = self.entities


        else:
            entities = self.entities

        results: list[dict[str, Any]] | None | Unset
        if isinstance(self.results, Unset):
            results = UNSET
        elif isinstance(self.results, list):
            results = []
            for results_type_0_item_data in self.results:
                results_type_0_item = results_type_0_item_data.to_dict()
                results.append(results_type_0_item)


        else:
            results = self.results

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
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
        from ..models.migration_import_run_results_type_0_item import MigrationImportRunResultsType0Item
        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: MigrationImportRunStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = MigrationImportRunStatus(_status)




        def _parse_started_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                started_at_type_0 = isoparse(data)



                return started_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        started_at = _parse_started_at(d.pop("startedAt", UNSET))


        def _parse_finished_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                finished_at_type_0 = isoparse(data)



                return finished_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        finished_at = _parse_finished_at(d.pop("finishedAt", UNSET))


        def _parse_entities(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                entities_type_0 = cast(list[str], data)

                return entities_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        entities = _parse_entities(d.pop("entities", UNSET))


        def _parse_results(data: object) -> list[MigrationImportRunResultsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                results_type_0 = []
                _results_type_0 = data
                for results_type_0_item_data in (_results_type_0):
                    results_type_0_item = MigrationImportRunResultsType0Item.from_dict(results_type_0_item_data)



                    results_type_0.append(results_type_0_item)

                return results_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MigrationImportRunResultsType0Item] | None | Unset, data)

        results = _parse_results(d.pop("results", UNSET))


        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))


        migration_import_run = cls(
            status=status,
            started_at=started_at,
            finished_at=finished_at,
            entities=entities,
            results=results,
            error=error,
        )


        migration_import_run.additional_properties = d
        return migration_import_run

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
