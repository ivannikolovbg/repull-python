from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="DeleteMigrationResponse200Data")



@_attrs_define
class DeleteMigrationResponse200Data:
    """ 
        Attributes:
            workspace_id (str | Unset):
            deactivated (bool | Unset):
            deactivated_at (datetime.datetime | Unset):
     """

    workspace_id: str | Unset = UNSET
    deactivated: bool | Unset = UNSET
    deactivated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        workspace_id = self.workspace_id

        deactivated = self.deactivated

        deactivated_at: str | Unset = UNSET
        if not isinstance(self.deactivated_at, Unset):
            deactivated_at = self.deactivated_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id
        if deactivated is not UNSET:
            field_dict["deactivated"] = deactivated
        if deactivated_at is not UNSET:
            field_dict["deactivatedAt"] = deactivated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        workspace_id = d.pop("workspaceId", UNSET)

        deactivated = d.pop("deactivated", UNSET)

        _deactivated_at = d.pop("deactivatedAt", UNSET)
        deactivated_at: datetime.datetime | Unset
        if isinstance(_deactivated_at,  Unset):
            deactivated_at = UNSET
        else:
            deactivated_at = isoparse(_deactivated_at)




        delete_migration_response_200_data = cls(
            workspace_id=workspace_id,
            deactivated=deactivated,
            deactivated_at=deactivated_at,
        )


        delete_migration_response_200_data.additional_properties = d
        return delete_migration_response_200_data

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
