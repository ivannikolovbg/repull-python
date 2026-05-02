from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.listing_pricing_recommendation_status import ListingPricingRecommendationStatus
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.listing_pricing_recommendation_factors import ListingPricingRecommendationFactors





T = TypeVar("T", bound="ListingPricingRecommendation")



@_attrs_define
class ListingPricingRecommendation:
    """ A pricing recommendation for one date in the listing's calendar window.

        Attributes:
            date (datetime.date | Unset):  Example: 2026-05-14.
            current_price (float | None | Unset): Current calendar price (from Vanio listings_calendar_days) before applying
                the recommendation.
            recommended_price (float | Unset): Atlas model's recommended price.
            min_price (float | None | Unset):
            max_price (float | None | Unset):
            currency (str | Unset):  Example: USD.
            confidence (float | Unset): Model confidence in [0, 1].
            booking_probability (float | None | Unset): Expected booking probability for the date at the recommended price.
            expected_revenue (float | None | Unset):
            factors (ListingPricingRecommendationFactors | Unset): Free-form JSON of model factors (comp distance, event
                boost, weekend, demand, etc.).
            status (ListingPricingRecommendationStatus | Unset): Lifecycle state.
            model_version (str | Unset):
            generated_at (datetime.datetime | Unset):
     """

    date: datetime.date | Unset = UNSET
    current_price: float | None | Unset = UNSET
    recommended_price: float | Unset = UNSET
    min_price: float | None | Unset = UNSET
    max_price: float | None | Unset = UNSET
    currency: str | Unset = UNSET
    confidence: float | Unset = UNSET
    booking_probability: float | None | Unset = UNSET
    expected_revenue: float | None | Unset = UNSET
    factors: ListingPricingRecommendationFactors | Unset = UNSET
    status: ListingPricingRecommendationStatus | Unset = UNSET
    model_version: str | Unset = UNSET
    generated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.listing_pricing_recommendation_factors import ListingPricingRecommendationFactors
        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        current_price: float | None | Unset
        if isinstance(self.current_price, Unset):
            current_price = UNSET
        else:
            current_price = self.current_price

        recommended_price = self.recommended_price

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

        currency = self.currency

        confidence = self.confidence

        booking_probability: float | None | Unset
        if isinstance(self.booking_probability, Unset):
            booking_probability = UNSET
        else:
            booking_probability = self.booking_probability

        expected_revenue: float | None | Unset
        if isinstance(self.expected_revenue, Unset):
            expected_revenue = UNSET
        else:
            expected_revenue = self.expected_revenue

        factors: dict[str, Any] | Unset = UNSET
        if not isinstance(self.factors, Unset):
            factors = self.factors.to_dict()

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        model_version = self.model_version

        generated_at: str | Unset = UNSET
        if not isinstance(self.generated_at, Unset):
            generated_at = self.generated_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if date is not UNSET:
            field_dict["date"] = date
        if current_price is not UNSET:
            field_dict["currentPrice"] = current_price
        if recommended_price is not UNSET:
            field_dict["recommendedPrice"] = recommended_price
        if min_price is not UNSET:
            field_dict["minPrice"] = min_price
        if max_price is not UNSET:
            field_dict["maxPrice"] = max_price
        if currency is not UNSET:
            field_dict["currency"] = currency
        if confidence is not UNSET:
            field_dict["confidence"] = confidence
        if booking_probability is not UNSET:
            field_dict["bookingProbability"] = booking_probability
        if expected_revenue is not UNSET:
            field_dict["expectedRevenue"] = expected_revenue
        if factors is not UNSET:
            field_dict["factors"] = factors
        if status is not UNSET:
            field_dict["status"] = status
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if generated_at is not UNSET:
            field_dict["generatedAt"] = generated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.listing_pricing_recommendation_factors import ListingPricingRecommendationFactors
        d = dict(src_dict)
        _date = d.pop("date", UNSET)
        date: datetime.date | Unset
        if isinstance(_date,  Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()




        def _parse_current_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        current_price = _parse_current_price(d.pop("currentPrice", UNSET))


        recommended_price = d.pop("recommendedPrice", UNSET)

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


        currency = d.pop("currency", UNSET)

        confidence = d.pop("confidence", UNSET)

        def _parse_booking_probability(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        booking_probability = _parse_booking_probability(d.pop("bookingProbability", UNSET))


        def _parse_expected_revenue(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        expected_revenue = _parse_expected_revenue(d.pop("expectedRevenue", UNSET))


        _factors = d.pop("factors", UNSET)
        factors: ListingPricingRecommendationFactors | Unset
        if isinstance(_factors,  Unset):
            factors = UNSET
        else:
            factors = ListingPricingRecommendationFactors.from_dict(_factors)




        _status = d.pop("status", UNSET)
        status: ListingPricingRecommendationStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = ListingPricingRecommendationStatus(_status)




        model_version = d.pop("modelVersion", UNSET)

        _generated_at = d.pop("generatedAt", UNSET)
        generated_at: datetime.datetime | Unset
        if isinstance(_generated_at,  Unset):
            generated_at = UNSET
        else:
            generated_at = isoparse(_generated_at)




        listing_pricing_recommendation = cls(
            date=date,
            current_price=current_price,
            recommended_price=recommended_price,
            min_price=min_price,
            max_price=max_price,
            currency=currency,
            confidence=confidence,
            booking_probability=booking_probability,
            expected_revenue=expected_revenue,
            factors=factors,
            status=status,
            model_version=model_version,
            generated_at=generated_at,
        )


        listing_pricing_recommendation.additional_properties = d
        return listing_pricing_recommendation

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
