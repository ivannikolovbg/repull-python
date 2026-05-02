from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ListingPricingResponseCompSummaryType0")



@_attrs_define
class ListingPricingResponseCompSummaryType0:
    """ 5km comp aggregate (Atlas comp_listings).

        Attributes:
            count (int | Unset):
            avg_price (float | None | Unset):
            min_price (float | None | Unset):
            max_price (float | None | Unset):
     """

    count: int | Unset = UNSET
    avg_price: float | None | Unset = UNSET
    min_price: float | None | Unset = UNSET
    max_price: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        count = self.count

        avg_price: float | None | Unset
        if isinstance(self.avg_price, Unset):
            avg_price = UNSET
        else:
            avg_price = self.avg_price

        min_price: float | None | Unset
        if isinstance(self.min_price, Unset):
            min_price = UNSET
        else:
            min_price = self.min_price

        max_price: float | None | Unset
        if isinstance(self.max_price, Unset):
            max_price = UNSET
        else:
            max_price = self.max_price


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if count is not UNSET:
            field_dict["count"] = count
        if avg_price is not UNSET:
            field_dict["avgPrice"] = avg_price
        if min_price is not UNSET:
            field_dict["minPrice"] = min_price
        if max_price is not UNSET:
            field_dict["maxPrice"] = max_price

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count", UNSET)

        def _parse_avg_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        avg_price = _parse_avg_price(d.pop("avgPrice", UNSET))


        def _parse_min_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        min_price = _parse_min_price(d.pop("minPrice", UNSET))


        def _parse_max_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_price = _parse_max_price(d.pop("maxPrice", UNSET))


        listing_pricing_response_comp_summary_type_0 = cls(
            count=count,
            avg_price=avg_price,
            min_price=min_price,
            max_price=max_price,
        )


        listing_pricing_response_comp_summary_type_0.additional_properties = d
        return listing_pricing_response_comp_summary_type_0

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
