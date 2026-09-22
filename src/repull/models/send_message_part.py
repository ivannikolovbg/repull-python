from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="SendMessagePart")



@_attrs_define
class SendMessagePart:
    """ One channel message produced by the send. Airbnb carries one file per message and no text beside it, so text + 2
    photos is 3 parts (files first, then the text). Booking.com carries every file on the one text message, so it is
    always 1 part.

        Attributes:
            attachment_indexes (list[int] | Unset): Indexes into the request's `attachments` that this message carried.
            has_text (bool | Unset): Whether this message carried the text.
            sent (bool | Unset):
            message_id (None | str | Unset):
            external_message_id (None | str | Unset):
            error (None | str | Unset): Why this part was not delivered.
     """

    attachment_indexes: list[int] | Unset = UNSET
    has_text: bool | Unset = UNSET
    sent: bool | Unset = UNSET
    message_id: None | str | Unset = UNSET
    external_message_id: None | str | Unset = UNSET
    error: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        attachment_indexes: list[int] | Unset = UNSET
        if not isinstance(self.attachment_indexes, Unset):
            attachment_indexes = self.attachment_indexes



        has_text = self.has_text

        sent = self.sent

        message_id: None | str | Unset
        if isinstance(self.message_id, Unset):
            message_id = UNSET
        else:
            message_id = self.message_id

        external_message_id: None | str | Unset
        if isinstance(self.external_message_id, Unset):
            external_message_id = UNSET
        else:
            external_message_id = self.external_message_id

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if attachment_indexes is not UNSET:
            field_dict["attachmentIndexes"] = attachment_indexes
        if has_text is not UNSET:
            field_dict["hasText"] = has_text
        if sent is not UNSET:
            field_dict["sent"] = sent
        if message_id is not UNSET:
            field_dict["messageId"] = message_id
        if external_message_id is not UNSET:
            field_dict["externalMessageId"] = external_message_id
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attachment_indexes = cast(list[int], d.pop("attachmentIndexes", UNSET))


        has_text = d.pop("hasText", UNSET)

        sent = d.pop("sent", UNSET)

        def _parse_message_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message_id = _parse_message_id(d.pop("messageId", UNSET))


        def _parse_external_message_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_message_id = _parse_external_message_id(d.pop("externalMessageId", UNSET))


        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))


        send_message_part = cls(
            attachment_indexes=attachment_indexes,
            has_text=has_text,
            sent=sent,
            message_id=message_id,
            external_message_id=external_message_id,
            error=error,
        )


        send_message_part.additional_properties = d
        return send_message_part

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
