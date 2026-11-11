from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="ErrorErrorCredits")



@_attrs_define
class ErrorErrorCredits:
    """ Pay-as-you-go credits, the alternative to a plan change: past your plan's monthly quota, requests are served while
    the wallet has a balance. Present with `upgrade`.

        Attributes:
            usd_per_1000_requests (float):  Example: 1.
            top_up_url (str):  Example: https://repull.dev/dashboard/billing.
            balance_usd (float | None): Your wallet balance; null when you have no wallet.
     """

    usd_per_1000_requests: float
    top_up_url: str
    balance_usd: float | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        usd_per_1000_requests = self.usd_per_1000_requests

        top_up_url = self.top_up_url

        balance_usd: float | None
        balance_usd = self.balance_usd


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "usd_per_1000_requests": usd_per_1000_requests,
            "top_up_url": top_up_url,
            "balance_usd": balance_usd,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        usd_per_1000_requests = d.pop("usd_per_1000_requests")

        top_up_url = d.pop("top_up_url")

        def _parse_balance_usd(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        balance_usd = _parse_balance_usd(d.pop("balance_usd"))


        error_error_credits = cls(
            usd_per_1000_requests=usd_per_1000_requests,
            top_up_url=top_up_url,
            balance_usd=balance_usd,
        )


        error_error_credits.additional_properties = d
        return error_error_credits

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
