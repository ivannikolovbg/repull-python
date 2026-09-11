from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.guest_create_response_contacts_item_type import GuestCreateResponseContactsItemType
from ..types import UNSET, Unset






T = TypeVar("T", bound="GuestCreateResponseContactsItem")



@_attrs_define
class GuestCreateResponseContactsItem:
    """ 
        Attributes:
            type_ (GuestCreateResponseContactsItemType | Unset):
            value (str | Unset):
            is_primary (bool | Unset):
     """

    type_: GuestCreateResponseContactsItemType | Unset = UNSET
    value: str | Unset = UNSET
    is_primary: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value


        value = self.value

        is_primary = self.is_primary


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

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: GuestCreateResponseContactsItemType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = GuestCreateResponseContactsItemType(_type_)




        value = d.pop("value", UNSET)

        is_primary = d.pop("isPrimary", UNSET)

        guest_create_response_contacts_item = cls(
            type_=type_,
            value=value,
            is_primary=is_primary,
        )


        guest_create_response_contacts_item.additional_properties = d
        return guest_create_response_contacts_item

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
