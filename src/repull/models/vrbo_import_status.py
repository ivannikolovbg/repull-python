from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.vrbo_import_status_access_type import VrboImportStatusAccessType
from ..models.vrbo_import_status_state import VrboImportStatusState
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="VrboImportStatus")



@_attrs_define
class VrboImportStatus:
    """ Where a Vrbo account import stands. Nothing is imported until its unit mapping is confirmed; then upcoming bookings
    and the last 30 days of messages come first, and the whole account history after.

        Attributes:
            account_id (int | Unset):
            state (VrboImportStatusState | Unset):
            access_type (VrboImportStatusAccessType | Unset): `messaging`: bookings and messages only, the calendar is never
                pushed.
            requested_at (datetime.datetime | None | Unset): When the mapping was confirmed.
            priority_imported_at (datetime.datetime | None | Unset): Upcoming bookings and the last 30 days are in.
            history_completed_at (datetime.datetime | None | Unset):
            history_complete (bool | Unset): The whole account history is imported.
            last_synced_at (datetime.datetime | None | Unset): Last completed sync (Vrbo is read every few minutes and on
                each Vrbo notification email).
            conversations_seen (int | Unset):
            conversations_imported (int | Unset):
            reservations (int | Unset): Bookings imported so far.
     """

    account_id: int | Unset = UNSET
    state: VrboImportStatusState | Unset = UNSET
    access_type: VrboImportStatusAccessType | Unset = UNSET
    requested_at: datetime.datetime | None | Unset = UNSET
    priority_imported_at: datetime.datetime | None | Unset = UNSET
    history_completed_at: datetime.datetime | None | Unset = UNSET
    history_complete: bool | Unset = UNSET
    last_synced_at: datetime.datetime | None | Unset = UNSET
    conversations_seen: int | Unset = UNSET
    conversations_imported: int | Unset = UNSET
    reservations: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value


        access_type: str | Unset = UNSET
        if not isinstance(self.access_type, Unset):
            access_type = self.access_type.value


        requested_at: None | str | Unset
        if isinstance(self.requested_at, Unset):
            requested_at = UNSET
        elif isinstance(self.requested_at, datetime.datetime):
            requested_at = self.requested_at.isoformat()
        else:
            requested_at = self.requested_at

        priority_imported_at: None | str | Unset
        if isinstance(self.priority_imported_at, Unset):
            priority_imported_at = UNSET
        elif isinstance(self.priority_imported_at, datetime.datetime):
            priority_imported_at = self.priority_imported_at.isoformat()
        else:
            priority_imported_at = self.priority_imported_at

        history_completed_at: None | str | Unset
        if isinstance(self.history_completed_at, Unset):
            history_completed_at = UNSET
        elif isinstance(self.history_completed_at, datetime.datetime):
            history_completed_at = self.history_completed_at.isoformat()
        else:
            history_completed_at = self.history_completed_at

        history_complete = self.history_complete

        last_synced_at: None | str | Unset
        if isinstance(self.last_synced_at, Unset):
            last_synced_at = UNSET
        elif isinstance(self.last_synced_at, datetime.datetime):
            last_synced_at = self.last_synced_at.isoformat()
        else:
            last_synced_at = self.last_synced_at

        conversations_seen = self.conversations_seen

        conversations_imported = self.conversations_imported

        reservations = self.reservations


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if state is not UNSET:
            field_dict["state"] = state
        if access_type is not UNSET:
            field_dict["accessType"] = access_type
        if requested_at is not UNSET:
            field_dict["requestedAt"] = requested_at
        if priority_imported_at is not UNSET:
            field_dict["priorityImportedAt"] = priority_imported_at
        if history_completed_at is not UNSET:
            field_dict["historyCompletedAt"] = history_completed_at
        if history_complete is not UNSET:
            field_dict["historyComplete"] = history_complete
        if last_synced_at is not UNSET:
            field_dict["lastSyncedAt"] = last_synced_at
        if conversations_seen is not UNSET:
            field_dict["conversationsSeen"] = conversations_seen
        if conversations_imported is not UNSET:
            field_dict["conversationsImported"] = conversations_imported
        if reservations is not UNSET:
            field_dict["reservations"] = reservations

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("accountId", UNSET)

        _state = d.pop("state", UNSET)
        state: VrboImportStatusState | Unset
        if isinstance(_state,  Unset):
            state = UNSET
        else:
            state = VrboImportStatusState(_state)




        _access_type = d.pop("accessType", UNSET)
        access_type: VrboImportStatusAccessType | Unset
        if isinstance(_access_type,  Unset):
            access_type = UNSET
        else:
            access_type = VrboImportStatusAccessType(_access_type)




        def _parse_requested_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                requested_at_type_0 = isoparse(data)



                return requested_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        requested_at = _parse_requested_at(d.pop("requestedAt", UNSET))


        def _parse_priority_imported_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                priority_imported_at_type_0 = isoparse(data)



                return priority_imported_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        priority_imported_at = _parse_priority_imported_at(d.pop("priorityImportedAt", UNSET))


        def _parse_history_completed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                history_completed_at_type_0 = isoparse(data)



                return history_completed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        history_completed_at = _parse_history_completed_at(d.pop("historyCompletedAt", UNSET))


        history_complete = d.pop("historyComplete", UNSET)

        def _parse_last_synced_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_synced_at_type_0 = isoparse(data)



                return last_synced_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_synced_at = _parse_last_synced_at(d.pop("lastSyncedAt", UNSET))


        conversations_seen = d.pop("conversationsSeen", UNSET)

        conversations_imported = d.pop("conversationsImported", UNSET)

        reservations = d.pop("reservations", UNSET)

        vrbo_import_status = cls(
            account_id=account_id,
            state=state,
            access_type=access_type,
            requested_at=requested_at,
            priority_imported_at=priority_imported_at,
            history_completed_at=history_completed_at,
            history_complete=history_complete,
            last_synced_at=last_synced_at,
            conversations_seen=conversations_seen,
            conversations_imported=conversations_imported,
            reservations=reservations,
        )


        vrbo_import_status.additional_properties = d
        return vrbo_import_status

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
