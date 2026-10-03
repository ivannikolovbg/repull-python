from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.listing_content_update_response_pms_type_0_errors_item_code import ListingContentUpdateResponsePmsType0ErrorsItemCode
from ..types import UNSET, Unset






T = TypeVar("T", bound="ListingContentUpdateResponsePmsType0ErrorsItem")



@_attrs_define
class ListingContentUpdateResponsePmsType0ErrorsItem:
    """ 
        Attributes:
            section (str | Unset):
            code (ListingContentUpdateResponsePmsType0ErrorsItemCode | Unset):
            message (str | Unset):
     """

    section: str | Unset = UNSET
    code: ListingContentUpdateResponsePmsType0ErrorsItemCode | Unset = UNSET
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        section = self.section

        code: str | Unset = UNSET
        if not isinstance(self.code, Unset):
            code = self.code.value


        message = self.message


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if section is not UNSET:
            field_dict["section"] = section
        if code is not UNSET:
            field_dict["code"] = code
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        section = d.pop("section", UNSET)

        _code = d.pop("code", UNSET)
        code: ListingContentUpdateResponsePmsType0ErrorsItemCode | Unset
        if isinstance(_code,  Unset):
            code = UNSET
        else:
            code = ListingContentUpdateResponsePmsType0ErrorsItemCode(_code)




        message = d.pop("message", UNSET)

        listing_content_update_response_pms_type_0_errors_item = cls(
            section=section,
            code=code,
            message=message,
        )


        listing_content_update_response_pms_type_0_errors_item.additional_properties = d
        return listing_content_update_response_pms_type_0_errors_item

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
