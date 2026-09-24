from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.run_migration_import_response_202_data_queued_item import RunMigrationImportResponse202DataQueuedItem





T = TypeVar("T", bound="RunMigrationImportResponse202Data")



@_attrs_define
class RunMigrationImportResponse202Data:
    """ 
        Attributes:
            workspace_id (str | Unset):
            queued (list[RunMigrationImportResponse202DataQueuedItem] | Unset):
     """

    workspace_id: str | Unset = UNSET
    queued: list[RunMigrationImportResponse202DataQueuedItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.run_migration_import_response_202_data_queued_item import RunMigrationImportResponse202DataQueuedItem
        workspace_id = self.workspace_id

        queued: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.queued, Unset):
            queued = []
            for queued_item_data in self.queued:
                queued_item = queued_item_data.to_dict()
                queued.append(queued_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id
        if queued is not UNSET:
            field_dict["queued"] = queued

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_migration_import_response_202_data_queued_item import RunMigrationImportResponse202DataQueuedItem
        d = dict(src_dict)
        workspace_id = d.pop("workspaceId", UNSET)

        _queued = d.pop("queued", UNSET)
        queued: list[RunMigrationImportResponse202DataQueuedItem] | Unset = UNSET
        if _queued is not UNSET:
            queued = []
            for queued_item_data in _queued:
                queued_item = RunMigrationImportResponse202DataQueuedItem.from_dict(queued_item_data)



                queued.append(queued_item)


        run_migration_import_response_202_data = cls(
            workspace_id=workspace_id,
            queued=queued,
        )


        run_migration_import_response_202_data.additional_properties = d
        return run_migration_import_response_202_data

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
