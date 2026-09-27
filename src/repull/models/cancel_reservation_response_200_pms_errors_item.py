from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CancelReservationResponse200PmsErrorsItem")



@_attrs_define
class CancelReservationResponse200PmsErrorsItem:
    """ 
        Attributes:
            section (str | Unset):
            message (str | Unset):
            code (str | Unset):
     """

    section: str | Unset = UNSET
    message: str | Unset = UNSET
    code: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        section = self.section

        message = self.message

        code = self.code


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if section is not UNSET:
            field_dict["section"] = section
        if message is not UNSET:
            field_dict["message"] = message
        if code is not UNSET:
            field_dict["code"] = code

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        section = d.pop("section", UNSET)

        message = d.pop("message", UNSET)

        code = d.pop("code", UNSET)

        cancel_reservation_response_200_pms_errors_item = cls(
            section=section,
            message=message,
            code=code,
        )


        cancel_reservation_response_200_pms_errors_item.additional_properties = d
        return cancel_reservation_response_200_pms_errors_item

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
