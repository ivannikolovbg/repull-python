from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="AirbnbConnectionHost")



@_attrs_define
class AirbnbConnectionHost:
    """ One Airbnb host record under the workspace, decorated with its most recent disconnect reason from
    `airbnb_host_events` (backfill events excluded).

        Attributes:
            airbnb_user_id (str): Upstream Airbnb user id. Example: 719854265.
            name (None | str): Display name (preferred form, falling back to legal first name). Null when both fields are
                empty. Example: STR Assistance.
            is_connected (bool):
            last_synced_at (datetime.datetime | None): When the host record was last touched (token refresh / activation /
                restriction). Closest available proxy for "last successful sync".
            deactivated_at (datetime.datetime | None): When the host was last marked inactive. Null on currently-connected
                hosts.
            last_disconnect_reason (None | str): Reason of the most recent non-backfill disconnect event. Common values:
                `token_refresh_rejected`, `auth_expired`, `user_revoked`. Null when the host has no recorded disconnects.
                Example: token_refresh_rejected.
     """

    airbnb_user_id: str
    name: None | str
    is_connected: bool
    last_synced_at: datetime.datetime | None
    deactivated_at: datetime.datetime | None
    last_disconnect_reason: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        airbnb_user_id = self.airbnb_user_id

        name: None | str
        name = self.name

        is_connected = self.is_connected

        last_synced_at: None | str
        if isinstance(self.last_synced_at, datetime.datetime):
            last_synced_at = self.last_synced_at.isoformat()
        else:
            last_synced_at = self.last_synced_at

        deactivated_at: None | str
        if isinstance(self.deactivated_at, datetime.datetime):
            deactivated_at = self.deactivated_at.isoformat()
        else:
            deactivated_at = self.deactivated_at

        last_disconnect_reason: None | str
        last_disconnect_reason = self.last_disconnect_reason


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "airbnbUserId": airbnb_user_id,
            "name": name,
            "isConnected": is_connected,
            "lastSyncedAt": last_synced_at,
            "deactivatedAt": deactivated_at,
            "lastDisconnectReason": last_disconnect_reason,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        airbnb_user_id = d.pop("airbnbUserId")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))


        is_connected = d.pop("isConnected")

        def _parse_last_synced_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_synced_at_type_0 = isoparse(data)



                return last_synced_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_synced_at = _parse_last_synced_at(d.pop("lastSyncedAt"))


        def _parse_deactivated_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deactivated_at_type_0 = isoparse(data)



                return deactivated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        deactivated_at = _parse_deactivated_at(d.pop("deactivatedAt"))


        def _parse_last_disconnect_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_disconnect_reason = _parse_last_disconnect_reason(d.pop("lastDisconnectReason"))


        airbnb_connection_host = cls(
            airbnb_user_id=airbnb_user_id,
            name=name,
            is_connected=is_connected,
            last_synced_at=last_synced_at,
            deactivated_at=deactivated_at,
            last_disconnect_reason=last_disconnect_reason,
        )


        airbnb_connection_host.additional_properties = d
        return airbnb_connection_host

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
