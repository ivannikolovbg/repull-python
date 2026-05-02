from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="MarketDetailResponseSupplyTrendItem")



@_attrs_define
class MarketDetailResponseSupplyTrendItem:
    """ 
        Attributes:
            month (str | Unset):  Example: 2026-04.
            new_listings (int | Unset):
     """

    month: str | Unset = UNSET
    new_listings: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        month = self.month

        new_listings = self.new_listings


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if month is not UNSET:
            field_dict["month"] = month
        if new_listings is not UNSET:
            field_dict["new_listings"] = new_listings

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        month = d.pop("month", UNSET)

        new_listings = d.pop("new_listings", UNSET)

        market_detail_response_supply_trend_item = cls(
            month=month,
            new_listings=new_listings,
        )


        market_detail_response_supply_trend_item.additional_properties = d
        return market_detail_response_supply_trend_item

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
