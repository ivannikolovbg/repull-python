from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.migration_report_issues_item_severity import MigrationReportIssuesItemSeverity
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MigrationReportIssuesItem")



@_attrs_define
class MigrationReportIssuesItem:
    """ 
        Attributes:
            severity (MigrationReportIssuesItemSeverity | Unset):
            entity (str | Unset):  Example: reservations.
            code (str | Unset):  Example: reservation_missing_guest_contact.
            message (str | Unset):
            count (int | Unset):
            sample_ids (list[int] | Unset): Up to 10 affected listing / reservation ids.
     """

    severity: MigrationReportIssuesItemSeverity | Unset = UNSET
    entity: str | Unset = UNSET
    code: str | Unset = UNSET
    message: str | Unset = UNSET
    count: int | Unset = UNSET
    sample_ids: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        severity: str | Unset = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity.value


        entity = self.entity

        code = self.code

        message = self.message

        count = self.count

        sample_ids: list[int] | Unset = UNSET
        if not isinstance(self.sample_ids, Unset):
            sample_ids = self.sample_ids




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if severity is not UNSET:
            field_dict["severity"] = severity
        if entity is not UNSET:
            field_dict["entity"] = entity
        if code is not UNSET:
            field_dict["code"] = code
        if message is not UNSET:
            field_dict["message"] = message
        if count is not UNSET:
            field_dict["count"] = count
        if sample_ids is not UNSET:
            field_dict["sampleIds"] = sample_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _severity = d.pop("severity", UNSET)
        severity: MigrationReportIssuesItemSeverity | Unset
        if isinstance(_severity,  Unset):
            severity = UNSET
        else:
            severity = MigrationReportIssuesItemSeverity(_severity)




        entity = d.pop("entity", UNSET)

        code = d.pop("code", UNSET)

        message = d.pop("message", UNSET)

        count = d.pop("count", UNSET)

        sample_ids = cast(list[int], d.pop("sampleIds", UNSET))


        migration_report_issues_item = cls(
            severity=severity,
            entity=entity,
            code=code,
            message=message,
            count=count,
            sample_ids=sample_ids,
        )


        migration_report_issues_item.additional_properties = d
        return migration_report_issues_item

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
