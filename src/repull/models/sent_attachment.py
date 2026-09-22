from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.sent_attachment_type import SentAttachmentType
from ..types import UNSET, Unset






T = TypeVar("T", bound="SentAttachment")



@_attrs_define
class SentAttachment:
    """ A file as delivered.

        Attributes:
            url (str | Unset): Durable stored copy — the same `url` the message's `attachments` will show when read back.
            type_ (SentAttachmentType | Unset):
            content_type (str | Unset): Type read from the file's bytes. Example: image/jpeg.
            filename (str | Unset):  Example: parking-map.jpg.
            size_bytes (int | Unset):  Example: 184233.
            source_url (str | Unset): The URL you sent.
     """

    url: str | Unset = UNSET
    type_: SentAttachmentType | Unset = UNSET
    content_type: str | Unset = UNSET
    filename: str | Unset = UNSET
    size_bytes: int | Unset = UNSET
    source_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        url = self.url

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value


        content_type = self.content_type

        filename = self.filename

        size_bytes = self.size_bytes

        source_url = self.source_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if url is not UNSET:
            field_dict["url"] = url
        if type_ is not UNSET:
            field_dict["type"] = type_
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if filename is not UNSET:
            field_dict["filename"] = filename
        if size_bytes is not UNSET:
            field_dict["sizeBytes"] = size_bytes
        if source_url is not UNSET:
            field_dict["sourceUrl"] = source_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: SentAttachmentType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = SentAttachmentType(_type_)




        content_type = d.pop("contentType", UNSET)

        filename = d.pop("filename", UNSET)

        size_bytes = d.pop("sizeBytes", UNSET)

        source_url = d.pop("sourceUrl", UNSET)

        sent_attachment = cls(
            url=url,
            type_=type_,
            content_type=content_type,
            filename=filename,
            size_bytes=size_bytes,
            source_url=source_url,
        )


        sent_attachment.additional_properties = d
        return sent_attachment

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
