from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.listing_publish_status_channel_push_status import ListingPublishStatusChannelPushStatus
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="ListingPublishStatusChannel")



@_attrs_define
class ListingPublishStatusChannel:
    """ 
        Attributes:
            platform (str | Unset):  Example: airbnb.
            push_status (ListingPublishStatusChannelPushStatus | Unset):
            last_pushed_at (datetime.datetime | None | Unset):
            last_pulled_at (datetime.datetime | None | Unset):
            dirty_fields (list[str] | Unset):
            platform_has_changes (bool | Unset):
     """

    platform: str | Unset = UNSET
    push_status: ListingPublishStatusChannelPushStatus | Unset = UNSET
    last_pushed_at: datetime.datetime | None | Unset = UNSET
    last_pulled_at: datetime.datetime | None | Unset = UNSET
    dirty_fields: list[str] | Unset = UNSET
    platform_has_changes: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        platform = self.platform

        push_status: str | Unset = UNSET
        if not isinstance(self.push_status, Unset):
            push_status = self.push_status.value


        last_pushed_at: None | str | Unset
        if isinstance(self.last_pushed_at, Unset):
            last_pushed_at = UNSET
        elif isinstance(self.last_pushed_at, datetime.datetime):
            last_pushed_at = self.last_pushed_at.isoformat()
        else:
            last_pushed_at = self.last_pushed_at

        last_pulled_at: None | str | Unset
        if isinstance(self.last_pulled_at, Unset):
            last_pulled_at = UNSET
        elif isinstance(self.last_pulled_at, datetime.datetime):
            last_pulled_at = self.last_pulled_at.isoformat()
        else:
            last_pulled_at = self.last_pulled_at

        dirty_fields: list[str] | Unset = UNSET
        if not isinstance(self.dirty_fields, Unset):
            dirty_fields = self.dirty_fields



        platform_has_changes = self.platform_has_changes


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if platform is not UNSET:
            field_dict["platform"] = platform
        if push_status is not UNSET:
            field_dict["pushStatus"] = push_status
        if last_pushed_at is not UNSET:
            field_dict["lastPushedAt"] = last_pushed_at
        if last_pulled_at is not UNSET:
            field_dict["lastPulledAt"] = last_pulled_at
        if dirty_fields is not UNSET:
            field_dict["dirtyFields"] = dirty_fields
        if platform_has_changes is not UNSET:
            field_dict["platformHasChanges"] = platform_has_changes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        platform = d.pop("platform", UNSET)

        _push_status = d.pop("pushStatus", UNSET)
        push_status: ListingPublishStatusChannelPushStatus | Unset
        if isinstance(_push_status,  Unset):
            push_status = UNSET
        else:
            push_status = ListingPublishStatusChannelPushStatus(_push_status)




        def _parse_last_pushed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_pushed_at_type_0 = isoparse(data)



                return last_pushed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_pushed_at = _parse_last_pushed_at(d.pop("lastPushedAt", UNSET))


        def _parse_last_pulled_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_pulled_at_type_0 = isoparse(data)



                return last_pulled_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_pulled_at = _parse_last_pulled_at(d.pop("lastPulledAt", UNSET))


        dirty_fields = cast(list[str], d.pop("dirtyFields", UNSET))


        platform_has_changes = d.pop("platformHasChanges", UNSET)

        listing_publish_status_channel = cls(
            platform=platform,
            push_status=push_status,
            last_pushed_at=last_pushed_at,
            last_pulled_at=last_pulled_at,
            dirty_fields=dirty_fields,
            platform_has_changes=platform_has_changes,
        )


        listing_publish_status_channel.additional_properties = d
        return listing_publish_status_channel

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
