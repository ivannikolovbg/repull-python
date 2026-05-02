from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.listing_segments_response_level import ListingSegmentsResponseLevel
from ..models.listing_segments_response_my_quality_tier_type_1 import ListingSegmentsResponseMyQualityTierType1
from ..models.listing_segments_response_my_quality_tier_type_2_type_1 import ListingSegmentsResponseMyQualityTierType2Type1
from ..models.listing_segments_response_my_quality_tier_type_3_type_1 import ListingSegmentsResponseMyQualityTierType3Type1
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.listing_quality_tier import ListingQualityTier
  from ..models.listing_segment import ListingSegment
  from ..models.listing_segment_recommendation import ListingSegmentRecommendation
  from ..models.listing_segments_response_scope import ListingSegmentsResponseScope





T = TypeVar("T", bound="ListingSegmentsResponse")



@_attrs_define
class ListingSegmentsResponse:
    """ Returned by `GET /v1/listings/{id}/segments`. Honest about DNA coverage — when no comps in the scope have been DNA-
    scored, returns `totalCompsAnalyzed: 0` plus a `low_dna_coverage` recommendation rather than fabricated data.

        Attributes:
            listing_id (int | Unset):
            level (ListingSegmentsResponseLevel | Unset):
            scope (ListingSegmentsResponseScope | Unset): When `level=comp_set` carries `radiusKm`; when `level=market`
                carries `city`. May be empty when neither could be resolved.
            my_segment (None | str | Unset): The source listing's own `ai_segment` (or null if not yet scored).
            my_quality_tier (ListingSegmentsResponseMyQualityTierType1 | ListingSegmentsResponseMyQualityTierType2Type1 |
                ListingSegmentsResponseMyQualityTierType3Type1 | None | Unset):
            total_comps_analyzed (int | Unset): Number of comps in scope that have a DNA score. `0` is a coverage signal,
                not an error.
            segments (list[ListingSegment] | Unset):
            quality_tiers (list[ListingQualityTier] | Unset):
            recommendations (list[ListingSegmentRecommendation] | Unset):
     """

    listing_id: int | Unset = UNSET
    level: ListingSegmentsResponseLevel | Unset = UNSET
    scope: ListingSegmentsResponseScope | Unset = UNSET
    my_segment: None | str | Unset = UNSET
    my_quality_tier: ListingSegmentsResponseMyQualityTierType1 | ListingSegmentsResponseMyQualityTierType2Type1 | ListingSegmentsResponseMyQualityTierType3Type1 | None | Unset = UNSET
    total_comps_analyzed: int | Unset = UNSET
    segments: list[ListingSegment] | Unset = UNSET
    quality_tiers: list[ListingQualityTier] | Unset = UNSET
    recommendations: list[ListingSegmentRecommendation] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.listing_quality_tier import ListingQualityTier
        from ..models.listing_segment import ListingSegment
        from ..models.listing_segment_recommendation import ListingSegmentRecommendation
        from ..models.listing_segments_response_scope import ListingSegmentsResponseScope
        listing_id = self.listing_id

        level: str | Unset = UNSET
        if not isinstance(self.level, Unset):
            level = self.level.value


        scope: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.to_dict()

        my_segment: None | str | Unset
        if isinstance(self.my_segment, Unset):
            my_segment = UNSET
        else:
            my_segment = self.my_segment

        my_quality_tier: None | str | Unset
        if isinstance(self.my_quality_tier, Unset):
            my_quality_tier = UNSET
        elif isinstance(self.my_quality_tier, ListingSegmentsResponseMyQualityTierType1):
            my_quality_tier = self.my_quality_tier.value
        elif isinstance(self.my_quality_tier, ListingSegmentsResponseMyQualityTierType2Type1):
            my_quality_tier = self.my_quality_tier.value
        elif isinstance(self.my_quality_tier, ListingSegmentsResponseMyQualityTierType3Type1):
            my_quality_tier = self.my_quality_tier.value
        else:
            my_quality_tier = self.my_quality_tier

        total_comps_analyzed = self.total_comps_analyzed

        segments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.segments, Unset):
            segments = []
            for segments_item_data in self.segments:
                segments_item = segments_item_data.to_dict()
                segments.append(segments_item)



        quality_tiers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.quality_tiers, Unset):
            quality_tiers = []
            for quality_tiers_item_data in self.quality_tiers:
                quality_tiers_item = quality_tiers_item_data.to_dict()
                quality_tiers.append(quality_tiers_item)



        recommendations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.recommendations, Unset):
            recommendations = []
            for recommendations_item_data in self.recommendations:
                recommendations_item = recommendations_item_data.to_dict()
                recommendations.append(recommendations_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if level is not UNSET:
            field_dict["level"] = level
        if scope is not UNSET:
            field_dict["scope"] = scope
        if my_segment is not UNSET:
            field_dict["mySegment"] = my_segment
        if my_quality_tier is not UNSET:
            field_dict["myQualityTier"] = my_quality_tier
        if total_comps_analyzed is not UNSET:
            field_dict["totalCompsAnalyzed"] = total_comps_analyzed
        if segments is not UNSET:
            field_dict["segments"] = segments
        if quality_tiers is not UNSET:
            field_dict["qualityTiers"] = quality_tiers
        if recommendations is not UNSET:
            field_dict["recommendations"] = recommendations

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.listing_quality_tier import ListingQualityTier
        from ..models.listing_segment import ListingSegment
        from ..models.listing_segment_recommendation import ListingSegmentRecommendation
        from ..models.listing_segments_response_scope import ListingSegmentsResponseScope
        d = dict(src_dict)
        listing_id = d.pop("listingId", UNSET)

        _level = d.pop("level", UNSET)
        level: ListingSegmentsResponseLevel | Unset
        if isinstance(_level,  Unset):
            level = UNSET
        else:
            level = ListingSegmentsResponseLevel(_level)




        _scope = d.pop("scope", UNSET)
        scope: ListingSegmentsResponseScope | Unset
        if isinstance(_scope,  Unset):
            scope = UNSET
        else:
            scope = ListingSegmentsResponseScope.from_dict(_scope)




        def _parse_my_segment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        my_segment = _parse_my_segment(d.pop("mySegment", UNSET))


        def _parse_my_quality_tier(data: object) -> ListingSegmentsResponseMyQualityTierType1 | ListingSegmentsResponseMyQualityTierType2Type1 | ListingSegmentsResponseMyQualityTierType3Type1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                my_quality_tier_type_1 = ListingSegmentsResponseMyQualityTierType1(data)



                return my_quality_tier_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                my_quality_tier_type_2_type_1 = ListingSegmentsResponseMyQualityTierType2Type1(data)



                return my_quality_tier_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                my_quality_tier_type_3_type_1 = ListingSegmentsResponseMyQualityTierType3Type1(data)



                return my_quality_tier_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListingSegmentsResponseMyQualityTierType1 | ListingSegmentsResponseMyQualityTierType2Type1 | ListingSegmentsResponseMyQualityTierType3Type1 | None | Unset, data)

        my_quality_tier = _parse_my_quality_tier(d.pop("myQualityTier", UNSET))


        total_comps_analyzed = d.pop("totalCompsAnalyzed", UNSET)

        _segments = d.pop("segments", UNSET)
        segments: list[ListingSegment] | Unset = UNSET
        if _segments is not UNSET:
            segments = []
            for segments_item_data in _segments:
                segments_item = ListingSegment.from_dict(segments_item_data)



                segments.append(segments_item)


        _quality_tiers = d.pop("qualityTiers", UNSET)
        quality_tiers: list[ListingQualityTier] | Unset = UNSET
        if _quality_tiers is not UNSET:
            quality_tiers = []
            for quality_tiers_item_data in _quality_tiers:
                quality_tiers_item = ListingQualityTier.from_dict(quality_tiers_item_data)



                quality_tiers.append(quality_tiers_item)


        _recommendations = d.pop("recommendations", UNSET)
        recommendations: list[ListingSegmentRecommendation] | Unset = UNSET
        if _recommendations is not UNSET:
            recommendations = []
            for recommendations_item_data in _recommendations:
                recommendations_item = ListingSegmentRecommendation.from_dict(recommendations_item_data)



                recommendations.append(recommendations_item)


        listing_segments_response = cls(
            listing_id=listing_id,
            level=level,
            scope=scope,
            my_segment=my_segment,
            my_quality_tier=my_quality_tier,
            total_comps_analyzed=total_comps_analyzed,
            segments=segments,
            quality_tiers=quality_tiers,
            recommendations=recommendations,
        )


        listing_segments_response.additional_properties = d
        return listing_segments_response

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
