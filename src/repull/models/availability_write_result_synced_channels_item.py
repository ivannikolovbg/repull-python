from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.availability_write_result_synced_channels_item_status import AvailabilityWriteResultSyncedChannelsItemStatus
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AvailabilityWriteResultSyncedChannelsItem")



@_attrs_define
class AvailabilityWriteResultSyncedChannelsItem:
    """ 
        Attributes:
            listing_id (str | Unset):
            channel (str | Unset): `airbnb`, `booking`, `vrbo`, or another connected channel. Example: booking.
            channel_listing_id (None | str | Unset): The channel's own id for the listing or room.
            status (AvailabilityWriteResultSyncedChannelsItemStatus | Unset): `accepted`: the channel took the write in this
                request. `queued` (Vrbo): sent within minutes and read back; `GET /v1/listings/{id}/calendar-sync` shows the
                outcome. `failed`: the channel refused it; see `error`.
            error (None | str | Unset):
            auth_error (bool | Unset): True when the channel's authorization has expired: reconnect, don't retry.
     """

    listing_id: str | Unset = UNSET
    channel: str | Unset = UNSET
    channel_listing_id: None | str | Unset = UNSET
    status: AvailabilityWriteResultSyncedChannelsItemStatus | Unset = UNSET
    error: None | str | Unset = UNSET
    auth_error: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        listing_id = self.listing_id

        channel = self.channel

        channel_listing_id: None | str | Unset
        if isinstance(self.channel_listing_id, Unset):
            channel_listing_id = UNSET
        else:
            channel_listing_id = self.channel_listing_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        auth_error = self.auth_error


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if channel is not UNSET:
            field_dict["channel"] = channel
        if channel_listing_id is not UNSET:
            field_dict["channelListingId"] = channel_listing_id
        if status is not UNSET:
            field_dict["status"] = status
        if error is not UNSET:
            field_dict["error"] = error
        if auth_error is not UNSET:
            field_dict["authError"] = auth_error

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        listing_id = d.pop("listingId", UNSET)

        channel = d.pop("channel", UNSET)

        def _parse_channel_listing_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        channel_listing_id = _parse_channel_listing_id(d.pop("channelListingId", UNSET))


        _status = d.pop("status", UNSET)
        status: AvailabilityWriteResultSyncedChannelsItemStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = AvailabilityWriteResultSyncedChannelsItemStatus(_status)




        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))


        auth_error = d.pop("authError", UNSET)

        availability_write_result_synced_channels_item = cls(
            listing_id=listing_id,
            channel=channel,
            channel_listing_id=channel_listing_id,
            status=status,
            error=error,
            auth_error=auth_error,
        )


        availability_write_result_synced_channels_item.additional_properties = d
        return availability_write_result_synced_channels_item

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
