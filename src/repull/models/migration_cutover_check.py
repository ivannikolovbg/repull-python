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
  from ..models.migration_cutover_check_mismatched_item import MigrationCutoverCheckMismatchedItem
  from ..models.migration_reservation_ref import MigrationReservationRef





T = TypeVar("T", bound="MigrationCutoverCheck")



@_attrs_define
class MigrationCutoverCheck:
    """ 
        Attributes:
            workspace_id (str | Unset):
            checked_at (datetime.datetime | Unset):
            matched (int | Unset):
            missing (list[MigrationReservationRef] | Unset): Upcoming in the source, absent from the destination.
            extra (list[MigrationReservationRef] | Unset): In the destination, not an upcoming reservation in the source.
            mismatched (list[MigrationCutoverCheckMismatchedItem] | Unset):
     """

    workspace_id: str | Unset = UNSET
    checked_at: datetime.datetime | Unset = UNSET
    matched: int | Unset = UNSET
    missing: list[MigrationReservationRef] | Unset = UNSET
    extra: list[MigrationReservationRef] | Unset = UNSET
    mismatched: list[MigrationCutoverCheckMismatchedItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.migration_cutover_check_mismatched_item import MigrationCutoverCheckMismatchedItem
        from ..models.migration_reservation_ref import MigrationReservationRef
        workspace_id = self.workspace_id

        checked_at: str | Unset = UNSET
        if not isinstance(self.checked_at, Unset):
            checked_at = self.checked_at.isoformat()

        matched = self.matched

        missing: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.missing, Unset):
            missing = []
            for missing_item_data in self.missing:
                missing_item = missing_item_data.to_dict()
                missing.append(missing_item)



        extra: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.extra, Unset):
            extra = []
            for extra_item_data in self.extra:
                extra_item = extra_item_data.to_dict()
                extra.append(extra_item)



        mismatched: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.mismatched, Unset):
            mismatched = []
            for mismatched_item_data in self.mismatched:
                mismatched_item = mismatched_item_data.to_dict()
                mismatched.append(mismatched_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id
        if checked_at is not UNSET:
            field_dict["checkedAt"] = checked_at
        if matched is not UNSET:
            field_dict["matched"] = matched
        if missing is not UNSET:
            field_dict["missing"] = missing
        if extra is not UNSET:
            field_dict["extra"] = extra
        if mismatched is not UNSET:
            field_dict["mismatched"] = mismatched

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.migration_cutover_check_mismatched_item import MigrationCutoverCheckMismatchedItem
        from ..models.migration_reservation_ref import MigrationReservationRef
        d = dict(src_dict)
        workspace_id = d.pop("workspaceId", UNSET)

        _checked_at = d.pop("checkedAt", UNSET)
        checked_at: datetime.datetime | Unset
        if isinstance(_checked_at,  Unset):
            checked_at = UNSET
        else:
            checked_at = isoparse(_checked_at)




        matched = d.pop("matched", UNSET)

        _missing = d.pop("missing", UNSET)
        missing: list[MigrationReservationRef] | Unset = UNSET
        if _missing is not UNSET:
            missing = []
            for missing_item_data in _missing:
                missing_item = MigrationReservationRef.from_dict(missing_item_data)



                missing.append(missing_item)


        _extra = d.pop("extra", UNSET)
        extra: list[MigrationReservationRef] | Unset = UNSET
        if _extra is not UNSET:
            extra = []
            for extra_item_data in _extra:
                extra_item = MigrationReservationRef.from_dict(extra_item_data)



                extra.append(extra_item)


        _mismatched = d.pop("mismatched", UNSET)
        mismatched: list[MigrationCutoverCheckMismatchedItem] | Unset = UNSET
        if _mismatched is not UNSET:
            mismatched = []
            for mismatched_item_data in _mismatched:
                mismatched_item = MigrationCutoverCheckMismatchedItem.from_dict(mismatched_item_data)



                mismatched.append(mismatched_item)


        migration_cutover_check = cls(
            workspace_id=workspace_id,
            checked_at=checked_at,
            matched=matched,
            missing=missing,
            extra=extra,
            mismatched=mismatched,
        )


        migration_cutover_check.additional_properties = d
        return migration_cutover_check

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
