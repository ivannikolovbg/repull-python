from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.send_message_request_channel import SendMessageRequestChannel
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.send_message_attachment import SendMessageAttachment





T = TypeVar("T", bound="SendMessageRequest")



@_attrs_define
class SendMessageRequest:
    """ `message`, `attachments`, or both. Per-channel limits for `attachments`:

    | Channel | Accepted types | Per file | Per request | Text |
    |---|---|---|---|---|
    | Airbnb | JPEG, PNG, GIF, WebP (sent as JPEG), MP4, QuickTime | 10 MB | 5 | optional — each file is sent as its own
    message, then the text |
    | Booking.com | JPEG, PNG | 10 MB | 5 | **required** — all files ride on the one text message |
    | SMS, email, direct-booking site chat | — | — | — | `422 attachments_not_supported`; nothing is sent |

        Attributes:
            message (str | Unset): The text to send the guest. Required unless `attachments` is present. Example: Here is
                the parking map — the gate code is 4821..
            channel (SendMessageRequestChannel | Unset): Force a channel. Omit to send on whichever channel the conversation
                already uses, which is the right default.
            attachments (list[SendMessageAttachment] | Unset): Files to send. See the per-channel table above.
     """

    message: str | Unset = UNSET
    channel: SendMessageRequestChannel | Unset = UNSET
    attachments: list[SendMessageAttachment] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.send_message_attachment import SendMessageAttachment
        message = self.message

        channel: str | Unset = UNSET
        if not isinstance(self.channel, Unset):
            channel = self.channel.value


        attachments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if message is not UNSET:
            field_dict["message"] = message
        if channel is not UNSET:
            field_dict["channel"] = channel
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.send_message_attachment import SendMessageAttachment
        d = dict(src_dict)
        message = d.pop("message", UNSET)

        _channel = d.pop("channel", UNSET)
        channel: SendMessageRequestChannel | Unset
        if isinstance(_channel,  Unset):
            channel = UNSET
        else:
            channel = SendMessageRequestChannel(_channel)




        _attachments = d.pop("attachments", UNSET)
        attachments: list[SendMessageAttachment] | Unset = UNSET
        if _attachments is not UNSET:
            attachments = []
            for attachments_item_data in _attachments:
                attachments_item = SendMessageAttachment.from_dict(attachments_item_data)



                attachments.append(attachments_item)


        send_message_request = cls(
            message=message,
            channel=channel,
            attachments=attachments,
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
