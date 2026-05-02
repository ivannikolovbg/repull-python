from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.listing_pricing_response_listing_type_0_ai_base_price_factors_type_0 import ListingPricingResponseListingType0AiBasePriceFactorsType0





T = TypeVar("T", bound="ListingPricingResponseListingType0")



@_attrs_define
class ListingPricingResponseListingType0:
    """ AI-derived base-price context for the listing.

        Attributes:
            ai_base_price (float | None | Unset):
            ai_base_price_factors (ListingPricingResponseListingType0AiBasePriceFactorsType0 | None | Unset):
            quality_tier (None | str | Unset):
            segment (None | str | Unset):
            currency (None | str | Unset):
     """

    ai_base_price: float | None | Unset = UNSET
    ai_base_price_factors: ListingPricingResponseListingType0AiBasePriceFactorsType0 | None | Unset = UNSET
    quality_tier: None | str | Unset = UNSET
    segment: None | str | Unset = UNSET
    currency: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.listing_pricing_response_listing_type_0_ai_base_price_factors_type_0 import ListingPricingResponseListingType0AiBasePriceFactorsType0
        ai_base_price: float | None | Unset
        if isinstance(self.ai_base_price, Unset):
            ai_base_price = UNSET
        else:
            ai_base_price = self.ai_base_price

        ai_base_price_factors: dict[str, Any] | None | Unset
        if isinstance(self.ai_base_price_factors, Unset):
            ai_base_price_factors = UNSET
        elif isinstance(self.ai_base_price_factors, ListingPricingResponseListingType0AiBasePriceFactorsType0):
            ai_base_price_factors = self.ai_base_price_factors.to_dict()
        else:
            ai_base_price_factors = self.ai_base_price_factors

        quality_tier: None | str | Unset
        if isinstance(self.quality_tier, Unset):
            quality_tier = UNSET
        else:
            quality_tier = self.quality_tier

        segment: None | str | Unset
        if isinstance(self.segment, Unset):
            segment = UNSET
        else:
            segment = self.segment

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if ai_base_price is not UNSET:
            field_dict["aiBasePrice"] = ai_base_price
        if ai_base_price_factors is not UNSET:
            field_dict["aiBasePriceFactors"] = ai_base_price_factors
        if quality_tier is not UNSET:
            field_dict["qualityTier"] = quality_tier
        if segment is not UNSET:
            field_dict["segment"] = segment
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.listing_pricing_response_listing_type_0_ai_base_price_factors_type_0 import ListingPricingResponseListingType0AiBasePriceFactorsType0
        d = dict(src_dict)
        def _parse_ai_base_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ai_base_price = _parse_ai_base_price(d.pop("aiBasePrice", UNSET))


        def _parse_ai_base_price_factors(data: object) -> ListingPricingResponseListingType0AiBasePriceFactorsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                ai_base_price_factors_type_0 = ListingPricingResponseListingType0AiBasePriceFactorsType0.from_dict(data)



                return ai_base_price_factors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListingPricingResponseListingType0AiBasePriceFactorsType0 | None | Unset, data)

        ai_base_price_factors = _parse_ai_base_price_factors(d.pop("aiBasePriceFactors", UNSET))


        def _parse_quality_tier(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        quality_tier = _parse_quality_tier(d.pop("qualityTier", UNSET))


        def _parse_segment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        segment = _parse_segment(d.pop("segment", UNSET))


        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))


        listing_pricing_response_listing_type_0 = cls(
            ai_base_price=ai_base_price,
            ai_base_price_factors=ai_base_price_factors,
            quality_tier=quality_tier,
            segment=segment,
            currency=currency,
        )


        listing_pricing_response_listing_type_0.additional_properties = d
        return listing_pricing_response_listing_type_0

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
