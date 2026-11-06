from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.airbnb_access_accounts_item import AirbnbAccessAccountsItem





T = TypeVar("T", bound="AirbnbAccess")



@_attrs_define
class AirbnbAccess:
    """ 
        Attributes:
            default_account (None | str): The account that acts when none is named: the conversation's own account while
                connected, else the listing's owner, else a connected co-host. Null when none is connected. Example:
                airbnb:483175841.
            accounts (list[AirbnbAccessAccountsItem]):
     """

    default_account: None | str
    accounts: list[AirbnbAccessAccountsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.airbnb_access_accounts_item import AirbnbAccessAccountsItem
        default_account: None | str
        default_account = self.default_account

        accounts = []
        for accounts_item_data in self.accounts:
            accounts_item = accounts_item_data.to_dict()
            accounts.append(accounts_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "defaultAccount": default_account,
            "accounts": accounts,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.airbnb_access_accounts_item import AirbnbAccessAccountsItem
        d = dict(src_dict)
        def _parse_default_account(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        default_account = _parse_default_account(d.pop("defaultAccount"))


        accounts = []
        _accounts = d.pop("accounts")
        for accounts_item_data in (_accounts):
            accounts_item = AirbnbAccessAccountsItem.from_dict(accounts_item_data)



            accounts.append(accounts_item)


        airbnb_access = cls(
            default_account=default_account,
            accounts=accounts,
        )


        airbnb_access.additional_properties = d
        return airbnb_access

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
