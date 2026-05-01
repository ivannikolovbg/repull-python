from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.message_sender_type import MessageSenderType
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="Message")



@_attrs_define
class Message:
    """ 
        Attributes:
            id (str | Unset):
            conversation_id (str | Unset):
            sender_type (MessageSenderType | Unset):
            sender_name (str | Unset):
            message (str | Unset):
            sent_at (datetime.datetime | Unset):
     """

    id: str | Unset = UNSET
    conversation_id: str | Unset = UNSET
    sender_type: MessageSenderType | Unset = UNSET
    sender_name: str | Unset = UNSET
    message: str | Unset = UNSET
    sent_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        conversation_id = self.conversation_id

        sender_type: str | Unset = UNSET
        if not isinstance(self.sender_type, Unset):
            sender_type = self.sender_type.value


        sender_name = self.sender_name

        message = self.message

        sent_at: str | Unset = UNSET
        if not isinstance(self.sent_at, Unset):
            sent_at = self.sent_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if conversation_id is not UNSET:
            field_dict["conversationId"] = conversation_id
        if sender_type is not UNSET:
            field_dict["senderType"] = sender_type
        if sender_name is not UNSET:
            field_dict["senderName"] = sender_name
        if message is not UNSET:
            field_dict["message"] = message
        if sent_at is not UNSET:
            field_dict["sentAt"] = sent_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        conversation_id = d.pop("conversationId", UNSET)

        _sender_type = d.pop("senderType", UNSET)
        sender_type: MessageSenderType | Unset
        if isinstance(_sender_type,  Unset):
            sender_type = UNSET
        else:
            sender_type = MessageSenderType(_sender_type)




        sender_name = d.pop("senderName", UNSET)

        message = d.pop("message", UNSET)

        _sent_at = d.pop("sentAt", UNSET)
        sent_at: datetime.datetime | Unset
        if isinstance(_sent_at,  Unset):
            sent_at = UNSET
        else:
            sent_at = isoparse(_sent_at)




        message = cls(
            id=id,
            conversation_id=conversation_id,
            sender_type=sender_type,
            sender_name=sender_name,
            message=message,
            sent_at=sent_at,
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
