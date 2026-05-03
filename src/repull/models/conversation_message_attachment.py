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






T = TypeVar("T", bound="ConversationMessageAttachment")



@_attrs_define
class ConversationMessageAttachment:
    """ 
        Attributes:
            id (str | Unset):
            image_url (str | Unset):
            content_type (str | Unset):  Example: image/jpeg.
            created_at (datetime.datetime | Unset):
     """

    id: str | Unset = UNSET
    image_url: str | Unset = UNSET
    content_type: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        image_url = self.image_url

        content_type = self.content_type

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if image_url is not UNSET:
            field_dict["imageUrl"] = image_url
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        image_url = d.pop("imageUrl", UNSET)

        content_type = d.pop("contentType", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        conversation_message_attachment = cls(
            id=id,
            image_url=image_url,
            content_type=content_type,
            created_at=created_at,
        )


        conversation_message_attachment.additional_properties = d
        return conversation_message_attachment

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
