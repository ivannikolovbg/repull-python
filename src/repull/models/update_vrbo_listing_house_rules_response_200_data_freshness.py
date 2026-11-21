from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.update_vrbo_listing_house_rules_response_200_data_freshness_reason import UpdateVrboListingHouseRulesResponse200DataFreshnessReason
from ..models.update_vrbo_listing_house_rules_response_200_data_freshness_source import UpdateVrboListingHouseRulesResponse200DataFreshnessSource
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.update_vrbo_listing_house_rules_response_200_data_freshness_accounts_item import UpdateVrboListingHouseRulesResponse200DataFreshnessAccountsItem





T = TypeVar("T", bound="UpdateVrboListingHouseRulesResponse200DataFreshness")



@_attrs_define
class UpdateVrboListingHouseRulesResponse200DataFreshness:
    """ 
        Attributes:
            last_synced_at (datetime.datetime): When this data was read from Vrbo.
            stale (bool):
            reason (UpdateVrboListingHouseRulesResponse200DataFreshnessReason): `refreshing`: the copy is over 24 h old and
                is being refreshed now — the next read has the new one. `reconnect_required`: Vrbo signed the account out;
                reconnect it (`fixUrl`).
            source (UpdateVrboListingHouseRulesResponse200DataFreshnessSource): `stored`: Repull's copy. `live`: read from
                Vrbo for this request.
            accounts (list[UpdateVrboListingHouseRulesResponse200DataFreshnessAccountsItem]):
            fix_url (str | Unset):
     """

    last_synced_at: datetime.datetime
    stale: bool
    reason: UpdateVrboListingHouseRulesResponse200DataFreshnessReason
    source: UpdateVrboListingHouseRulesResponse200DataFreshnessSource
    accounts: list[UpdateVrboListingHouseRulesResponse200DataFreshnessAccountsItem]
    fix_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_vrbo_listing_house_rules_response_200_data_freshness_accounts_item import UpdateVrboListingHouseRulesResponse200DataFreshnessAccountsItem
        last_synced_at = self.last_synced_at.isoformat()

        stale = self.stale

        reason = self.reason.value

        source = self.source.value

        accounts = []
        for accounts_item_data in self.accounts:
            accounts_item = accounts_item_data.to_dict()
            accounts.append(accounts_item)



        fix_url = self.fix_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "lastSyncedAt": last_synced_at,
            "stale": stale,
            "reason": reason,
            "source": source,
            "accounts": accounts,
        })
        if fix_url is not UNSET:
            field_dict["fixUrl"] = fix_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_vrbo_listing_house_rules_response_200_data_freshness_accounts_item import UpdateVrboListingHouseRulesResponse200DataFreshnessAccountsItem
        d = dict(src_dict)
        last_synced_at = isoparse(d.pop("lastSyncedAt"))




        stale = d.pop("stale")

        reason = UpdateVrboListingHouseRulesResponse200DataFreshnessReason(d.pop("reason"))




        source = UpdateVrboListingHouseRulesResponse200DataFreshnessSource(d.pop("source"))




        accounts = []
        _accounts = d.pop("accounts")
        for accounts_item_data in (_accounts):
            accounts_item = UpdateVrboListingHouseRulesResponse200DataFreshnessAccountsItem.from_dict(accounts_item_data)



            accounts.append(accounts_item)


        fix_url = d.pop("fixUrl", UNSET)

        update_vrbo_listing_house_rules_response_200_data_freshness = cls(
            last_synced_at=last_synced_at,
            stale=stale,
            reason=reason,
            source=source,
            accounts=accounts,
            fix_url=fix_url,
        )


        update_vrbo_listing_house_rules_response_200_data_freshness.additional_properties = d
        return update_vrbo_listing_house_rules_response_200_data_freshness

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
