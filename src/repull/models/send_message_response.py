from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.send_message_response_direction import SendMessageResponseDirection
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="SendMessageResponse")



@_attrs_define
class SendMessageResponse:
    """ 
        Attributes:
            id (None | str | Unset): Repull message id for the row that was recorded.
            conversation_id (int | Unset):
            external_message_id (None | str | Unset): The channel's own message id, when it returns one.
            channel (None | str | Unset): The channel the message actually went out on.
            status (str | Unset):  Example: sent.
            direction (SendMessageResponseDirection | Unset):
            content_rewritten (bool | Unset): TRUE when the channel altered the text before delivery — today that means
                Airbnb stripped a link, an email address or a phone number and the remainder was re-sent. When true, the guest
                did NOT receive `submittedContent`; they received `deliveredContent`.
            submitted_content (None | str | Unset): The text you sent.
            delivered_content (None | str | Unset): The text the guest actually received. Differs from `submittedContent`
                exactly when `contentRewritten` is true.
            status_reason (None | str | Unset): The channel's verbatim note, when it gave one — including the refusal that
                triggered a rewrite.
     """

    id: None | str | Unset = UNSET
    conversation_id: int | Unset = UNSET
    external_message_id: None | str | Unset = UNSET
    channel: None | str | Unset = UNSET
    status: str | Unset = UNSET
    direction: SendMessageResponseDirection | Unset = UNSET
    content_rewritten: bool | Unset = UNSET
    submitted_content: None | str | Unset = UNSET
    delivered_content: None | str | Unset = UNSET
    status_reason: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        conversation_id = self.conversation_id

        external_message_id: None | str | Unset
        if isinstance(self.external_message_id, Unset):
            external_message_id = UNSET
        else:
            external_message_id = self.external_message_id

        channel: None | str | Unset
        if isinstance(self.channel, Unset):
            channel = UNSET
        else:
            channel = self.channel

        status = self.status

        direction: str | Unset = UNSET
        if not isinstance(self.direction, Unset):
            direction = self.direction.value


        content_rewritten = self.content_rewritten

        submitted_content: None | str | Unset
        if isinstance(self.submitted_content, Unset):
            submitted_content = UNSET
        else:
            submitted_content = self.submitted_content

        delivered_content: None | str | Unset
        if isinstance(self.delivered_content, Unset):
            delivered_content = UNSET
        else:
            delivered_content = self.delivered_content

        status_reason: None | str | Unset
        if isinstance(self.status_reason, Unset):
            status_reason = UNSET
        else:
            status_reason = self.status_reason


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if conversation_id is not UNSET:
            field_dict["conversationId"] = conversation_id
        if external_message_id is not UNSET:
            field_dict["externalMessageId"] = external_message_id
        if channel is not UNSET:
            field_dict["channel"] = channel
        if status is not UNSET:
            field_dict["status"] = status
        if direction is not UNSET:
            field_dict["direction"] = direction
        if content_rewritten is not UNSET:
            field_dict["contentRewritten"] = content_rewritten
        if submitted_content is not UNSET:
            field_dict["submittedContent"] = submitted_content
        if delivered_content is not UNSET:
            field_dict["deliveredContent"] = delivered_content
        if status_reason is not UNSET:
            field_dict["statusReason"] = status_reason

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))


        conversation_id = d.pop("conversationId", UNSET)

        def _parse_external_message_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_message_id = _parse_external_message_id(d.pop("externalMessageId", UNSET))


        def _parse_channel(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        channel = _parse_channel(d.pop("channel", UNSET))


        status = d.pop("status", UNSET)

        _direction = d.pop("direction", UNSET)
        direction: SendMessageResponseDirection | Unset
        if isinstance(_direction,  Unset):
            direction = UNSET
        else:
            direction = SendMessageResponseDirection(_direction)




        content_rewritten = d.pop("contentRewritten", UNSET)

        def _parse_submitted_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        submitted_content = _parse_submitted_content(d.pop("submittedContent", UNSET))


        def _parse_delivered_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        delivered_content = _parse_delivered_content(d.pop("deliveredContent", UNSET))


        def _parse_status_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status_reason = _parse_status_reason(d.pop("statusReason", UNSET))


        send_message_response = cls(
            id=id,
            conversation_id=conversation_id,
            external_message_id=external_message_id,
            channel=channel,
            status=status,
            direction=direction,
            content_rewritten=content_rewritten,
            submitted_content=submitted_content,
            delivered_content=delivered_content,
            status_reason=status_reason,
        )


        send_message_response.additional_properties = d
        return send_message_response

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
