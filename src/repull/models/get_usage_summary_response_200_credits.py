from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetUsageSummaryResponse200Credits")



@_attrs_define
class GetUsageSummaryResponse200Credits:
    """ Pay-as-you-go wallet. Requests beyond your plan's monthly quota keep being served while `active`, billed at
    `usdPer1000Requests`. Top up at https://repull.dev/dashboard/billing.

        Attributes:
            balance_usd (float | Unset):
            active (bool | Unset): Positive balance and not paused — usage beyond the monthly quota is being served.
            paused (bool | Unset):
            usd_per_1000_requests (float | Unset):  Example: 1.
            requests_covered (int | Unset): Requests beyond your quota the current balance pays for.
     """

    balance_usd: float | Unset = UNSET
    active: bool | Unset = UNSET
    paused: bool | Unset = UNSET
    usd_per_1000_requests: float | Unset = UNSET
    requests_covered: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        balance_usd = self.balance_usd

        active = self.active

        paused = self.paused

        usd_per_1000_requests = self.usd_per_1000_requests

        requests_covered = self.requests_covered


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if balance_usd is not UNSET:
            field_dict["balanceUsd"] = balance_usd
        if active is not UNSET:
            field_dict["active"] = active
        if paused is not UNSET:
            field_dict["paused"] = paused
        if usd_per_1000_requests is not UNSET:
            field_dict["usdPer1000Requests"] = usd_per_1000_requests
        if requests_covered is not UNSET:
            field_dict["requestsCovered"] = requests_covered

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        balance_usd = d.pop("balanceUsd", UNSET)

        active = d.pop("active", UNSET)

        paused = d.pop("paused", UNSET)

        usd_per_1000_requests = d.pop("usdPer1000Requests", UNSET)

        requests_covered = d.pop("requestsCovered", UNSET)

        get_usage_summary_response_200_credits = cls(
            balance_usd=balance_usd,
            active=active,
            paused=paused,
            usd_per_1000_requests=usd_per_1000_requests,
            requests_covered=requests_covered,
        )


        get_usage_summary_response_200_credits.additional_properties = d
        return get_usage_summary_response_200_credits

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
