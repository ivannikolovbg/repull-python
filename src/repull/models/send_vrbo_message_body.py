from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="SendVrboMessageBody")



@_attrs_define
class SendVrboMessageBody:
    """ 
        Attributes:
            message (str): The text to send to the guest.
            media_url (None | str | Unset): Accepted for the same body as Airbnb; Vrbo carries no files, so a send with one
                is refused (`attachments_not_supported`).
            media_type (None | str | Unset):
     """

    message: str
    media_url: None | str | Unset = UNSET
    media_type: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        message = self.message

        media_url: None | str | Unset
        if isinstance(self.media_url, Unset):
            media_url = UNSET
        else:
            media_url = self.media_url

        media_type: None | str | Unset
        if isinstance(self.media_type, Unset):
            media_type = UNSET
        else:
            media_type = self.media_type


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "message": message,
        })
        if media_url is not UNSET:
            field_dict["mediaUrl"] = media_url
        if media_type is not UNSET:
            field_dict["mediaType"] = media_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message")

        def _parse_media_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        media_url = _parse_media_url(d.pop("mediaUrl", UNSET))


        def _parse_media_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        media_type = _parse_media_type(d.pop("mediaType", UNSET))


        send_vrbo_message_body = cls(
            message=message,
            media_url=media_url,
            media_type=media_type,
        )

        return send_vrbo_message_body

