from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.account_import_started_payload_trigger import AccountImportStartedPayloadTrigger
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="AccountImportStartedPayload")



@_attrs_define
class AccountImportStartedPayload:
    """ 
        Attributes:
            import_id (UUID | Unset):
            trigger (AccountImportStartedPayloadTrigger | Unset):
            started_at (datetime.datetime | Unset):
            stages (list[str] | Unset): The stages this import will run.
     """

    import_id: UUID | Unset = UNSET
    trigger: AccountImportStartedPayloadTrigger | Unset = UNSET
    started_at: datetime.datetime | Unset = UNSET
    stages: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        import_id: str | Unset = UNSET
        if not isinstance(self.import_id, Unset):
            import_id = str(self.import_id)

        trigger: str | Unset = UNSET
        if not isinstance(self.trigger, Unset):
            trigger = self.trigger.value


        started_at: str | Unset = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()

        stages: list[str] | Unset = UNSET
        if not isinstance(self.stages, Unset):
            stages = self.stages




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if import_id is not UNSET:
            field_dict["importId"] = import_id
        if trigger is not UNSET:
            field_dict["trigger"] = trigger
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if stages is not UNSET:
            field_dict["stages"] = stages

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _import_id = d.pop("importId", UNSET)
        import_id: UUID | Unset
        if isinstance(_import_id,  Unset):
            import_id = UNSET
        else:
            import_id = UUID(_import_id)




        _trigger = d.pop("trigger", UNSET)
        trigger: AccountImportStartedPayloadTrigger | Unset
        if isinstance(_trigger,  Unset):
            trigger = UNSET
        else:
            trigger = AccountImportStartedPayloadTrigger(_trigger)




        _started_at = d.pop("startedAt", UNSET)
        started_at: datetime.datetime | Unset
        if isinstance(_started_at,  Unset):
            started_at = UNSET
        else:
            started_at = isoparse(_started_at)




        stages = cast(list[str], d.pop("stages", UNSET))


        account_import_started_payload = cls(
            import_id=import_id,
            trigger=trigger,
            started_at=started_at,
            stages=stages,
        )


        account_import_started_payload.additional_properties = d
        return account_import_started_payload

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
