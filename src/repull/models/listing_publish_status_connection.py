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
            locked_fields (list[str] | Unset): Fields the channel will not let this listing change. **Airbnb only** —
                present on the `airbnb` entry and absent on every other channel, because no other channel has the concept.

                Airbnb does not refuse a write to a locked field: the request returns 200, reports the field as locked, and
                applies nothing. So a write to one of these looks exactly like a write that worked. Read this before you let a
                user edit — it is here, rather than only on `GET /v1/channels/airbnb/listings/{id}`, because this is the
                endpoint a listing editor already calls.

                Empty for a listing with nothing locked, and for one that has not synced since we began recording them — the two
                are not distinguished, because a caller acts the same way on both. This is what Airbnb last told us, not a
                promise: a lock can appear between syncs, which is why a publish result also reports `lockedFields`. Example:
                ['name', 'property_type_category'].
     """

    channel: str | Unset = UNSET
    connected: bool | Unset = UNSET
    sync_enabled: bool | Unset = UNSET
    since: datetime.datetime | None | Unset = UNSET
    locked_fields: list[str] | Unset = UNSET
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

        locked_fields: list[str] | Unset = UNSET
        if not isinstance(self.locked_fields, Unset):
            locked_fields = self.locked_fields




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
        if locked_fields is not UNSET:
            field_dict["lockedFields"] = locked_fields

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


        locked_fields = cast(list[str], d.pop("lockedFields", UNSET))


        listing_publish_status_connection = cls(
            channel=channel,
            connected=connected,
            sync_enabled=sync_enabled,
            since=since,
            locked_fields=locked_fields,
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
