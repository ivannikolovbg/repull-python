from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GetVrboListingHouseRulesResponse200DataFreshnessAccountsItem")



@_attrs_define
class GetVrboListingHouseRulesResponse200DataFreshnessAccountsItem:
    """ 
        Attributes:
            account_id (None | str | Unset):
            account_name (None | str | Unset):
            last_synced_at (str | Unset):
            stale (bool | Unset):
            reason (str | Unset):
            fix_url (str | Unset):
     """

    account_id: None | str | Unset = UNSET
    account_name: None | str | Unset = UNSET
    last_synced_at: str | Unset = UNSET
    stale: bool | Unset = UNSET
    reason: str | Unset = UNSET
    fix_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        account_id: None | str | Unset
        if isinstance(self.account_id, Unset):
            account_id = UNSET
        else:
            account_id = self.account_id

        account_name: None | str | Unset
        if isinstance(self.account_name, Unset):
            account_name = UNSET
        else:
            account_name = self.account_name

        last_synced_at = self.last_synced_at

        stale = self.stale

        reason = self.reason

        fix_url = self.fix_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if account_name is not UNSET:
            field_dict["accountName"] = account_name
        if last_synced_at is not UNSET:
            field_dict["lastSyncedAt"] = last_synced_at
        if stale is not UNSET:
            field_dict["stale"] = stale
        if reason is not UNSET:
            field_dict["reason"] = reason
        if fix_url is not UNSET:
            field_dict["fixUrl"] = fix_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account_id = _parse_account_id(d.pop("accountId", UNSET))


        def _parse_account_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account_name = _parse_account_name(d.pop("accountName", UNSET))


        last_synced_at = d.pop("lastSyncedAt", UNSET)

        stale = d.pop("stale", UNSET)

        reason = d.pop("reason", UNSET)

        fix_url = d.pop("fixUrl", UNSET)

        get_vrbo_listing_house_rules_response_200_data_freshness_accounts_item = cls(
            account_id=account_id,
            account_name=account_name,
            last_synced_at=last_synced_at,
            stale=stale,
            reason=reason,
            fix_url=fix_url,
        )


        get_vrbo_listing_house_rules_response_200_data_freshness_accounts_item.additional_properties = d
        return get_vrbo_listing_house_rules_response_200_data_freshness_accounts_item

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
