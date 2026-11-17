from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_listing_calendar_sync_response_200_channels_item_off_reason import GetListingCalendarSyncResponse200ChannelsItemOffReason
from ..models.get_listing_calendar_sync_response_200_channels_item_status import GetListingCalendarSyncResponse200ChannelsItemStatus
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.get_listing_calendar_sync_response_200_channels_item_problems_item import GetListingCalendarSyncResponse200ChannelsItemProblemsItem
  from ..models.get_listing_calendar_sync_response_200_channels_item_queue import GetListingCalendarSyncResponse200ChannelsItemQueue





T = TypeVar("T", bound="GetListingCalendarSyncResponse200ChannelsItem")



@_attrs_define
class GetListingCalendarSyncResponse200ChannelsItem:
    """ 
        Attributes:
            channel (str):  Example: vrbo.
            platform_id (None | str): The listing's id on the channel. Example: 5121372.
            sync_enabled (bool): Calendar pushes to this channel are on.
            status (GetListingCalendarSyncResponse200ChannelsItemStatus): `in_sync` — no future night has a problem;
                `problems` — see `problems`; `off` — calendar sync is off for this channel.
            last_sync_at (datetime.datetime | None): When a push last wrote to this listing's calendar.
            nights_with_problems (int):
            problems (list[GetListingCalendarSyncResponse200ChannelsItemProblemsItem]):
            off_reason (GetListingCalendarSyncResponse200ChannelsItemOffReason | Unset): Vrbo only, when Repull turned
                calendar sync off: Vrbo says another tool (such as a PMS) manages the account's calendar. Absent when the host
                turned it off.
            docs_url (str | Unset): Explains `offReason` and how to turn calendar sync back on.
            queue (GetListingCalendarSyncResponse200ChannelsItemQueue | Unset): VRBO only — the paced push queue.
     """

    channel: str
    platform_id: None | str
    sync_enabled: bool
    status: GetListingCalendarSyncResponse200ChannelsItemStatus
    last_sync_at: datetime.datetime | None
    nights_with_problems: int
    problems: list[GetListingCalendarSyncResponse200ChannelsItemProblemsItem]
    off_reason: GetListingCalendarSyncResponse200ChannelsItemOffReason | Unset = UNSET
    docs_url: str | Unset = UNSET
    queue: GetListingCalendarSyncResponse200ChannelsItemQueue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_listing_calendar_sync_response_200_channels_item_problems_item import GetListingCalendarSyncResponse200ChannelsItemProblemsItem
        from ..models.get_listing_calendar_sync_response_200_channels_item_queue import GetListingCalendarSyncResponse200ChannelsItemQueue
        channel = self.channel

        platform_id: None | str
        platform_id = self.platform_id

        sync_enabled = self.sync_enabled

        status = self.status.value

        last_sync_at: None | str
        if isinstance(self.last_sync_at, datetime.datetime):
            last_sync_at = self.last_sync_at.isoformat()
        else:
            last_sync_at = self.last_sync_at

        nights_with_problems = self.nights_with_problems

        problems = []
        for problems_item_data in self.problems:
            problems_item = problems_item_data.to_dict()
            problems.append(problems_item)



        off_reason: str | Unset = UNSET
        if not isinstance(self.off_reason, Unset):
            off_reason = self.off_reason.value


        docs_url = self.docs_url

        queue: dict[str, Any] | Unset = UNSET
        if not isinstance(self.queue, Unset):
            queue = self.queue.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "channel": channel,
            "platformId": platform_id,
            "syncEnabled": sync_enabled,
            "status": status,
            "lastSyncAt": last_sync_at,
            "nightsWithProblems": nights_with_problems,
            "problems": problems,
        })
        if off_reason is not UNSET:
            field_dict["offReason"] = off_reason
        if docs_url is not UNSET:
            field_dict["docsUrl"] = docs_url
        if queue is not UNSET:
            field_dict["queue"] = queue

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_listing_calendar_sync_response_200_channels_item_problems_item import GetListingCalendarSyncResponse200ChannelsItemProblemsItem
        from ..models.get_listing_calendar_sync_response_200_channels_item_queue import GetListingCalendarSyncResponse200ChannelsItemQueue
        d = dict(src_dict)
        channel = d.pop("channel")

        def _parse_platform_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        platform_id = _parse_platform_id(d.pop("platformId"))


        sync_enabled = d.pop("syncEnabled")

        status = GetListingCalendarSyncResponse200ChannelsItemStatus(d.pop("status"))




        def _parse_last_sync_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_sync_at_type_0 = isoparse(data)



                return last_sync_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_sync_at = _parse_last_sync_at(d.pop("lastSyncAt"))


        nights_with_problems = d.pop("nightsWithProblems")

        problems = []
        _problems = d.pop("problems")
        for problems_item_data in (_problems):
            problems_item = GetListingCalendarSyncResponse200ChannelsItemProblemsItem.from_dict(problems_item_data)



            problems.append(problems_item)


        _off_reason = d.pop("offReason", UNSET)
        off_reason: GetListingCalendarSyncResponse200ChannelsItemOffReason | Unset
        if isinstance(_off_reason,  Unset):
            off_reason = UNSET
        else:
            off_reason = GetListingCalendarSyncResponse200ChannelsItemOffReason(_off_reason)




        docs_url = d.pop("docsUrl", UNSET)

        _queue = d.pop("queue", UNSET)
        queue: GetListingCalendarSyncResponse200ChannelsItemQueue | Unset
        if isinstance(_queue,  Unset):
            queue = UNSET
        else:
            queue = GetListingCalendarSyncResponse200ChannelsItemQueue.from_dict(_queue)




        get_listing_calendar_sync_response_200_channels_item = cls(
            channel=channel,
            platform_id=platform_id,
            sync_enabled=sync_enabled,
            status=status,
            last_sync_at=last_sync_at,
            nights_with_problems=nights_with_problems,
            problems=problems,
            off_reason=off_reason,
            docs_url=docs_url,
            queue=queue,
        )


        get_listing_calendar_sync_response_200_channels_item.additional_properties = d
        return get_listing_calendar_sync_response_200_channels_item

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
