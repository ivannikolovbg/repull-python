from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="MarketsOverviewResponseTotals")



@_attrs_define
class MarketsOverviewResponseTotals:
    """ 
        Attributes:
            my_listings (int | Unset):
            markets (int | Unset):
            total_competitors (int | Unset):
     """

    my_listings: int | Unset = UNSET
    markets: int | Unset = UNSET
    total_competitors: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        my_listings = self.my_listings

        markets = self.markets

        total_competitors = self.total_competitors


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if my_listings is not UNSET:
            field_dict["myListings"] = my_listings
        if markets is not UNSET:
            field_dict["markets"] = markets
        if total_competitors is not UNSET:
            field_dict["totalCompetitors"] = total_competitors

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        my_listings = d.pop("myListings", UNSET)

        markets = d.pop("markets", UNSET)

        total_competitors = d.pop("totalCompetitors", UNSET)

        markets_overview_response_totals = cls(
            my_listings=my_listings,
            markets=markets,
            total_competitors=total_competitors,
        )


        markets_overview_response_totals.additional_properties = d
        return markets_overview_response_totals

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
