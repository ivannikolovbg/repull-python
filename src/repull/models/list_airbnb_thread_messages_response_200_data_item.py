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
  from ..models.conversation_message_attachment import ConversationMessageAttachment





T = TypeVar("T", bound="ListAirbnbThreadMessagesResponse200DataItem")



@_attrs_define
class ListAirbnbThreadMessagesResponse200DataItem:
    """ 
        Attributes:
            id (str | Unset): Repull message id.
            external_message_id (None | str | Unset): Airbnb's message id.
            thread_id (str | Unset): The Airbnb thread id.
            user_id (None | str | Unset): Airbnb user id of the sender.
            message (None | str | Unset): Message text. Empty for a file-only message.
            translated_message (None | str | Unset):
            channel (None | str | Unset):  Example: airbnb.
            sender_type (None | str | Unset): `guest`, `host`, `user`, `system`, …
            reservation_id (None | str | Unset):
            created_at (datetime.datetime | None | Unset):
            updated_at (datetime.datetime | None | Unset):
            external_created_at (datetime.datetime | None | Unset): When Airbnb recorded the message.
            attachments (list[ConversationMessageAttachment] | Unset):
     """

    id: str | Unset = UNSET
    external_message_id: None | str | Unset = UNSET
    thread_id: str | Unset = UNSET
    user_id: None | str | Unset = UNSET
    message: None | str | Unset = UNSET
    translated_message: None | str | Unset = UNSET
    channel: None | str | Unset = UNSET
    sender_type: None | str | Unset = UNSET
    reservation_id: None | str | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    external_created_at: datetime.datetime | None | Unset = UNSET
    attachments: list[ConversationMessageAttachment] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.conversation_message_attachment import ConversationMessageAttachment
        id = self.id

        external_message_id: None | str | Unset
        if isinstance(self.external_message_id, Unset):
            external_message_id = UNSET
        else:
            external_message_id = self.external_message_id

        thread_id = self.thread_id

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        translated_message: None | str | Unset
        if isinstance(self.translated_message, Unset):
            translated_message = UNSET
        else:
            translated_message = self.translated_message

        channel: None | str | Unset
        if isinstance(self.channel, Unset):
            channel = UNSET
        else:
            channel = self.channel

        sender_type: None | str | Unset
        if isinstance(self.sender_type, Unset):
            sender_type = UNSET
        else:
            sender_type = self.sender_type

        reservation_id: None | str | Unset
        if isinstance(self.reservation_id, Unset):
            reservation_id = UNSET
        else:
            reservation_id = self.reservation_id

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        external_created_at: None | str | Unset
        if isinstance(self.external_created_at, Unset):
            external_created_at = UNSET
        elif isinstance(self.external_created_at, datetime.datetime):
            external_created_at = self.external_created_at.isoformat()
        else:
            external_created_at = self.external_created_at

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
        if id is not UNSET:
            field_dict["id"] = id
        if external_message_id is not UNSET:
            field_dict["externalMessageId"] = external_message_id
        if thread_id is not UNSET:
            field_dict["threadId"] = thread_id
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if message is not UNSET:
            field_dict["message"] = message
        if translated_message is not UNSET:
            field_dict["translatedMessage"] = translated_message
        if channel is not UNSET:
            field_dict["channel"] = channel
        if sender_type is not UNSET:
            field_dict["senderType"] = sender_type
        if reservation_id is not UNSET:
            field_dict["reservationId"] = reservation_id
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if external_created_at is not UNSET:
            field_dict["externalCreatedAt"] = external_created_at
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

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

        external_message_id = _parse_external_message_id(d.pop("externalMessageId", UNSET))


        thread_id = d.pop("threadId", UNSET)

        def _parse_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_id = _parse_user_id(d.pop("userId", UNSET))


        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))


        def _parse_translated_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        translated_message = _parse_translated_message(d.pop("translatedMessage", UNSET))


        def _parse_channel(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        channel = _parse_channel(d.pop("channel", UNSET))


        def _parse_sender_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sender_type = _parse_sender_type(d.pop("senderType", UNSET))


        def _parse_reservation_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reservation_id = _parse_reservation_id(d.pop("reservationId", UNSET))


        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = isoparse(data)



                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("createdAt", UNSET))


        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = isoparse(data)



                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updatedAt", UNSET))


        def _parse_external_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                external_created_at_type_0 = isoparse(data)



                return external_created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        external_created_at = _parse_external_created_at(d.pop("externalCreatedAt", UNSET))


        _attachments = d.pop("attachments", UNSET)
        attachments: list[ConversationMessageAttachment] | Unset = UNSET
        if _attachments is not UNSET:
            attachments = []
            for attachments_item_data in _attachments:
                attachments_item = ConversationMessageAttachment.from_dict(attachments_item_data)



                attachments.append(attachments_item)


        list_airbnb_thread_messages_response_200_data_item = cls(
            id=id,
            external_message_id=external_message_id,
            thread_id=thread_id,
            user_id=user_id,
            message=message,
            translated_message=translated_message,
            channel=channel,
            sender_type=sender_type,
            reservation_id=reservation_id,
            created_at=created_at,
            updated_at=updated_at,
            external_created_at=external_created_at,
            attachments=attachments,
        )


        list_airbnb_thread_messages_response_200_data_item.additional_properties = d
        return list_airbnb_thread_messages_response_200_data_item

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
