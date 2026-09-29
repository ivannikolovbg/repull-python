from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_listing_calendar_sync_response_200_channels_item_queue_last_push_type_0_result import GetListingCalendarSyncResponse200ChannelsItemQueueLastPushType0Result
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="GetListingCalendarSyncResponse200ChannelsItemQueueLastPushType0")



@_attrs_define
class GetListingCalendarSyncResponse200ChannelsItemQueueLastPushType0:
    """ 
        Attributes:
            finished_at (datetime.datetime | None | Unset):
            result (GetListingCalendarSyncResponse200ChannelsItemQueueLastPushType0Result | Unset): `skipped` — not sent
                because the unit is not live on VRBO (`reason`).
            reason (None | str | Unset):
            nights (int | Unset): Nights the push covered.
            prices_changed (int | Unset):
            min_stays_changed (int | Unset):
            blocks_created (int | Unset):
            blocks_removed (int | Unset):
            calls (int | Unset): VRBO calls made — only what differed was sent.
            nights_differing (int | Unset): Nights VRBO still showed differently after the push (they are retried).
     """

    finished_at: datetime.datetime | None | Unset = UNSET
    result: GetListingCalendarSyncResponse200ChannelsItemQueueLastPushType0Result | Unset = UNSET
    reason: None | str | Unset = UNSET
    nights: int | Unset = UNSET
    prices_changed: int | Unset = UNSET
    min_stays_changed: int | Unset = UNSET
    blocks_created: int | Unset = UNSET
    blocks_removed: int | Unset = UNSET
    calls: int | Unset = UNSET
    nights_differing: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        finished_at: None | str | Unset
        if isinstance(self.finished_at, Unset):
            finished_at = UNSET
        elif isinstance(self.finished_at, datetime.datetime):
            finished_at = self.finished_at.isoformat()
        else:
            finished_at = self.finished_at

        result: str | Unset = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.value


        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        nights = self.nights

        prices_changed = self.prices_changed

        min_stays_changed = self.min_stays_changed

        blocks_created = self.blocks_created

        blocks_removed = self.blocks_removed

        calls = self.calls

        nights_differing = self.nights_differing


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if finished_at is not UNSET:
            field_dict["finishedAt"] = finished_at
        if result is not UNSET:
            field_dict["result"] = result
        if reason is not UNSET:
            field_dict["reason"] = reason
        if nights is not UNSET:
            field_dict["nights"] = nights
        if prices_changed is not UNSET:
            field_dict["pricesChanged"] = prices_changed
        if min_stays_changed is not UNSET:
            field_dict["minStaysChanged"] = min_stays_changed
        if blocks_created is not UNSET:
            field_dict["blocksCreated"] = blocks_created
        if blocks_removed is not UNSET:
            field_dict["blocksRemoved"] = blocks_removed
        if calls is not UNSET:
            field_dict["calls"] = calls
        if nights_differing is not UNSET:
            field_dict["nightsDiffering"] = nights_differing

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_finished_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                finished_at_type_0 = isoparse(data)



                return finished_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        finished_at = _parse_finished_at(d.pop("finishedAt", UNSET))


        _result = d.pop("result", UNSET)
        result: GetListingCalendarSyncResponse200ChannelsItemQueueLastPushType0Result | Unset
        if isinstance(_result,  Unset):
            result = UNSET
        else:
            result = GetListingCalendarSyncResponse200ChannelsItemQueueLastPushType0Result(_result)




        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))


        nights = d.pop("nights", UNSET)

        prices_changed = d.pop("pricesChanged", UNSET)

        min_stays_changed = d.pop("minStaysChanged", UNSET)

        blocks_created = d.pop("blocksCreated", UNSET)

        blocks_removed = d.pop("blocksRemoved", UNSET)

        calls = d.pop("calls", UNSET)

        nights_differing = d.pop("nightsDiffering", UNSET)

        get_listing_calendar_sync_response_200_channels_item_queue_last_push_type_0 = cls(
            finished_at=finished_at,
            result=result,
            reason=reason,
            nights=nights,
            prices_changed=prices_changed,
            min_stays_changed=min_stays_changed,
            blocks_created=blocks_created,
            blocks_removed=blocks_removed,
            calls=calls,
            nights_differing=nights_differing,
        )


        get_listing_calendar_sync_response_200_channels_item_queue_last_push_type_0.additional_properties = d
        return get_listing_calendar_sync_response_200_channels_item_queue_last_push_type_0

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
