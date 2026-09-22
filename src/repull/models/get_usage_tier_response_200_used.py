from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetUsageTierResponse200Used")



@_attrs_define
class GetUsageTierResponse200Used:
    """ 
        Attributes:
            monthly (int | Unset):
            daily (int | Unset):
            daily_ai (int | Unset):
            dynamic_pricing_listings (int | Unset):
     """

    monthly: int | Unset = UNSET
    daily: int | Unset = UNSET
    daily_ai: int | Unset = UNSET
    dynamic_pricing_listings: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        monthly = self.monthly

        daily = self.daily

        daily_ai = self.daily_ai

        dynamic_pricing_listings = self.dynamic_pricing_listings


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if monthly is not UNSET:
            field_dict["monthly"] = monthly
        if daily is not UNSET:
            field_dict["daily"] = daily
        if daily_ai is not UNSET:
            field_dict["dailyAi"] = daily_ai
        if dynamic_pricing_listings is not UNSET:
            field_dict["dynamicPricingListings"] = dynamic_pricing_listings

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        monthly = d.pop("monthly", UNSET)

        daily = d.pop("daily", UNSET)

        daily_ai = d.pop("dailyAi", UNSET)

        dynamic_pricing_listings = d.pop("dynamicPricingListings", UNSET)

        get_usage_tier_response_200_used = cls(
            monthly=monthly,
            daily=daily,
            daily_ai=daily_ai,
            dynamic_pricing_listings=dynamic_pricing_listings,
        )


        get_usage_tier_response_200_used.additional_properties = d
        return get_usage_tier_response_200_used

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
