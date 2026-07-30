from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GetUsageTierResponse200Limits")



@_attrs_define
class GetUsageTierResponse200Limits:
    """ 
        Attributes:
            monthly_requests (int | None | Unset):
            daily_ai_requests (int | None | Unset):
            dynamic_pricing_listings (int | None | Unset):
     """

    monthly_requests: int | None | Unset = UNSET
    daily_ai_requests: int | None | Unset = UNSET
    dynamic_pricing_listings: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        monthly_requests: int | None | Unset
        if isinstance(self.monthly_requests, Unset):
            monthly_requests = UNSET
        else:
            monthly_requests = self.monthly_requests

        daily_ai_requests: int | None | Unset
        if isinstance(self.daily_ai_requests, Unset):
            daily_ai_requests = UNSET
        else:
            daily_ai_requests = self.daily_ai_requests

        dynamic_pricing_listings: int | None | Unset
        if isinstance(self.dynamic_pricing_listings, Unset):
            dynamic_pricing_listings = UNSET
        else:
            dynamic_pricing_listings = self.dynamic_pricing_listings


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if monthly_requests is not UNSET:
            field_dict["monthly_requests"] = monthly_requests
        if daily_ai_requests is not UNSET:
            field_dict["daily_ai_requests"] = daily_ai_requests
        if dynamic_pricing_listings is not UNSET:
            field_dict["dynamic_pricing_listings"] = dynamic_pricing_listings

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_monthly_requests(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        monthly_requests = _parse_monthly_requests(d.pop("monthly_requests", UNSET))


        def _parse_daily_ai_requests(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        daily_ai_requests = _parse_daily_ai_requests(d.pop("daily_ai_requests", UNSET))


        def _parse_dynamic_pricing_listings(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        dynamic_pricing_listings = _parse_dynamic_pricing_listings(d.pop("dynamic_pricing_listings", UNSET))


        get_usage_tier_response_200_limits = cls(
            monthly_requests=monthly_requests,
            daily_ai_requests=daily_ai_requests,
            dynamic_pricing_listings=dynamic_pricing_listings,
        )


        get_usage_tier_response_200_limits.additional_properties = d
        return get_usage_tier_response_200_limits

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
