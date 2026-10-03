from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PmsCapabilitiesReviews")



@_attrs_define
class PmsCapabilitiesReviews:
    """ 
        Attributes:
            read (bool | Unset): Its reviews appear in `GET /v1/reviews` (with `pms` set).
            reply (bool | Unset): `POST /v1/reviews/{id}/reply`.
     """

    read: bool | Unset = UNSET
    reply: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        read = self.read

        reply = self.reply


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if read is not UNSET:
            field_dict["read"] = read
        if reply is not UNSET:
            field_dict["reply"] = reply

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        read = d.pop("read", UNSET)

        reply = d.pop("reply", UNSET)

        pms_capabilities_reviews = cls(
            read=read,
            reply=reply,
        )


        pms_capabilities_reviews.additional_properties = d
        return pms_capabilities_reviews

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
