from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetChannelHealthResponse200Vrbo")



@_attrs_define
class GetChannelHealthResponse200Vrbo:
    """ VRBO only — the connector's own signals.

        Attributes:
            accounts_connected (int | Unset):
            accounts_signed_out (int | Unset): Accounts VRBO signed out; `status` is `down` while any is.
            inbox_sync_late (int | Unset): Accounts whose last full inbox sync is older than 30 minutes (it runs every 5).
            calendar_queue_backlog (int | Unset): Listings with a calendar push waiting.
            calendar_oldest_wait_minutes (int | Unset):
            window_hours (int | Unset): Hours the push failure rate is judged over.
     """

    accounts_connected: int | Unset = UNSET
    accounts_signed_out: int | Unset = UNSET
    inbox_sync_late: int | Unset = UNSET
    calendar_queue_backlog: int | Unset = UNSET
    calendar_oldest_wait_minutes: int | Unset = UNSET
    window_hours: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        accounts_connected = self.accounts_connected

        accounts_signed_out = self.accounts_signed_out

        inbox_sync_late = self.inbox_sync_late

        calendar_queue_backlog = self.calendar_queue_backlog

        calendar_oldest_wait_minutes = self.calendar_oldest_wait_minutes

        window_hours = self.window_hours


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if accounts_connected is not UNSET:
            field_dict["accounts_connected"] = accounts_connected
        if accounts_signed_out is not UNSET:
            field_dict["accounts_signed_out"] = accounts_signed_out
        if inbox_sync_late is not UNSET:
            field_dict["inbox_sync_late"] = inbox_sync_late
        if calendar_queue_backlog is not UNSET:
            field_dict["calendar_queue_backlog"] = calendar_queue_backlog
        if calendar_oldest_wait_minutes is not UNSET:
            field_dict["calendar_oldest_wait_minutes"] = calendar_oldest_wait_minutes
        if window_hours is not UNSET:
            field_dict["window_hours"] = window_hours

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        accounts_connected = d.pop("accounts_connected", UNSET)

        accounts_signed_out = d.pop("accounts_signed_out", UNSET)

        inbox_sync_late = d.pop("inbox_sync_late", UNSET)

        calendar_queue_backlog = d.pop("calendar_queue_backlog", UNSET)

        calendar_oldest_wait_minutes = d.pop("calendar_oldest_wait_minutes", UNSET)

        window_hours = d.pop("window_hours", UNSET)

        get_channel_health_response_200_vrbo = cls(
            accounts_connected=accounts_connected,
            accounts_signed_out=accounts_signed_out,
            inbox_sync_late=inbox_sync_late,
            calendar_queue_backlog=calendar_queue_backlog,
            calendar_oldest_wait_minutes=calendar_oldest_wait_minutes,
            window_hours=window_hours,
        )


        get_channel_health_response_200_vrbo.additional_properties = d
        return get_channel_health_response_200_vrbo

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
