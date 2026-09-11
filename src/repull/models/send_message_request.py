from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.send_message_request_channel import SendMessageRequestChannel
from ..types import UNSET, Unset






T = TypeVar("T", bound="SendMessageRequest")



@_attrs_define
class SendMessageRequest:
    """ 
        Attributes:
            message (str): The text to send the guest. Example: Your check-in details are ready — the door code is active
                from 16:00..
            channel (SendMessageRequestChannel | Unset): Force a channel. Omit to send on whichever channel the conversation
                already uses, which is the right default.
     """

    message: str
    channel: SendMessageRequestChannel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        message = self.message

        channel: str | Unset = UNSET
        if not isinstance(self.channel, Unset):
            channel = self.channel.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "message": message,
        })
        if channel is not UNSET:
            field_dict["channel"] = channel

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message")

        _channel = d.pop("channel", UNSET)
        channel: SendMessageRequestChannel | Unset
        if isinstance(_channel,  Unset):
            channel = UNSET
        else:
            channel = SendMessageRequestChannel(_channel)




        send_message_request = cls(
            message=message,
            channel=channel,
        )


        send_message_request.additional_properties = d
        return send_message_request

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
