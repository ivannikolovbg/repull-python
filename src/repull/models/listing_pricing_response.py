from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.listing_pricing_recommendation import ListingPricingRecommendation
  from ..models.listing_pricing_response_comp_summary_type_0 import ListingPricingResponseCompSummaryType0
  from ..models.listing_pricing_response_date_range import ListingPricingResponseDateRange
  from ..models.listing_pricing_response_listing_type_0 import ListingPricingResponseListingType0





T = TypeVar("T", bound="ListingPricingResponse")



@_attrs_define
class ListingPricingResponse:
    """ 
        Attributes:
            listing_id (str | Unset):
            date_range (ListingPricingResponseDateRange | Unset):
            recommendations (list[ListingPricingRecommendation] | Unset):
            listing (ListingPricingResponseListingType0 | None | Unset): AI-derived base-price context for the listing.
            comp_summary (ListingPricingResponseCompSummaryType0 | None | Unset): 5km comp aggregate (Atlas comp_listings).
     """

    listing_id: str | Unset = UNSET
    date_range: ListingPricingResponseDateRange | Unset = UNSET
    recommendations: list[ListingPricingRecommendation] | Unset = UNSET
    listing: ListingPricingResponseListingType0 | None | Unset = UNSET
    comp_summary: ListingPricingResponseCompSummaryType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.listing_pricing_recommendation import ListingPricingRecommendation
        from ..models.listing_pricing_response_comp_summary_type_0 import ListingPricingResponseCompSummaryType0
        from ..models.listing_pricing_response_date_range import ListingPricingResponseDateRange
        from ..models.listing_pricing_response_listing_type_0 import ListingPricingResponseListingType0
        listing_id = self.listing_id

        date_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.date_range, Unset):
            date_range = self.date_range.to_dict()

        recommendations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.recommendations, Unset):
            recommendations = []
            for recommendations_item_data in self.recommendations:
                recommendations_item = recommendations_item_data.to_dict()
                recommendations.append(recommendations_item)



        listing: dict[str, Any] | None | Unset
        if isinstance(self.listing, Unset):
            listing = UNSET
        elif isinstance(self.listing, ListingPricingResponseListingType0):
            listing = self.listing.to_dict()
        else:
            listing = self.listing

        comp_summary: dict[str, Any] | None | Unset
        if isinstance(self.comp_summary, Unset):
            comp_summary = UNSET
        elif isinstance(self.comp_summary, ListingPricingResponseCompSummaryType0):
            comp_summary = self.comp_summary.to_dict()
        else:
            comp_summary = self.comp_summary


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if date_range is not UNSET:
            field_dict["dateRange"] = date_range
        if recommendations is not UNSET:
            field_dict["recommendations"] = recommendations
        if listing is not UNSET:
            field_dict["listing"] = listing
        if comp_summary is not UNSET:
            field_dict["compSummary"] = comp_summary

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.listing_pricing_recommendation import ListingPricingRecommendation
        from ..models.listing_pricing_response_comp_summary_type_0 import ListingPricingResponseCompSummaryType0
        from ..models.listing_pricing_response_date_range import ListingPricingResponseDateRange
        from ..models.listing_pricing_response_listing_type_0 import ListingPricingResponseListingType0
        d = dict(src_dict)
        listing_id = d.pop("listingId", UNSET)

        _date_range = d.pop("dateRange", UNSET)
        date_range: ListingPricingResponseDateRange | Unset
        if isinstance(_date_range,  Unset):
            date_range = UNSET
        else:
            date_range = ListingPricingResponseDateRange.from_dict(_date_range)




        _recommendations = d.pop("recommendations", UNSET)
        recommendations: list[ListingPricingRecommendation] | Unset = UNSET
        if _recommendations is not UNSET:
            recommendations = []
            for recommendations_item_data in _recommendations:
                recommendations_item = ListingPricingRecommendation.from_dict(recommendations_item_data)



                recommendations.append(recommendations_item)


        def _parse_listing(data: object) -> ListingPricingResponseListingType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                listing_type_0 = ListingPricingResponseListingType0.from_dict(data)



                return listing_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListingPricingResponseListingType0 | None | Unset, data)

        listing = _parse_listing(d.pop("listing", UNSET))


        def _parse_comp_summary(data: object) -> ListingPricingResponseCompSummaryType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                comp_summary_type_0 = ListingPricingResponseCompSummaryType0.from_dict(data)



                return comp_summary_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListingPricingResponseCompSummaryType0 | None | Unset, data)

        comp_summary = _parse_comp_summary(d.pop("compSummary", UNSET))


        listing_pricing_response = cls(
            listing_id=listing_id,
            date_range=date_range,
            recommendations=recommendations,
            listing=listing,
            comp_summary=comp_summary,
        )


        listing_pricing_response.additional_properties = d
        return listing_pricing_response

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
