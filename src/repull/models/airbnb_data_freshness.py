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

if TYPE_CHECKING:
  from ..models.airbnb_account_freshness import AirbnbAccountFreshness





T = TypeVar("T", bound="AirbnbDataFreshness")



@_attrs_define
class AirbnbDataFreshness:
    """ Top-level freshness indicator for any DB-backed Airbnb read. Tells consumers WHY a column may be `null` or stale
    without sprinkling per-row error envelopes through the response. The endpoint always returns 200 + DB data; this
    field is the single signal for "should I prompt the user to reconnect / wait for sync?".

    A workspace can connect several Airbnb accounts, so the answer has two levels. `accounts[]` carries the verdict per
    account; the top-level fields aggregate it. Scope a request with `?account_id=` and `accounts[]` holds exactly that
    account, with the top-level fields mirroring it.

        Attributes:
            last_synced_at (datetime.datetime | None): The most recent Airbnb import COMPLETED by any account in scope.
                `null` when none of them ever has. A run that failed or was rate-limited does not move it.
            stale (bool): `true` only when EVERY connected Airbnb account is stale — nothing in this response can be trusted
                to be current. With one account (the common case) that is the same as it has always been. With several, one
                disconnected host no longer condemns the other's rows: `stale` stays `false` and `reason` becomes
                `partial_account_staleness`. Read `accounts[]` for which is which.
            reason (None | str | Unset): Why the data is stale. One of `host_disconnected_since_<iso>`,
                `host_not_activated`, `sync_lag_>_24h`, `never_synced`, `host_disconnected`, or `partial_account_staleness`. The
                last one appears WITH `stale: false`: the response is usable, but at least one connected account needs attention
                — deliberately surfaced so a consumer reading only the aggregate is never told everything is fine while an
                account is down.
            fix_url (None | str | Unset): Dashboard URL the consumer can open to resolve the staleness (the Airbnb
                connections screen). Present whenever `reason` is, including on `partial_account_staleness`.
            accounts (list[AirbnbAccountFreshness] | Unset): Per-account freshness, sorted by `accountId`. Omitted on
                responses that have no connected account to attribute (e.g. a workspace that has never connected Airbnb).
     """

    last_synced_at: datetime.datetime | None
    stale: bool
    reason: None | str | Unset = UNSET
    fix_url: None | str | Unset = UNSET
    accounts: list[AirbnbAccountFreshness] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.airbnb_account_freshness import AirbnbAccountFreshness
        last_synced_at: None | str
        if isinstance(self.last_synced_at, datetime.datetime):
            last_synced_at = self.last_synced_at.isoformat()
        else:
            last_synced_at = self.last_synced_at

        stale = self.stale

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

        accounts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.accounts, Unset):
            accounts = []
            for accounts_item_data in self.accounts:
                accounts_item = accounts_item_data.to_dict()
                accounts.append(accounts_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "lastSyncedAt": last_synced_at,
            "stale": stale,
        })
        if reason is not UNSET:
            field_dict["reason"] = reason
        if fix_url is not UNSET:
            field_dict["fixUrl"] = fix_url
        if accounts is not UNSET:
            field_dict["accounts"] = accounts

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.airbnb_account_freshness import AirbnbAccountFreshness
        d = dict(src_dict)
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


        _accounts = d.pop("accounts", UNSET)
        accounts: list[AirbnbAccountFreshness] | Unset = UNSET
        if _accounts is not UNSET:
            accounts = []
            for accounts_item_data in _accounts:
                accounts_item = AirbnbAccountFreshness.from_dict(accounts_item_data)



                accounts.append(accounts_item)


        airbnb_data_freshness = cls(
            last_synced_at=last_synced_at,
            stale=stale,
            reason=reason,
            fix_url=fix_url,
            accounts=accounts,
        )


        airbnb_data_freshness.additional_properties = d
        return airbnb_data_freshness

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
