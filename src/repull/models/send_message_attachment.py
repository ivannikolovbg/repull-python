from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SendMessageAttachment")



@_attrs_define
class SendMessageAttachment:
    """ A file to send, by URL. Repull downloads it (public `https://` only — no credentials in the URL, no private or
    internal addresses; redirects are followed and re-checked; 20 s timeout), reads its real type from the file's bytes,
    and keeps a durable copy. Nothing is sent to the guest until every file in the request has passed.

        Attributes:
            url (str): Public https URL of the file. A signed URL valid for a few minutes is fine. Example:
                https://cdn.example.com/parking-map.jpg.
            content_type (str | Unset): Optional hint, e.g. `image/jpeg`. The type is read from the file itself; this never
                overrides it. Example: image/jpeg.
            filename (str | Unset): Optional display name. Defaults to the last segment of the URL. Example: parking-
                map.jpg.
     """

    url: str
    content_type: str | Unset = UNSET
    filename: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        url = self.url

        content_type = self.content_type

        filename = self.filename


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "url": url,
        })
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if filename is not UNSET:
            field_dict["filename"] = filename

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        content_type = d.pop("contentType", UNSET)

        filename = d.pop("filename", UNSET)

        send_message_attachment = cls(
            url=url,
            content_type=content_type,
            filename=filename,
        )

        return send_message_attachment

