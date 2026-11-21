from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetVrboConnectionResponse200DataAccountsItemSync")



@_attrs_define
class GetVrboConnectionResponse200DataAccountsItemSync:
    """ 
        Attributes:
            stale (bool | Unset):
            reason (str | Unset):
     """

    stale: bool | Unset = UNSET
    reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        stale = self.stale

        reason = self.reason


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if stale is not UNSET:
            field_dict["stale"] = stale
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        stale = d.pop("stale", UNSET)

        reason = d.pop("reason", UNSET)

        get_vrbo_connection_response_200_data_accounts_item_sync = cls(
            stale=stale,
            reason=reason,
        )


        get_vrbo_connection_response_200_data_accounts_item_sync.additional_properties = d
        return get_vrbo_connection_response_200_data_accounts_item_sync

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
