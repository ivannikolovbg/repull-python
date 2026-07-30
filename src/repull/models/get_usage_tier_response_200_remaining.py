from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GetUsageTierResponse200Remaining")



@_attrs_define
class GetUsageTierResponse200Remaining:
    """ 
        Attributes:
            monthly (int | None | Unset):
            daily_ai (int | None | Unset):
            dynamic_pricing_listings (int | None | Unset):
     """

    monthly: int | None | Unset = UNSET
    daily_ai: int | None | Unset = UNSET
    dynamic_pricing_listings: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        monthly: int | None | Unset
        if isinstance(self.monthly, Unset):
            monthly = UNSET
        else:
            monthly = self.monthly

        daily_ai: int | None | Unset
        if isinstance(self.daily_ai, Unset):
            daily_ai = UNSET
        else:
            daily_ai = self.daily_ai

        dynamic_pricing_listings: int | None | Unset
        if isinstance(self.dynamic_pricing_listings, Unset):
            dynamic_pricing_listings = UNSET
        else:
            dynamic_pricing_listings = self.dynamic_pricing_listings


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if monthly is not UNSET:
            field_dict["monthly"] = monthly
        if daily_ai is not UNSET:
            field_dict["daily_ai"] = daily_ai
        if dynamic_pricing_listings is not UNSET:
            field_dict["dynamic_pricing_listings"] = dynamic_pricing_listings

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_monthly(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        monthly = _parse_monthly(d.pop("monthly", UNSET))


        def _parse_daily_ai(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        daily_ai = _parse_daily_ai(d.pop("daily_ai", UNSET))


        def _parse_dynamic_pricing_listings(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        dynamic_pricing_listings = _parse_dynamic_pricing_listings(d.pop("dynamic_pricing_listings", UNSET))


        get_usage_tier_response_200_remaining = cls(
            monthly=monthly,
            daily_ai=daily_ai,
            dynamic_pricing_listings=dynamic_pricing_listings,
        )


        get_usage_tier_response_200_remaining.additional_properties = d
        return get_usage_tier_response_200_remaining

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
