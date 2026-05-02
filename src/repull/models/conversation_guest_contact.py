from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ConversationGuestContact")



@_attrs_define
class ConversationGuestContact:
    """ 
        Attributes:
            type_ (str | Unset):  Example: phone.
            value (str | Unset):
            is_primary (bool | Unset):
            is_verified (bool | Unset):
     """

    type_: str | Unset = UNSET
    value: str | Unset = UNSET
    is_primary: bool | Unset = UNSET
    is_verified: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        value = self.value

        is_primary = self.is_primary

        is_verified = self.is_verified


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if type_ is not UNSET:
            field_dict["type"] = type_
        if value is not UNSET:
            field_dict["value"] = value
        if is_primary is not UNSET:
            field_dict["isPrimary"] = is_primary
        if is_verified is not UNSET:
            field_dict["isVerified"] = is_verified

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        value = d.pop("value", UNSET)

        is_primary = d.pop("isPrimary", UNSET)

        is_verified = d.pop("isVerified", UNSET)

        conversation_guest_contact = cls(
            type_=type_,
            value=value,
            is_primary=is_primary,
            is_verified=is_verified,
        )


        conversation_guest_contact.additional_properties = d
        return conversation_guest_contact

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
