from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PromotionBulkResponseDataItemError")



@_attrs_define
class PromotionBulkResponseDataItemError:
    """ 
        Attributes:
            message (str | Unset):
            code (str | Unset):
            field (str | Unset):
     """

    message: str | Unset = UNSET
    code: str | Unset = UNSET
    field: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        message = self.message

        code = self.code

        field = self.field


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if message is not UNSET:
            field_dict["message"] = message
        if code is not UNSET:
            field_dict["code"] = code
        if field is not UNSET:
            field_dict["field"] = field

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message", UNSET)

        code = d.pop("code", UNSET)

        field = d.pop("field", UNSET)

        promotion_bulk_response_data_item_error = cls(
            message=message,
            code=code,
            field=field,
        )


        promotion_bulk_response_data_item_error.additional_properties = d
        return promotion_bulk_response_data_item_error

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
