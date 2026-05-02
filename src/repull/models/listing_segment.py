from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.listing_segment_quality_tier_type_1 import ListingSegmentQualityTierType1
from ..models.listing_segment_quality_tier_type_2_type_1 import ListingSegmentQualityTierType2Type1
from ..models.listing_segment_quality_tier_type_3_type_1 import ListingSegmentQualityTierType3Type1
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ListingSegment")



@_attrs_define
class ListingSegment:
    """ One Atlas DNA segment (e.g. `upscale-modern-2br`) with share + ADR aggregates across the scoped comp set or market.

        Attributes:
            name (str | Unset):  Example: upscale-modern-2br.
            share_pct (float | Unset): Percent of analyzed comps in the scope that fall in this segment.
            sample_size (int | Unset):
            avg_adr_in_segment (float | None | Unset):
            currency (None | str | Unset):
            quality_tier (ListingSegmentQualityTierType1 | ListingSegmentQualityTierType2Type1 |
                ListingSegmentQualityTierType3Type1 | None | Unset):
            design_style (None | str | Unset): Decomposed style token (e.g. `modern`, `mid-century`).
            bedrooms (int | None | Unset): Decomposed bedroom count. `0` indicates studio.
            my_listing_match (bool | Unset): True when the source listing's `ai_segment` matches this segment.
     """

    name: str | Unset = UNSET
    share_pct: float | Unset = UNSET
    sample_size: int | Unset = UNSET
    avg_adr_in_segment: float | None | Unset = UNSET
    currency: None | str | Unset = UNSET
    quality_tier: ListingSegmentQualityTierType1 | ListingSegmentQualityTierType2Type1 | ListingSegmentQualityTierType3Type1 | None | Unset = UNSET
    design_style: None | str | Unset = UNSET
    bedrooms: int | None | Unset = UNSET
    my_listing_match: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        share_pct = self.share_pct

        sample_size = self.sample_size

        avg_adr_in_segment: float | None | Unset
        if isinstance(self.avg_adr_in_segment, Unset):
            avg_adr_in_segment = UNSET
        else:
            avg_adr_in_segment = self.avg_adr_in_segment

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        quality_tier: None | str | Unset
        if isinstance(self.quality_tier, Unset):
            quality_tier = UNSET
        elif isinstance(self.quality_tier, ListingSegmentQualityTierType1):
            quality_tier = self.quality_tier.value
        elif isinstance(self.quality_tier, ListingSegmentQualityTierType2Type1):
            quality_tier = self.quality_tier.value
        elif isinstance(self.quality_tier, ListingSegmentQualityTierType3Type1):
            quality_tier = self.quality_tier.value
        else:
            quality_tier = self.quality_tier

        design_style: None | str | Unset
        if isinstance(self.design_style, Unset):
            design_style = UNSET
        else:
            design_style = self.design_style

        bedrooms: int | None | Unset
        if isinstance(self.bedrooms, Unset):
            bedrooms = UNSET
        else:
            bedrooms = self.bedrooms

        my_listing_match = self.my_listing_match


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if share_pct is not UNSET:
            field_dict["share_pct"] = share_pct
        if sample_size is not UNSET:
            field_dict["sample_size"] = sample_size
        if avg_adr_in_segment is not UNSET:
            field_dict["avg_adr_in_segment"] = avg_adr_in_segment
        if currency is not UNSET:
            field_dict["currency"] = currency
        if quality_tier is not UNSET:
            field_dict["quality_tier"] = quality_tier
        if design_style is not UNSET:
            field_dict["design_style"] = design_style
        if bedrooms is not UNSET:
            field_dict["bedrooms"] = bedrooms
        if my_listing_match is not UNSET:
            field_dict["my_listing_match"] = my_listing_match

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        share_pct = d.pop("share_pct", UNSET)

        sample_size = d.pop("sample_size", UNSET)

        def _parse_avg_adr_in_segment(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        avg_adr_in_segment = _parse_avg_adr_in_segment(d.pop("avg_adr_in_segment", UNSET))


        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))


        def _parse_quality_tier(data: object) -> ListingSegmentQualityTierType1 | ListingSegmentQualityTierType2Type1 | ListingSegmentQualityTierType3Type1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                quality_tier_type_1 = ListingSegmentQualityTierType1(data)



                return quality_tier_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                quality_tier_type_2_type_1 = ListingSegmentQualityTierType2Type1(data)



                return quality_tier_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                quality_tier_type_3_type_1 = ListingSegmentQualityTierType3Type1(data)



                return quality_tier_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListingSegmentQualityTierType1 | ListingSegmentQualityTierType2Type1 | ListingSegmentQualityTierType3Type1 | None | Unset, data)

        quality_tier = _parse_quality_tier(d.pop("quality_tier", UNSET))


        def _parse_design_style(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        design_style = _parse_design_style(d.pop("design_style", UNSET))


        def _parse_bedrooms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        bedrooms = _parse_bedrooms(d.pop("bedrooms", UNSET))


        my_listing_match = d.pop("my_listing_match", UNSET)

        listing_segment = cls(
            name=name,
            share_pct=share_pct,
            sample_size=sample_size,
            avg_adr_in_segment=avg_adr_in_segment,
            currency=currency,
            quality_tier=quality_tier,
            design_style=design_style,
            bedrooms=bedrooms,
            my_listing_match=my_listing_match,
        )


        listing_segment.additional_properties = d
        return listing_segment

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
