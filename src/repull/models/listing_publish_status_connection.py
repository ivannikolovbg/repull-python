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






T = TypeVar("T", bound="ListingPublishStatusConnection")



@_attrs_define
class ListingPublishStatusConnection:
    """ Per-channel connection state. Distinct from `channels` (sync activity) — a listing can be connected here yet have
    empty `channels` if it has never been pushed.

        Attributes:
            channel (str | Unset): Channel name: airbnb, booking, vrbo, etc. Example: airbnb.
            connected (bool | Unset): True when the link is active (not disconnected/suspended).
            sync_enabled (bool | Unset): True when sync writes are enabled for this channel.
            since (datetime.datetime | None | Unset): ISO timestamp the connection was first established.
     """

    channel: str | Unset = UNSET
    connected: bool | Unset = UNSET
    sync_enabled: bool | Unset = UNSET
    since: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        channel = self.channel

        connected = self.connected

        sync_enabled = self.sync_enabled

        since: None | str | Unset
        if isinstance(self.since, Unset):
            since = UNSET
        elif isinstance(self.since, datetime.datetime):
            since = self.since.isoformat()
        else:
            since = self.since


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if channel is not UNSET:
            field_dict["channel"] = channel
        if connected is not UNSET:
            field_dict["connected"] = connected
        if sync_enabled is not UNSET:
            field_dict["syncEnabled"] = sync_enabled
        if since is not UNSET:
            field_dict["since"] = since

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        channel = d.pop("channel", UNSET)

        connected = d.pop("connected", UNSET)

        sync_enabled = d.pop("syncEnabled", UNSET)

        def _parse_since(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                since_type_0 = isoparse(data)



                return since_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        since = _parse_since(d.pop("since", UNSET))


        listing_publish_status_connection = cls(
            channel=channel,
            connected=connected,
            sync_enabled=sync_enabled,
            since=since,
        )


        listing_publish_status_connection.additional_properties = d
        return listing_publish_status_connection

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
