from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.refresh_airbnb_resolutions_response_200_accounts_item import RefreshAirbnbResolutionsResponse200AccountsItem





T = TypeVar("T", bound="RefreshAirbnbResolutionsResponse200")



@_attrs_define
class RefreshAirbnbResolutionsResponse200:
    """ 
        Attributes:
            synced (bool):
            count (int): Resolutions upserted across all accounts.
            accounts (list[RefreshAirbnbResolutionsResponse200AccountsItem]):
     """

    synced: bool
    count: int
    accounts: list[RefreshAirbnbResolutionsResponse200AccountsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.refresh_airbnb_resolutions_response_200_accounts_item import RefreshAirbnbResolutionsResponse200AccountsItem
        synced = self.synced

        count = self.count

        accounts = []
        for accounts_item_data in self.accounts:
            accounts_item = accounts_item_data.to_dict()
            accounts.append(accounts_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "synced": synced,
            "count": count,
            "accounts": accounts,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.refresh_airbnb_resolutions_response_200_accounts_item import RefreshAirbnbResolutionsResponse200AccountsItem
        d = dict(src_dict)
        synced = d.pop("synced")

        count = d.pop("count")

        accounts = []
        _accounts = d.pop("accounts")
        for accounts_item_data in (_accounts):
            accounts_item = RefreshAirbnbResolutionsResponse200AccountsItem.from_dict(accounts_item_data)



            accounts.append(accounts_item)


        refresh_airbnb_resolutions_response_200 = cls(
            synced=synced,
            count=count,
            accounts=accounts,
        )


        refresh_airbnb_resolutions_response_200.additional_properties = d
        return refresh_airbnb_resolutions_response_200

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
