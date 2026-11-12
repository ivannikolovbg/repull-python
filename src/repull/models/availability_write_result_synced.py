from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.availability_write_result_synced_channels_item import AvailabilityWriteResultSyncedChannelsItem





T = TypeVar("T", bound="AvailabilityWriteResultSynced")



@_attrs_define
class AvailabilityWriteResultSynced:
    """ Per-channel push outcome. A partial failure is surfaced, not swallowed: "saved locally but the channel rejected it"
    is precisely the state a caller must know about.

        Attributes:
            attempted (int | Unset):
            succeeded (int | Unset):
            failed (int | Unset):
            auth_errors (int | Unset): Channels whose token has expired — these need reconnecting, not retrying.
            channels (list[AvailabilityWriteResultSyncedChannelsItem] | Unset): One entry per listing per connected channel:
                which channel took the write and which refused it.
     """

    attempted: int | Unset = UNSET
    succeeded: int | Unset = UNSET
    failed: int | Unset = UNSET
    auth_errors: int | Unset = UNSET
    channels: list[AvailabilityWriteResultSyncedChannelsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.availability_write_result_synced_channels_item import AvailabilityWriteResultSyncedChannelsItem
        attempted = self.attempted

        succeeded = self.succeeded

        failed = self.failed

        auth_errors = self.auth_errors

        channels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.channels, Unset):
            channels = []
            for channels_item_data in self.channels:
                channels_item = channels_item_data.to_dict()
                channels.append(channels_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if attempted is not UNSET:
            field_dict["attempted"] = attempted
        if succeeded is not UNSET:
            field_dict["succeeded"] = succeeded
        if failed is not UNSET:
            field_dict["failed"] = failed
        if auth_errors is not UNSET:
            field_dict["authErrors"] = auth_errors
        if channels is not UNSET:
            field_dict["channels"] = channels

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.availability_write_result_synced_channels_item import AvailabilityWriteResultSyncedChannelsItem
        d = dict(src_dict)
        attempted = d.pop("attempted", UNSET)

        succeeded = d.pop("succeeded", UNSET)

        failed = d.pop("failed", UNSET)

        auth_errors = d.pop("authErrors", UNSET)

        _channels = d.pop("channels", UNSET)
        channels: list[AvailabilityWriteResultSyncedChannelsItem] | Unset = UNSET
        if _channels is not UNSET:
            channels = []
            for channels_item_data in _channels:
                channels_item = AvailabilityWriteResultSyncedChannelsItem.from_dict(channels_item_data)



                channels.append(channels_item)


        availability_write_result_synced = cls(
            attempted=attempted,
            succeeded=succeeded,
            failed=failed,
            auth_errors=auth_errors,
            channels=channels,
        )


        availability_write_result_synced.additional_properties = d
        return availability_write_result_synced

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
