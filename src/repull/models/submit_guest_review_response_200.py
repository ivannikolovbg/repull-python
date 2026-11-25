from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.submit_guest_review_response_200_rating import SubmitGuestReviewResponse200Rating
  from ..models.submit_guest_review_response_200_review_type_0 import SubmitGuestReviewResponse200ReviewType0





T = TypeVar("T", bound="SubmitGuestReviewResponse200")



@_attrs_define
class SubmitGuestReviewResponse200:
    """ 
        Attributes:
            id (str | Unset):
            external_review_id (str | Unset):
            submitted (bool | Unset):
            review (None | SubmitGuestReviewResponse200ReviewType0 | Unset): Airbnb: the review as stored after the
                submission — the same object `GET /v1/reviews/{id}` returns, with `publicReview`, `rating`, `categories` and
                `submittedAt` set. It can stay `hidden` until the guest reviews too.
            platform (str | Unset): `vrbo` for a Vrbo rating.
            rating (SubmitGuestReviewResponse200Rating | Unset): Vrbo: the rating as sent to Vrbo.
     """

    id: str | Unset = UNSET
    external_review_id: str | Unset = UNSET
    submitted: bool | Unset = UNSET
    review: None | SubmitGuestReviewResponse200ReviewType0 | Unset = UNSET
    platform: str | Unset = UNSET
    rating: SubmitGuestReviewResponse200Rating | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.submit_guest_review_response_200_rating import SubmitGuestReviewResponse200Rating
        from ..models.submit_guest_review_response_200_review_type_0 import SubmitGuestReviewResponse200ReviewType0
        id = self.id

        external_review_id = self.external_review_id

        submitted = self.submitted

        review: dict[str, Any] | None | Unset
        if isinstance(self.review, Unset):
            review = UNSET
        elif isinstance(self.review, SubmitGuestReviewResponse200ReviewType0):
            review = self.review.to_dict()
        else:
            review = self.review

        platform = self.platform

        rating: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rating, Unset):
            rating = self.rating.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if external_review_id is not UNSET:
            field_dict["externalReviewId"] = external_review_id
        if submitted is not UNSET:
            field_dict["submitted"] = submitted
        if review is not UNSET:
            field_dict["review"] = review
        if platform is not UNSET:
            field_dict["platform"] = platform
        if rating is not UNSET:
            field_dict["rating"] = rating

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.submit_guest_review_response_200_rating import SubmitGuestReviewResponse200Rating
        from ..models.submit_guest_review_response_200_review_type_0 import SubmitGuestReviewResponse200ReviewType0
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        external_review_id = d.pop("externalReviewId", UNSET)

        submitted = d.pop("submitted", UNSET)

        def _parse_review(data: object) -> None | SubmitGuestReviewResponse200ReviewType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                review_type_0 = SubmitGuestReviewResponse200ReviewType0.from_dict(data)



                return review_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SubmitGuestReviewResponse200ReviewType0 | Unset, data)

        review = _parse_review(d.pop("review", UNSET))


        platform = d.pop("platform", UNSET)

        _rating = d.pop("rating", UNSET)
        rating: SubmitGuestReviewResponse200Rating | Unset
        if isinstance(_rating,  Unset):
            rating = UNSET
        else:
            rating = SubmitGuestReviewResponse200Rating.from_dict(_rating)




        submit_guest_review_response_200 = cls(
            id=id,
            external_review_id=external_review_id,
            submitted=submitted,
            review=review,
            platform=platform,
            rating=rating,
        )


        submit_guest_review_response_200.additional_properties = d
        return submit_guest_review_response_200

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
