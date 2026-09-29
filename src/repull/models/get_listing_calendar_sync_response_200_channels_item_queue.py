from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_listing_calendar_sync_response_200_channels_item_queue_state import GetListingCalendarSyncResponse200ChannelsItemQueueState
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.get_listing_calendar_sync_response_200_channels_item_queue_last_push_type_0 import GetListingCalendarSyncResponse200ChannelsItemQueueLastPushType0





T = TypeVar("T", bound="GetListingCalendarSyncResponse200ChannelsItemQueue")



@_attrs_define
class GetListingCalendarSyncResponse200ChannelsItemQueue:
    """ VRBO only — the paced push queue.

        Attributes:
            state (GetListingCalendarSyncResponse200ChannelsItemQueueState | Unset):
            queued_nights (int | Unset): Nights waiting to be pushed.
            queued_at (datetime.datetime | None | Unset):
            last_push (GetListingCalendarSyncResponse200ChannelsItemQueueLastPushType0 | None | Unset):
     """

    state: GetListingCalendarSyncResponse200ChannelsItemQueueState | Unset = UNSET
    queued_nights: int | Unset = UNSET
    queued_at: datetime.datetime | None | Unset = UNSET
    last_push: GetListingCalendarSyncResponse200ChannelsItemQueueLastPushType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_listing_calendar_sync_response_200_channels_item_queue_last_push_type_0 import GetListingCalendarSyncResponse200ChannelsItemQueueLastPushType0
        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value


        queued_nights = self.queued_nights

        queued_at: None | str | Unset
        if isinstance(self.queued_at, Unset):
            queued_at = UNSET
        elif isinstance(self.queued_at, datetime.datetime):
            queued_at = self.queued_at.isoformat()
        else:
            queued_at = self.queued_at

        last_push: dict[str, Any] | None | Unset
        if isinstance(self.last_push, Unset):
            last_push = UNSET
        elif isinstance(self.last_push, GetListingCalendarSyncResponse200ChannelsItemQueueLastPushType0):
            last_push = self.last_push.to_dict()
        else:
            last_push = self.last_push


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if state is not UNSET:
            field_dict["state"] = state
        if queued_nights is not UNSET:
            field_dict["queuedNights"] = queued_nights
        if queued_at is not UNSET:
            field_dict["queuedAt"] = queued_at
        if last_push is not UNSET:
            field_dict["lastPush"] = last_push

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_listing_calendar_sync_response_200_channels_item_queue_last_push_type_0 import GetListingCalendarSyncResponse200ChannelsItemQueueLastPushType0
        d = dict(src_dict)
        _state = d.pop("state", UNSET)
        state: GetListingCalendarSyncResponse200ChannelsItemQueueState | Unset
        if isinstance(_state,  Unset):
            state = UNSET
        else:
            state = GetListingCalendarSyncResponse200ChannelsItemQueueState(_state)




        queued_nights = d.pop("queuedNights", UNSET)

        def _parse_queued_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                queued_at_type_0 = isoparse(data)



                return queued_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        queued_at = _parse_queued_at(d.pop("queuedAt", UNSET))


        def _parse_last_push(data: object) -> GetListingCalendarSyncResponse200ChannelsItemQueueLastPushType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_push_type_0 = GetListingCalendarSyncResponse200ChannelsItemQueueLastPushType0.from_dict(data)



                return last_push_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetListingCalendarSyncResponse200ChannelsItemQueueLastPushType0 | None | Unset, data)

        last_push = _parse_last_push(d.pop("lastPush", UNSET))


        get_listing_calendar_sync_response_200_channels_item_queue = cls(
            state=state,
            queued_nights=queued_nights,
            queued_at=queued_at,
            last_push=last_push,
        )


        get_listing_calendar_sync_response_200_channels_item_queue.additional_properties = d
        return get_listing_calendar_sync_response_200_channels_item_queue

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
