from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="DeactivateWorkspaceResponse200DataDisconnectedItem")



@_attrs_define
class DeactivateWorkspaceResponse200DataDisconnectedItem:
    """ 
        Attributes:
            provider (str | Unset):  Example: airbnb.
            account_id (str | Unset):
     """

    provider: str | Unset = UNSET
    account_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        provider = self.provider

        account_id = self.account_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if provider is not UNSET:
            field_dict["provider"] = provider
        if account_id is not UNSET:
            field_dict["accountId"] = account_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        provider = d.pop("provider", UNSET)

        account_id = d.pop("accountId", UNSET)

        deactivate_workspace_response_200_data_disconnected_item = cls(
            provider=provider,
            account_id=account_id,
        )


        deactivate_workspace_response_200_data_disconnected_item.additional_properties = d
        return deactivate_workspace_response_200_data_disconnected_item

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
