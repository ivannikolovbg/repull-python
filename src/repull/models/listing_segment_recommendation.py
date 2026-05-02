from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.listing_segment_recommendation_kind import ListingSegmentRecommendationKind
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.listing_segment_recommendation_evidence_type_0 import ListingSegmentRecommendationEvidenceType0





T = TypeVar("T", bound="ListingSegmentRecommendation")



@_attrs_define
class ListingSegmentRecommendation:
    """ Structural observation about the segment landscape — not LLM-generated.

        Attributes:
            kind (ListingSegmentRecommendationKind | Unset): Stable identifier for the recommendation kind. SDKs can switch
                on this safely.
            message (str | Unset):
            evidence (ListingSegmentRecommendationEvidenceType0 | None | Unset):
     """

    kind: ListingSegmentRecommendationKind | Unset = UNSET
    message: str | Unset = UNSET
    evidence: ListingSegmentRecommendationEvidenceType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.listing_segment_recommendation_evidence_type_0 import ListingSegmentRecommendationEvidenceType0
        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value


        message = self.message

        evidence: dict[str, Any] | None | Unset
        if isinstance(self.evidence, Unset):
            evidence = UNSET
        elif isinstance(self.evidence, ListingSegmentRecommendationEvidenceType0):
            evidence = self.evidence.to_dict()
        else:
            evidence = self.evidence


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if kind is not UNSET:
            field_dict["kind"] = kind
        if message is not UNSET:
            field_dict["message"] = message
        if evidence is not UNSET:
            field_dict["evidence"] = evidence

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.listing_segment_recommendation_evidence_type_0 import ListingSegmentRecommendationEvidenceType0
        d = dict(src_dict)
        _kind = d.pop("kind", UNSET)
        kind: ListingSegmentRecommendationKind | Unset
        if isinstance(_kind,  Unset):
            kind = UNSET
        else:
            kind = ListingSegmentRecommendationKind(_kind)




        message = d.pop("message", UNSET)

        def _parse_evidence(data: object) -> ListingSegmentRecommendationEvidenceType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                evidence_type_0 = ListingSegmentRecommendationEvidenceType0.from_dict(data)



                return evidence_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListingSegmentRecommendationEvidenceType0 | None | Unset, data)

        evidence = _parse_evidence(d.pop("evidence", UNSET))


        listing_segment_recommendation = cls(
            kind=kind,
            message=message,
            evidence=evidence,
        )


        listing_segment_recommendation.additional_properties = d
        return listing_segment_recommendation

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
