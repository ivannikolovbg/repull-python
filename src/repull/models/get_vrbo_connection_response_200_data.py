from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_vrbo_connection_response_200_data_status import GetVrboConnectionResponse200DataStatus
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_vrbo_connection_response_200_data_accounts_item import GetVrboConnectionResponse200DataAccountsItem





T = TypeVar("T", bound="GetVrboConnectionResponse200Data")



@_attrs_define
class GetVrboConnectionResponse200Data:
    """ 
        Attributes:
            status (GetVrboConnectionResponse200DataStatus | Unset):
            account_count (int | Unset):
            accounts (list[GetVrboConnectionResponse200DataAccountsItem] | Unset):
            fix_url (str | Unset):
     """

    status: GetVrboConnectionResponse200DataStatus | Unset = UNSET
    account_count: int | Unset = UNSET
    accounts: list[GetVrboConnectionResponse200DataAccountsItem] | Unset = UNSET
    fix_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_vrbo_connection_response_200_data_accounts_item import GetVrboConnectionResponse200DataAccountsItem
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        account_count = self.account_count

        accounts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.accounts, Unset):
            accounts = []
            for accounts_item_data in self.accounts:
                accounts_item = accounts_item_data.to_dict()
                accounts.append(accounts_item)



        fix_url = self.fix_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if status is not UNSET:
            field_dict["status"] = status
        if account_count is not UNSET:
            field_dict["accountCount"] = account_count
        if accounts is not UNSET:
            field_dict["accounts"] = accounts
        if fix_url is not UNSET:
            field_dict["fixUrl"] = fix_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_vrbo_connection_response_200_data_accounts_item import GetVrboConnectionResponse200DataAccountsItem
        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: GetVrboConnectionResponse200DataStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = GetVrboConnectionResponse200DataStatus(_status)




        account_count = d.pop("accountCount", UNSET)

        _accounts = d.pop("accounts", UNSET)
        accounts: list[GetVrboConnectionResponse200DataAccountsItem] | Unset = UNSET
        if _accounts is not UNSET:
            accounts = []
            for accounts_item_data in _accounts:
                accounts_item = GetVrboConnectionResponse200DataAccountsItem.from_dict(accounts_item_data)



                accounts.append(accounts_item)


        fix_url = d.pop("fixUrl", UNSET)

        get_vrbo_connection_response_200_data = cls(
            status=status,
            account_count=account_count,
            accounts=accounts,
            fix_url=fix_url,
        )


        get_vrbo_connection_response_200_data.additional_properties = d
        return get_vrbo_connection_response_200_data

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
