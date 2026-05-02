from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.message_direction import MessageDirection
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.conversation_message_attachment import ConversationMessageAttachment





T = TypeVar("T", bound="Message")



@_attrs_define
class Message:
    """ A single message inside a conversation thread. Returned by `GET /v1/conversations/{id}/messages`. `direction` is
    normalized to `inbound` (from the guest) / `outbound` (from the host or an automation).

        Attributes:
            id (int | Unset):
            external_message_id (None | str | Unset): ID assigned by the source channel (Airbnb message id, Booking message
                id, etc.). Stable across syncs.
            direction (MessageDirection | Unset):
            sender_type (None | str | Unset): Free-form sender role from the channel (e.g. `guest`, `host`, `system`,
                `airbnb`). Use `direction` for binary inbound/outbound logic.
            sender_name (str | Unset):
            sender_avatar (None | str | Unset):
            channel (None | str | Unset): Delivery channel — `airbnb`, `booking`, `sms`, `email`, etc.
            body (str | Unset): Message body in the original language.
            translated_body (None | str | Unset): English translation when the original language is non-English and a
                translation has been computed.
            attachments (list[ConversationMessageAttachment] | Unset):
            is_automated (bool | Unset): `true` when the message was sent by a Vanio automation (template, schedule, etc.).
            ai_generated (bool | Unset): `true` when the body was authored by Vanio AI (autopilot, draft).
            sent_at (datetime.datetime | Unset):
            delivered_at (datetime.datetime | Unset):
            read_at (datetime.datetime | None | Unset):
     """

    id: int | Unset = UNSET
    external_message_id: None | str | Unset = UNSET
    direction: MessageDirection | Unset = UNSET
    sender_type: None | str | Unset = UNSET
    sender_name: str | Unset = UNSET
    sender_avatar: None | str | Unset = UNSET
    channel: None | str | Unset = UNSET
    body: str | Unset = UNSET
    translated_body: None | str | Unset = UNSET
    attachments: list[ConversationMessageAttachment] | Unset = UNSET
    is_automated: bool | Unset = UNSET
    ai_generated: bool | Unset = UNSET
    sent_at: datetime.datetime | Unset = UNSET
    delivered_at: datetime.datetime | Unset = UNSET
    read_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.conversation_message_attachment import ConversationMessageAttachment
        id = self.id

        external_message_id: None | str | Unset
        if isinstance(self.external_message_id, Unset):
            external_message_id = UNSET
        else:
            external_message_id = self.external_message_id

        direction: str | Unset = UNSET
        if not isinstance(self.direction, Unset):
            direction = self.direction.value


        sender_type: None | str | Unset
        if isinstance(self.sender_type, Unset):
            sender_type = UNSET
        else:
            sender_type = self.sender_type

        sender_name = self.sender_name

        sender_avatar: None | str | Unset
        if isinstance(self.sender_avatar, Unset):
            sender_avatar = UNSET
        else:
            sender_avatar = self.sender_avatar

        channel: None | str | Unset
        if isinstance(self.channel, Unset):
            channel = UNSET
        else:
            channel = self.channel

        body = self.body

        translated_body: None | str | Unset
        if isinstance(self.translated_body, Unset):
            translated_body = UNSET
        else:
            translated_body = self.translated_body

        attachments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)



        is_automated = self.is_automated

        ai_generated = self.ai_generated

        sent_at: str | Unset = UNSET
        if not isinstance(self.sent_at, Unset):
            sent_at = self.sent_at.isoformat()

        delivered_at: str | Unset = UNSET
        if not isinstance(self.delivered_at, Unset):
            delivered_at = self.delivered_at.isoformat()

        read_at: None | str | Unset
        if isinstance(self.read_at, Unset):
            read_at = UNSET
        elif isinstance(self.read_at, datetime.datetime):
            read_at = self.read_at.isoformat()
        else:
            read_at = self.read_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if external_message_id is not UNSET:
            field_dict["external_message_id"] = external_message_id
        if direction is not UNSET:
            field_dict["direction"] = direction
        if sender_type is not UNSET:
            field_dict["sender_type"] = sender_type
        if sender_name is not UNSET:
            field_dict["sender_name"] = sender_name
        if sender_avatar is not UNSET:
            field_dict["sender_avatar"] = sender_avatar
        if channel is not UNSET:
            field_dict["channel"] = channel
        if body is not UNSET:
            field_dict["body"] = body
        if translated_body is not UNSET:
            field_dict["translated_body"] = translated_body
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if is_automated is not UNSET:
            field_dict["is_automated"] = is_automated
        if ai_generated is not UNSET:
            field_dict["ai_generated"] = ai_generated
        if sent_at is not UNSET:
            field_dict["sent_at"] = sent_at
        if delivered_at is not UNSET:
            field_dict["delivered_at"] = delivered_at
        if read_at is not UNSET:
            field_dict["read_at"] = read_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conversation_message_attachment import ConversationMessageAttachment
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_external_message_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_message_id = _parse_external_message_id(d.pop("external_message_id", UNSET))


        _direction = d.pop("direction", UNSET)
        direction: MessageDirection | Unset
        if isinstance(_direction,  Unset):
            direction = UNSET
        else:
            direction = MessageDirection(_direction)




        def _parse_sender_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sender_type = _parse_sender_type(d.pop("sender_type", UNSET))


        sender_name = d.pop("sender_name", UNSET)

        def _parse_sender_avatar(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sender_avatar = _parse_sender_avatar(d.pop("sender_avatar", UNSET))


        def _parse_channel(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        channel = _parse_channel(d.pop("channel", UNSET))


        body = d.pop("body", UNSET)

        def _parse_translated_body(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        translated_body = _parse_translated_body(d.pop("translated_body", UNSET))


        _attachments = d.pop("attachments", UNSET)
        attachments: list[ConversationMessageAttachment] | Unset = UNSET
        if _attachments is not UNSET:
            attachments = []
            for attachments_item_data in _attachments:
                attachments_item = ConversationMessageAttachment.from_dict(attachments_item_data)



                attachments.append(attachments_item)


        is_automated = d.pop("is_automated", UNSET)

        ai_generated = d.pop("ai_generated", UNSET)

        _sent_at = d.pop("sent_at", UNSET)
        sent_at: datetime.datetime | Unset
        if isinstance(_sent_at,  Unset):
            sent_at = UNSET
        else:
            sent_at = isoparse(_sent_at)




        _delivered_at = d.pop("delivered_at", UNSET)
        delivered_at: datetime.datetime | Unset
        if isinstance(_delivered_at,  Unset):
            delivered_at = UNSET
        else:
            delivered_at = isoparse(_delivered_at)




        def _parse_read_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                read_at_type_0 = isoparse(data)



                return read_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        read_at = _parse_read_at(d.pop("read_at", UNSET))


        message = cls(
            id=id,
            external_message_id=external_message_id,
            direction=direction,
            sender_type=sender_type,
            sender_name=sender_name,
            sender_avatar=sender_avatar,
            channel=channel,
            body=body,
            translated_body=translated_body,
            attachments=attachments,
            is_automated=is_automated,
            ai_generated=ai_generated,
            sent_at=sent_at,
            delivered_at=delivered_at,
            read_at=read_at,
        )


        message.additional_properties = d
        return message

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
