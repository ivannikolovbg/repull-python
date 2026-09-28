from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.airbnb_host_review_submit_category_ratings_item import AirbnbHostReviewSubmitCategoryRatingsItem





T = TypeVar("T", bound="AirbnbHostReviewSubmit")



@_attrs_define
class AirbnbHostReviewSubmit:
    """ Your review of a guest. Airbnb requires `publicReview`, `isRevieweeRecommended`, and a rating for each of
    cleanliness, communication and respect_house_rules — through `rating`, `categoryRatings`, or both. Submitting
    publishes it and is final.

        Example:
            {'publicReview': 'Joanne was a great guest. The space was kept clean and communication was clear.', 'rating': 5,
                'categoryRatings': [{'category': 'cleanliness', 'rating': 5, 'comment': 'Left it spotless'}], 'privateFeedback':
                'Thanks for being such a considerate guest!', 'isRevieweeRecommended': True}

        Attributes:
            public_review (str): Shown publicly on the guest's profile. `comment` is accepted as an alias. Example: Joanne
                was a great guest. The space was kept clean and communication was clear..
            is_reviewee_recommended (bool): Required. Whether you would host this guest again.
            rating (int | Unset): Used for every category not rated in `categoryRatings`. Example: 5.
            category_ratings (list[AirbnbHostReviewSubmitCategoryRatingsItem] | Unset): Per-category scores. Categories not
                listed take `rating`; without `rating`, all three must be listed.
            private_feedback (str | Unset): Optional. A note to the guest that is not published.
     """

    public_review: str
    is_reviewee_recommended: bool
    rating: int | Unset = UNSET
    category_ratings: list[AirbnbHostReviewSubmitCategoryRatingsItem] | Unset = UNSET
    private_feedback: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.airbnb_host_review_submit_category_ratings_item import AirbnbHostReviewSubmitCategoryRatingsItem
        public_review = self.public_review

        is_reviewee_recommended = self.is_reviewee_recommended

        rating = self.rating

        category_ratings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.category_ratings, Unset):
            category_ratings = []
            for category_ratings_item_data in self.category_ratings:
                category_ratings_item = category_ratings_item_data.to_dict()
                category_ratings.append(category_ratings_item)



        private_feedback = self.private_feedback


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "publicReview": public_review,
            "isRevieweeRecommended": is_reviewee_recommended,
        })
        if rating is not UNSET:
            field_dict["rating"] = rating
        if category_ratings is not UNSET:
            field_dict["categoryRatings"] = category_ratings
        if private_feedback is not UNSET:
            field_dict["privateFeedback"] = private_feedback

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.airbnb_host_review_submit_category_ratings_item import AirbnbHostReviewSubmitCategoryRatingsItem
        d = dict(src_dict)
        public_review = d.pop("publicReview")

        is_reviewee_recommended = d.pop("isRevieweeRecommended")

        rating = d.pop("rating", UNSET)

        _category_ratings = d.pop("categoryRatings", UNSET)
        category_ratings: list[AirbnbHostReviewSubmitCategoryRatingsItem] | Unset = UNSET
        if _category_ratings is not UNSET:
            category_ratings = []
            for category_ratings_item_data in _category_ratings:
                category_ratings_item = AirbnbHostReviewSubmitCategoryRatingsItem.from_dict(category_ratings_item_data)



                category_ratings.append(category_ratings_item)


        private_feedback = d.pop("privateFeedback", UNSET)

        airbnb_host_review_submit = cls(
            public_review=public_review,
            is_reviewee_recommended=is_reviewee_recommended,
            rating=rating,
            category_ratings=category_ratings,
            private_feedback=private_feedback,
        )


        airbnb_host_review_submit.additional_properties = d
        return airbnb_host_review_submit

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
