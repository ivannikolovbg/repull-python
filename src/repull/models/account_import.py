from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.account_import_outcome import AccountImportOutcome
from ..models.account_import_status import AccountImportStatus
from ..models.account_import_trigger import AccountImportTrigger
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.account_import_counts import AccountImportCounts
  from ..models.account_import_stage import AccountImportStage





T = TypeVar("T", bound="AccountImport")



@_attrs_define
class AccountImport:
    """ One import run of a connected account: the first sync after connecting, a room or unit mapped later, a reconnect or
    a re-sync.

        Attributes:
            id (UUID | Unset): The import id — the `importId` on `account.import.*` webhooks.
            status (AccountImportStatus | Unset):
            trigger (AccountImportTrigger | Unset):
            outcome (AccountImportOutcome | Unset): `completed` imports only: `partial` when some units failed (see
                `stages`).
            reason (None | str | Unset): `failed` imports only: why it stopped — e.g. `needs_permissions`,
                `duplicate_account`, `stalled`.
            started_at (datetime.datetime | Unset):
            last_activity_at (datetime.datetime | Unset):
            completed_at (datetime.datetime | None | Unset):
            stages (list[AccountImportStage] | Unset):
            counts (AccountImportCounts | Unset): What the import brought in. A channel reports the keys it imports.
     """

    id: UUID | Unset = UNSET
    status: AccountImportStatus | Unset = UNSET
    trigger: AccountImportTrigger | Unset = UNSET
    outcome: AccountImportOutcome | Unset = UNSET
    reason: None | str | Unset = UNSET
    started_at: datetime.datetime | Unset = UNSET
    last_activity_at: datetime.datetime | Unset = UNSET
    completed_at: datetime.datetime | None | Unset = UNSET
    stages: list[AccountImportStage] | Unset = UNSET
    counts: AccountImportCounts | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.account_import_counts import AccountImportCounts
        from ..models.account_import_stage import AccountImportStage
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        trigger: str | Unset = UNSET
        if not isinstance(self.trigger, Unset):
            trigger = self.trigger.value


        outcome: str | Unset = UNSET
        if not isinstance(self.outcome, Unset):
            outcome = self.outcome.value


        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        started_at: str | Unset = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()

        last_activity_at: str | Unset = UNSET
        if not isinstance(self.last_activity_at, Unset):
            last_activity_at = self.last_activity_at.isoformat()

        completed_at: None | str | Unset
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        elif isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

        stages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.stages, Unset):
            stages = []
            for stages_item_data in self.stages:
                stages_item = stages_item_data.to_dict()
                stages.append(stages_item)



        counts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.counts, Unset):
            counts = self.counts.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if trigger is not UNSET:
            field_dict["trigger"] = trigger
        if outcome is not UNSET:
            field_dict["outcome"] = outcome
        if reason is not UNSET:
            field_dict["reason"] = reason
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if last_activity_at is not UNSET:
            field_dict["lastActivityAt"] = last_activity_at
        if completed_at is not UNSET:
            field_dict["completedAt"] = completed_at
        if stages is not UNSET:
            field_dict["stages"] = stages
        if counts is not UNSET:
            field_dict["counts"] = counts

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_import_counts import AccountImportCounts
        from ..models.account_import_stage import AccountImportStage
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        _status = d.pop("status", UNSET)
        status: AccountImportStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = AccountImportStatus(_status)




        _trigger = d.pop("trigger", UNSET)
        trigger: AccountImportTrigger | Unset
        if isinstance(_trigger,  Unset):
            trigger = UNSET
        else:
            trigger = AccountImportTrigger(_trigger)




        _outcome = d.pop("outcome", UNSET)
        outcome: AccountImportOutcome | Unset
        if isinstance(_outcome,  Unset):
            outcome = UNSET
        else:
            outcome = AccountImportOutcome(_outcome)




        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))


        _started_at = d.pop("startedAt", UNSET)
        started_at: datetime.datetime | Unset
        if isinstance(_started_at,  Unset):
            started_at = UNSET
        else:
            started_at = isoparse(_started_at)




        _last_activity_at = d.pop("lastActivityAt", UNSET)
        last_activity_at: datetime.datetime | Unset
        if isinstance(_last_activity_at,  Unset):
            last_activity_at = UNSET
        else:
            last_activity_at = isoparse(_last_activity_at)




        def _parse_completed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_at_type_0 = isoparse(data)



                return completed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        completed_at = _parse_completed_at(d.pop("completedAt", UNSET))


        _stages = d.pop("stages", UNSET)
        stages: list[AccountImportStage] | Unset = UNSET
        if _stages is not UNSET:
            stages = []
            for stages_item_data in _stages:
                stages_item = AccountImportStage.from_dict(stages_item_data)



                stages.append(stages_item)


        _counts = d.pop("counts", UNSET)
        counts: AccountImportCounts | Unset
        if isinstance(_counts,  Unset):
            counts = UNSET
        else:
            counts = AccountImportCounts.from_dict(_counts)




        account_import = cls(
            id=id,
            status=status,
            trigger=trigger,
            outcome=outcome,
            reason=reason,
            started_at=started_at,
            last_activity_at=last_activity_at,
            completed_at=completed_at,
            stages=stages,
            counts=counts,
        )


        account_import.additional_properties = d
        return account_import

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
