from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.listing_publish_status_connection_channel_status_type_1 import ListingPublishStatusConnectionChannelStatusType1
from ..models.listing_publish_status_connection_channel_status_type_2_type_1 import ListingPublishStatusConnectionChannelStatusType2Type1
from ..models.listing_publish_status_connection_channel_status_type_3_type_1 import ListingPublishStatusConnectionChannelStatusType3Type1
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
            platform_id (None | str | Unset): The listing's id on the channel — Airbnb listing id, Booking.com room/property
                id, VRBO listing number. Example: 5121372.
            channel_status (ListingPublishStatusConnectionChannelStatusType1 |
                ListingPublishStatusConnectionChannelStatusType2Type1 | ListingPublishStatusConnectionChannelStatusType3Type1 |
                None | Unset): Where the listing stands on the channel itself, when the channel reports it (VRBO): `online` —
                live and bookable; `offline` — hidden by the owner (`POST /v1/listings/{id}/online` brings it back); `not_live`
                — expired, new, still onboarding or deactivated by the channel (see `channelStatusDetail`). Null when not
                reported. Example: online.
            channel_status_detail (None | str | Unset): The channel's own status word behind `channelStatus` (VRBO: `LIVE`,
                `InactiveByOwnerRequest`, `Expired`, `New`, …). Example: LIVE.
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
    platform_id: None | str | Unset = UNSET
    channel_status: ListingPublishStatusConnectionChannelStatusType1 | ListingPublishStatusConnectionChannelStatusType2Type1 | ListingPublishStatusConnectionChannelStatusType3Type1 | None | Unset = UNSET
    channel_status_detail: None | str | Unset = UNSET
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

        platform_id: None | str | Unset
        if isinstance(self.platform_id, Unset):
            platform_id = UNSET
        else:
            platform_id = self.platform_id

        channel_status: None | str | Unset
        if isinstance(self.channel_status, Unset):
            channel_status = UNSET
        elif isinstance(self.channel_status, ListingPublishStatusConnectionChannelStatusType1):
            channel_status = self.channel_status.value
        elif isinstance(self.channel_status, ListingPublishStatusConnectionChannelStatusType2Type1):
            channel_status = self.channel_status.value
        elif isinstance(self.channel_status, ListingPublishStatusConnectionChannelStatusType3Type1):
            channel_status = self.channel_status.value
        else:
            channel_status = self.channel_status

        channel_status_detail: None | str | Unset
        if isinstance(self.channel_status_detail, Unset):
            channel_status_detail = UNSET
        else:
            channel_status_detail = self.channel_status_detail

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
        if platform_id is not UNSET:
            field_dict["platformId"] = platform_id
        if channel_status is not UNSET:
            field_dict["channelStatus"] = channel_status
        if channel_status_detail is not UNSET:
            field_dict["channelStatusDetail"] = channel_status_detail
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


        def _parse_platform_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        platform_id = _parse_platform_id(d.pop("platformId", UNSET))


        def _parse_channel_status(data: object) -> ListingPublishStatusConnectionChannelStatusType1 | ListingPublishStatusConnectionChannelStatusType2Type1 | ListingPublishStatusConnectionChannelStatusType3Type1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                channel_status_type_1 = ListingPublishStatusConnectionChannelStatusType1(data)



                return channel_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                channel_status_type_2_type_1 = ListingPublishStatusConnectionChannelStatusType2Type1(data)



                return channel_status_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                channel_status_type_3_type_1 = ListingPublishStatusConnectionChannelStatusType3Type1(data)



                return channel_status_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListingPublishStatusConnectionChannelStatusType1 | ListingPublishStatusConnectionChannelStatusType2Type1 | ListingPublishStatusConnectionChannelStatusType3Type1 | None | Unset, data)

        channel_status = _parse_channel_status(d.pop("channelStatus", UNSET))


        def _parse_channel_status_detail(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        channel_status_detail = _parse_channel_status_detail(d.pop("channelStatusDetail", UNSET))


        locked_fields = cast(list[str], d.pop("lockedFields", UNSET))


        listing_publish_status_connection = cls(
            channel=channel,
            connected=connected,
            sync_enabled=sync_enabled,
            since=since,
            platform_id=platform_id,
            channel_status=channel_status,
            channel_status_detail=channel_status_detail,
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
