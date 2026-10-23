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

if TYPE_CHECKING:
  from ..models.channel_sync_failure_payload_failures_item import ChannelSyncFailurePayloadFailuresItem
  from ..models.channel_sync_failure_payload_object import ChannelSyncFailurePayloadObject





T = TypeVar("T", bound="ChannelSyncFailurePayload")



@_attrs_define
class ChannelSyncFailurePayload:
    """ Payload for `channel.sync.failed`. A push of availability, rates or content to a connected channel did not land.

        Attributes:
            object_ (ChannelSyncFailurePayloadObject):
            failures (list[ChannelSyncFailurePayloadFailuresItem]): One entry per channel mapping that refused the push.
            reservation_id (int | None | Unset): Set when the push was blocking dates for a booking just taken. Those nights
                are sold on one channel and still open on another — treat as urgent.
            occurred_at (datetime.datetime | Unset):
     """

    object_: ChannelSyncFailurePayloadObject
    failures: list[ChannelSyncFailurePayloadFailuresItem]
    reservation_id: int | None | Unset = UNSET
    occurred_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.channel_sync_failure_payload_failures_item import ChannelSyncFailurePayloadFailuresItem
        from ..models.channel_sync_failure_payload_object import ChannelSyncFailurePayloadObject
        object_ = self.object_.to_dict()

        failures = []
        for failures_item_data in self.failures:
            failures_item = failures_item_data.to_dict()
            failures.append(failures_item)



        reservation_id: int | None | Unset
        if isinstance(self.reservation_id, Unset):
            reservation_id = UNSET
        else:
            reservation_id = self.reservation_id

        occurred_at: str | Unset = UNSET
        if not isinstance(self.occurred_at, Unset):
            occurred_at = self.occurred_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "object": object_,
            "failures": failures,
        })
        if reservation_id is not UNSET:
            field_dict["reservationId"] = reservation_id
        if occurred_at is not UNSET:
            field_dict["occurredAt"] = occurred_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.channel_sync_failure_payload_failures_item import ChannelSyncFailurePayloadFailuresItem
        from ..models.channel_sync_failure_payload_object import ChannelSyncFailurePayloadObject
        d = dict(src_dict)
        object_ = ChannelSyncFailurePayloadObject.from_dict(d.pop("object"))




        failures = []
        _failures = d.pop("failures")
        for failures_item_data in (_failures):
            failures_item = ChannelSyncFailurePayloadFailuresItem.from_dict(failures_item_data)



            failures.append(failures_item)


        def _parse_reservation_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        reservation_id = _parse_reservation_id(d.pop("reservationId", UNSET))


        _occurred_at = d.pop("occurredAt", UNSET)
        occurred_at: datetime.datetime | Unset
        if isinstance(_occurred_at,  Unset):
            occurred_at = UNSET
        else:
            occurred_at = isoparse(_occurred_at)




        channel_sync_failure_payload = cls(
            object_=object_,
            failures=failures,
            reservation_id=reservation_id,
            occurred_at=occurred_at,
        )


        channel_sync_failure_payload.additional_properties = d
        return channel_sync_failure_payload

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
