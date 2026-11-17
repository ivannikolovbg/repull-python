from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.conversation_message_status_changed_payload_status import ConversationMessageStatusChangedPayloadStatus
from typing import cast






T = TypeVar("T", bound="ConversationMessageStatusChangedPayload")



@_attrs_define
class ConversationMessageStatusChangedPayload:
    """ Payload for `conversation.message.status_changed`: a message you sent changed delivery status after the send call
    returned — a Vrbo reply accepted as `queued` (`202`) was delivered (`sent`) or gave up (`failed`).

        Attributes:
            conversation_id (str): The conversation (`GET /v1/conversations/{id}`). Example: 549555.
            message_id (str): The message, as `id` on the send response and on `GET /v1/conversations/{id}/messages`.
                Example: 1861207.
            status (ConversationMessageStatusChangedPayloadStatus): The new delivery status.
            status_reason (None | str): Why it `failed`, in plain words. `null` when `sent`.
     """

    conversation_id: str
    message_id: str
    status: ConversationMessageStatusChangedPayloadStatus
    status_reason: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        conversation_id = self.conversation_id

        message_id = self.message_id

        status = self.status.value

        status_reason: None | str
        status_reason = self.status_reason


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "conversationId": conversation_id,
            "messageId": message_id,
            "status": status,
            "statusReason": status_reason,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        conversation_id = d.pop("conversationId")

        message_id = d.pop("messageId")

        status = ConversationMessageStatusChangedPayloadStatus(d.pop("status"))




        def _parse_status_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        status_reason = _parse_status_reason(d.pop("statusReason"))


        conversation_message_status_changed_payload = cls(
            conversation_id=conversation_id,
            message_id=message_id,
            status=status,
            status_reason=status_reason,
        )


        conversation_message_status_changed_payload.additional_properties = d
        return conversation_message_status_changed_payload

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
