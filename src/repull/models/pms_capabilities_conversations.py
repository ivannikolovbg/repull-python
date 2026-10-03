from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PmsCapabilitiesConversations")



@_attrs_define
class PmsCapabilitiesConversations:
    """ 
        Attributes:
            send (bool | Unset):
            attachments (bool | Unset): `attachments` on `POST /v1/conversations/{id}/messages`.
            channel_select (bool | Unset): `channel` on `POST /v1/conversations/{id}/messages`.
     """

    send: bool | Unset = UNSET
    attachments: bool | Unset = UNSET
    channel_select: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        send = self.send

        attachments = self.attachments

        channel_select = self.channel_select


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if send is not UNSET:
            field_dict["send"] = send
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if channel_select is not UNSET:
            field_dict["channelSelect"] = channel_select

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        send = d.pop("send", UNSET)

        attachments = d.pop("attachments", UNSET)

        channel_select = d.pop("channelSelect", UNSET)

        pms_capabilities_conversations = cls(
            send=send,
            attachments=attachments,
            channel_select=channel_select,
        )


        pms_capabilities_conversations.additional_properties = d
        return pms_capabilities_conversations

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
