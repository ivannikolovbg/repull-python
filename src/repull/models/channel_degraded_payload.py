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
  from ..models.channel_degraded_payload_object import ChannelDegradedPayloadObject





T = TypeVar("T", bound="ChannelDegradedPayload")



@_attrs_define
class ChannelDegradedPayload:
    """ Payload for `channel.degraded`. A connection is failing repeatedly and will stop working. Sent on the transition
    into degraded or down, not on every health check.

        Attributes:
            object_ (ChannelDegradedPayloadObject):
            occurred_at (datetime.datetime | Unset):
     """

    object_: ChannelDegradedPayloadObject
    occurred_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.channel_degraded_payload_object import ChannelDegradedPayloadObject
        object_ = self.object_.to_dict()

        occurred_at: str | Unset = UNSET
        if not isinstance(self.occurred_at, Unset):
            occurred_at = self.occurred_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "object": object_,
        })
        if occurred_at is not UNSET:
            field_dict["occurredAt"] = occurred_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.channel_degraded_payload_object import ChannelDegradedPayloadObject
        d = dict(src_dict)
        object_ = ChannelDegradedPayloadObject.from_dict(d.pop("object"))




        _occurred_at = d.pop("occurredAt", UNSET)
        occurred_at: datetime.datetime | Unset
        if isinstance(_occurred_at,  Unset):
            occurred_at = UNSET
        else:
            occurred_at = isoparse(_occurred_at)




        channel_degraded_payload = cls(
            object_=object_,
            occurred_at=occurred_at,
        )


        channel_degraded_payload.additional_properties = d
        return channel_degraded_payload

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
