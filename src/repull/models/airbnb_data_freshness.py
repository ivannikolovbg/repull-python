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






T = TypeVar("T", bound="AirbnbDataFreshness")



@_attrs_define
class AirbnbDataFreshness:
    """ Top-level freshness indicator for any DB-backed Airbnb read. Tells consumers WHY a column may be `null` or stale
    without sprinkling per-row error envelopes through the response. The endpoint always returns 200 + DB data; this
    field is the single signal for "should I prompt the user to reconnect / wait for sync?".

        Attributes:
            last_synced_at (datetime.datetime | None): Most recent sync timestamp across the rows in the response. `null`
                when nothing has ever synced for this customer.
            stale (bool): `true` when any host is disconnected, when the local cache is empty, or when the cache hasn't been
                refreshed in 24h+. `false` when hosts are healthy and sync is fresh.
            reason (None | str | Unset): Why the data is stale. One of `host_disconnected_since_<iso>`, `sync_lag_>_24h`,
                `never_synced`. Omitted when `stale` is `false`.
            fix_url (None | str | Unset): Dashboard URL the consumer can open to resolve the staleness (typically the Airbnb
                reconnect screen). Omitted when `stale` is `false`.
     """

    last_synced_at: datetime.datetime | None
    stale: bool
    reason: None | str | Unset = UNSET
    fix_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
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


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "last_synced_at": last_synced_at,
            "stale": stale,
        })
        if reason is not UNSET:
            field_dict["reason"] = reason
        if fix_url is not UNSET:
            field_dict["fix_url"] = fix_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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

        last_synced_at = _parse_last_synced_at(d.pop("last_synced_at"))


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

        fix_url = _parse_fix_url(d.pop("fix_url", UNSET))


        airbnb_data_freshness = cls(
            last_synced_at=last_synced_at,
            stale=stale,
            reason=reason,
            fix_url=fix_url,
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
