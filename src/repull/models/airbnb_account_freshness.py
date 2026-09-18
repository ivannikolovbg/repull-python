from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="AirbnbAccountFreshness")



@_attrs_define
class AirbnbAccountFreshness:
    """ Freshness of ONE connected Airbnb account. Freshness is a property of an account, not of a workspace: one host's
    token expiring says nothing about another host's data.

        Attributes:
            account_id (str): Airbnb host id, as a string (they exceed 2^53). The same value `?account_id=` accepts and `GET
                /v1/connect/airbnb` returns as `accounts[].externalAccountId`. Example: 1772489413932732258.
            last_synced_at (datetime.datetime | None): When this account last COMPLETED an Airbnb import. `null` when it
                never has. A run that failed or was rate-limited does not move it.
            stale (bool): `true` when this account is disconnected, has never synced, or has not refreshed in 24h+.
            account_name (None | str | Unset): Display name of the connected account. Example: Pomello.
            reason (None | str | Unset): Why THIS account is stale. Omitted when it is fresh.
            fix_url (None | str | Unset): Where to reconnect this account. Omitted when it is fresh.
     """

    account_id: str
    last_synced_at: datetime.datetime | None
    stale: bool
    account_name: None | str | Unset = UNSET
    reason: None | str | Unset = UNSET
    fix_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        last_synced_at: None | str
        if isinstance(self.last_synced_at, datetime.datetime):
            last_synced_at = self.last_synced_at.isoformat()
        else:
            last_synced_at = self.last_synced_at

        stale = self.stale

        account_name: None | str | Unset
        if isinstance(self.account_name, Unset):
            account_name = UNSET
        else:
            account_name = self.account_name

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        fix_url: None | str | Unset
        if isinstance(self.fix_url, Unset):
            fix_url = UNSET
        else:
            fix_url = self.fix_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "accountId": account_id,
            "lastSyncedAt": last_synced_at,
            "stale": stale,
        })
        if account_name is not UNSET:
            field_dict["accountName"] = account_name
        if reason is not UNSET:
            field_dict["reason"] = reason
        if fix_url is not UNSET:
            field_dict["fixUrl"] = fix_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("accountId")

        def _parse_last_synced_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_synced_at_type_0 = isoparse(data)



                return last_synced_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_synced_at = _parse_last_synced_at(d.pop("lastSyncedAt"))


        stale = d.pop("stale")

        def _parse_account_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account_name = _parse_account_name(d.pop("accountName", UNSET))


        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))


        def _parse_fix_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fix_url = _parse_fix_url(d.pop("fixUrl", UNSET))


        airbnb_account_freshness = cls(
            account_id=account_id,
            last_synced_at=last_synced_at,
            stale=stale,
            account_name=account_name,
            reason=reason,
            fix_url=fix_url,
        )


        airbnb_account_freshness.additional_properties = d
        return airbnb_account_freshness

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
