from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.listing_quality_tier_tier import ListingQualityTierTier
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ListingQualityTier")



@_attrs_define
class ListingQualityTier:
    """ 
        Attributes:
            tier (ListingQualityTierTier | Unset):
            share_pct (float | Unset):
            avg_adr (float | None | Unset):
            sample_size (int | Unset):
     """

    tier: ListingQualityTierTier | Unset = UNSET
    share_pct: float | Unset = UNSET
    avg_adr: float | None | Unset = UNSET
    sample_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        tier: str | Unset = UNSET
        if not isinstance(self.tier, Unset):
            tier = self.tier.value


        share_pct = self.share_pct

        avg_adr: float | None | Unset
        if isinstance(self.avg_adr, Unset):
            avg_adr = UNSET
        else:
            avg_adr = self.avg_adr

        sample_size = self.sample_size


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if tier is not UNSET:
            field_dict["tier"] = tier
        if share_pct is not UNSET:
            field_dict["sharePct"] = share_pct
        if avg_adr is not UNSET:
            field_dict["avgAdr"] = avg_adr
        if sample_size is not UNSET:
            field_dict["sampleSize"] = sample_size

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _tier = d.pop("tier", UNSET)
        tier: ListingQualityTierTier | Unset
        if isinstance(_tier,  Unset):
            tier = UNSET
        else:
            tier = ListingQualityTierTier(_tier)




        share_pct = d.pop("sharePct", UNSET)

        def _parse_avg_adr(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        avg_adr = _parse_avg_adr(d.pop("avgAdr", UNSET))


        sample_size = d.pop("sampleSize", UNSET)

        listing_quality_tier = cls(
            tier=tier,
            share_pct=share_pct,
            avg_adr=avg_adr,
            sample_size=sample_size,
        )


        listing_quality_tier.additional_properties = d
        return listing_quality_tier

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
