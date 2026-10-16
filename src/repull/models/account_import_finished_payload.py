from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.account_import_finished_payload_outcome import AccountImportFinishedPayloadOutcome
from ..models.account_import_finished_payload_status import AccountImportFinishedPayloadStatus
from ..models.account_import_finished_payload_trigger import AccountImportFinishedPayloadTrigger
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.account_import_counts import AccountImportCounts
  from ..models.account_import_stage import AccountImportStage





T = TypeVar("T", bound="AccountImportFinishedPayload")



@_attrs_define
class AccountImportFinishedPayload:
    """ 
        Attributes:
            import_id (UUID | Unset):
            trigger (AccountImportFinishedPayloadTrigger | Unset):
            status (AccountImportFinishedPayloadStatus | Unset):
            outcome (AccountImportFinishedPayloadOutcome | Unset):
            started_at (datetime.datetime | Unset):
            completed_at (datetime.datetime | Unset):
            stages (list[AccountImportStage] | Unset):
            counts (AccountImportCounts | Unset): What the import brought in. A channel reports the keys it imports.
            reason (None | str | Unset): `account.import.failed` only.
     """

    import_id: UUID | Unset = UNSET
    trigger: AccountImportFinishedPayloadTrigger | Unset = UNSET
    status: AccountImportFinishedPayloadStatus | Unset = UNSET
    outcome: AccountImportFinishedPayloadOutcome | Unset = UNSET
    started_at: datetime.datetime | Unset = UNSET
    completed_at: datetime.datetime | Unset = UNSET
    stages: list[AccountImportStage] | Unset = UNSET
    counts: AccountImportCounts | Unset = UNSET
    reason: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.account_import_counts import AccountImportCounts
        from ..models.account_import_stage import AccountImportStage
        import_id: str | Unset = UNSET
        if not isinstance(self.import_id, Unset):
            import_id = str(self.import_id)

        trigger: str | Unset = UNSET
        if not isinstance(self.trigger, Unset):
            trigger = self.trigger.value


        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        outcome: str | Unset = UNSET
        if not isinstance(self.outcome, Unset):
            outcome = self.outcome.value


        started_at: str | Unset = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()

        completed_at: str | Unset = UNSET
        if not isinstance(self.completed_at, Unset):
            completed_at = self.completed_at.isoformat()

        stages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.stages, Unset):
            stages = []
            for stages_item_data in self.stages:
                stages_item = stages_item_data.to_dict()
                stages.append(stages_item)



        counts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.counts, Unset):
            counts = self.counts.to_dict()

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if import_id is not UNSET:
            field_dict["importId"] = import_id
        if trigger is not UNSET:
            field_dict["trigger"] = trigger
        if status is not UNSET:
            field_dict["status"] = status
        if outcome is not UNSET:
            field_dict["outcome"] = outcome
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if completed_at is not UNSET:
            field_dict["completedAt"] = completed_at
        if stages is not UNSET:
            field_dict["stages"] = stages
        if counts is not UNSET:
            field_dict["counts"] = counts
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_import_counts import AccountImportCounts
        from ..models.account_import_stage import AccountImportStage
        d = dict(src_dict)
        _import_id = d.pop("importId", UNSET)
        import_id: UUID | Unset
        if isinstance(_import_id,  Unset):
            import_id = UNSET
        else:
            import_id = UUID(_import_id)




        _trigger = d.pop("trigger", UNSET)
        trigger: AccountImportFinishedPayloadTrigger | Unset
        if isinstance(_trigger,  Unset):
            trigger = UNSET
        else:
            trigger = AccountImportFinishedPayloadTrigger(_trigger)




        _status = d.pop("status", UNSET)
        status: AccountImportFinishedPayloadStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = AccountImportFinishedPayloadStatus(_status)




        _outcome = d.pop("outcome", UNSET)
        outcome: AccountImportFinishedPayloadOutcome | Unset
        if isinstance(_outcome,  Unset):
            outcome = UNSET
        else:
            outcome = AccountImportFinishedPayloadOutcome(_outcome)




        _started_at = d.pop("startedAt", UNSET)
        started_at: datetime.datetime | Unset
        if isinstance(_started_at,  Unset):
            started_at = UNSET
        else:
            started_at = isoparse(_started_at)




        _completed_at = d.pop("completedAt", UNSET)
        completed_at: datetime.datetime | Unset
        if isinstance(_completed_at,  Unset):
            completed_at = UNSET
        else:
            completed_at = isoparse(_completed_at)




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




        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))


        account_import_finished_payload = cls(
            import_id=import_id,
            trigger=trigger,
            status=status,
            outcome=outcome,
            started_at=started_at,
            completed_at=completed_at,
            stages=stages,
            counts=counts,
            reason=reason,
        )


        account_import_finished_payload.additional_properties = d
        return account_import_finished_payload

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
