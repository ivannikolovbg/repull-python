from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_vrbo_listing_response_200_data_freshness_accounts_item import GetVrboListingResponse200DataFreshnessAccountsItem





T = TypeVar("T", bound="GetVrboListingResponse200DataFreshness")



@_attrs_define
class GetVrboListingResponse200DataFreshness:
    """ Whether the Vrbo accounts are in sync — the same envelope as the Airbnb reads.

        Attributes:
            last_synced_at (None | str | Unset):
            stale (bool | Unset):
            reason (str | Unset):
            fix_url (str | Unset):
            accounts (list[GetVrboListingResponse200DataFreshnessAccountsItem] | Unset):
     """

    last_synced_at: None | str | Unset = UNSET
    stale: bool | Unset = UNSET
    reason: str | Unset = UNSET
    fix_url: str | Unset = UNSET
    accounts: list[GetVrboListingResponse200DataFreshnessAccountsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_vrbo_listing_response_200_data_freshness_accounts_item import GetVrboListingResponse200DataFreshnessAccountsItem
        last_synced_at: None | str | Unset
        if isinstance(self.last_synced_at, Unset):
            last_synced_at = UNSET
        else:
            last_synced_at = self.last_synced_at

        stale = self.stale

        reason = self.reason

        fix_url = self.fix_url

        accounts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.accounts, Unset):
            accounts = []
            for accounts_item_data in self.accounts:
                accounts_item = accounts_item_data.to_dict()
                accounts.append(accounts_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if last_synced_at is not UNSET:
            field_dict["lastSyncedAt"] = last_synced_at
        if stale is not UNSET:
            field_dict["stale"] = stale
        if reason is not UNSET:
            field_dict["reason"] = reason
        if fix_url is not UNSET:
            field_dict["fixUrl"] = fix_url
        if accounts is not UNSET:
            field_dict["accounts"] = accounts

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_vrbo_listing_response_200_data_freshness_accounts_item import GetVrboListingResponse200DataFreshnessAccountsItem
        d = dict(src_dict)
        def _parse_last_synced_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_synced_at = _parse_last_synced_at(d.pop("lastSyncedAt", UNSET))


        stale = d.pop("stale", UNSET)

        reason = d.pop("reason", UNSET)

        fix_url = d.pop("fixUrl", UNSET)

        _accounts = d.pop("accounts", UNSET)
        accounts: list[GetVrboListingResponse200DataFreshnessAccountsItem] | Unset = UNSET
        if _accounts is not UNSET:
            accounts = []
            for accounts_item_data in _accounts:
                accounts_item = GetVrboListingResponse200DataFreshnessAccountsItem.from_dict(accounts_item_data)



                accounts.append(accounts_item)


        get_vrbo_listing_response_200_data_freshness = cls(
            last_synced_at=last_synced_at,
            stale=stale,
            reason=reason,
            fix_url=fix_url,
            accounts=accounts,
        )


        get_vrbo_listing_response_200_data_freshness.additional_properties = d
        return get_vrbo_listing_response_200_data_freshness

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
