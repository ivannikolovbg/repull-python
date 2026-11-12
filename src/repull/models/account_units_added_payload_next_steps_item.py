from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.account_units_added_payload_next_steps_item_method import AccountUnitsAddedPayloadNextStepsItemMethod






T = TypeVar("T", bound="AccountUnitsAddedPayloadNextStepsItem")



@_attrs_define
class AccountUnitsAddedPayloadNextStepsItem:
    """ 
        Attributes:
            method (AccountUnitsAddedPayloadNextStepsItemMethod):
            path (str):  Example: /v1/connections/booking_extranet:20123456/units.
            description (str):
     """

    method: AccountUnitsAddedPayloadNextStepsItemMethod
    path: str
    description: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        method = self.method.value

        path = self.path

        description = self.description


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "method": method,
            "path": path,
            "description": description,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        method = AccountUnitsAddedPayloadNextStepsItemMethod(d.pop("method"))




        path = d.pop("path")

        description = d.pop("description")

        account_units_added_payload_next_steps_item = cls(
            method=method,
            path=path,
            description=description,
        )


        account_units_added_payload_next_steps_item.additional_properties = d
        return account_units_added_payload_next_steps_item

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
