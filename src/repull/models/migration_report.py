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

if TYPE_CHECKING:
  from ..models.migration_report_capabilities import MigrationReportCapabilities
  from ..models.migration_report_issues_item import MigrationReportIssuesItem





T = TypeVar("T", bound="MigrationReport")



@_attrs_define
class MigrationReport:
    """ 
        Attributes:
            workspace_id (str | Unset):
            generated_at (datetime.datetime | Unset):
            capabilities (MigrationReportCapabilities | Unset): Per source provider: what it can carry, per entity — `{
                read: { listings: { level, notes } … }, write: { … } }`, level `full` | `partial` | `none`.
            issues (list[MigrationReportIssuesItem] | Unset):
     """

    workspace_id: str | Unset = UNSET
    generated_at: datetime.datetime | Unset = UNSET
    capabilities: MigrationReportCapabilities | Unset = UNSET
    issues: list[MigrationReportIssuesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.migration_report_capabilities import MigrationReportCapabilities
        from ..models.migration_report_issues_item import MigrationReportIssuesItem
        workspace_id = self.workspace_id

        generated_at: str | Unset = UNSET
        if not isinstance(self.generated_at, Unset):
            generated_at = self.generated_at.isoformat()

        capabilities: dict[str, Any] | Unset = UNSET
        if not isinstance(self.capabilities, Unset):
            capabilities = self.capabilities.to_dict()

        issues: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.issues, Unset):
            issues = []
            for issues_item_data in self.issues:
                issues_item = issues_item_data.to_dict()
                issues.append(issues_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id
        if generated_at is not UNSET:
            field_dict["generatedAt"] = generated_at
        if capabilities is not UNSET:
            field_dict["capabilities"] = capabilities
        if issues is not UNSET:
            field_dict["issues"] = issues

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.migration_report_capabilities import MigrationReportCapabilities
        from ..models.migration_report_issues_item import MigrationReportIssuesItem
        d = dict(src_dict)
        workspace_id = d.pop("workspaceId", UNSET)

        _generated_at = d.pop("generatedAt", UNSET)
        generated_at: datetime.datetime | Unset
        if isinstance(_generated_at,  Unset):
            generated_at = UNSET
        else:
            generated_at = isoparse(_generated_at)




        _capabilities = d.pop("capabilities", UNSET)
        capabilities: MigrationReportCapabilities | Unset
        if isinstance(_capabilities,  Unset):
            capabilities = UNSET
        else:
            capabilities = MigrationReportCapabilities.from_dict(_capabilities)




        _issues = d.pop("issues", UNSET)
        issues: list[MigrationReportIssuesItem] | Unset = UNSET
        if _issues is not UNSET:
            issues = []
            for issues_item_data in _issues:
                issues_item = MigrationReportIssuesItem.from_dict(issues_item_data)



                issues.append(issues_item)


        migration_report = cls(
            workspace_id=workspace_id,
            generated_at=generated_at,
            capabilities=capabilities,
            issues=issues,
        )


        migration_report.additional_properties = d
        return migration_report

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
