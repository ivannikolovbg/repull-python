from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.submit_vrbo_guest_review_body_category_ratings_item import SubmitVrboGuestReviewBodyCategoryRatingsItem





T = TypeVar("T", bound="SubmitVrboGuestReviewBody")



@_attrs_define
class SubmitVrboGuestReviewBody:
    """ 
        Attributes:
            rating (int | Unset):
            category_ratings (list[SubmitVrboGuestReviewBodyCategoryRatingsItem] | Unset):
            is_reviewee_recommended (bool | Unset):
     """

    rating: int | Unset = UNSET
    category_ratings: list[SubmitVrboGuestReviewBodyCategoryRatingsItem] | Unset = UNSET
    is_reviewee_recommended: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.submit_vrbo_guest_review_body_category_ratings_item import SubmitVrboGuestReviewBodyCategoryRatingsItem
        rating = self.rating

        category_ratings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.category_ratings, Unset):
            category_ratings = []
            for category_ratings_item_data in self.category_ratings:
                category_ratings_item = category_ratings_item_data.to_dict()
                category_ratings.append(category_ratings_item)



        is_reviewee_recommended = self.is_reviewee_recommended


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if rating is not UNSET:
            field_dict["rating"] = rating
        if category_ratings is not UNSET:
            field_dict["categoryRatings"] = category_ratings
        if is_reviewee_recommended is not UNSET:
            field_dict["isRevieweeRecommended"] = is_reviewee_recommended

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.submit_vrbo_guest_review_body_category_ratings_item import SubmitVrboGuestReviewBodyCategoryRatingsItem
        d = dict(src_dict)
        rating = d.pop("rating", UNSET)

        _category_ratings = d.pop("categoryRatings", UNSET)
        category_ratings: list[SubmitVrboGuestReviewBodyCategoryRatingsItem] | Unset = UNSET
        if _category_ratings is not UNSET:
            category_ratings = []
            for category_ratings_item_data in _category_ratings:
                category_ratings_item = SubmitVrboGuestReviewBodyCategoryRatingsItem.from_dict(category_ratings_item_data)



                category_ratings.append(category_ratings_item)


        is_reviewee_recommended = d.pop("isRevieweeRecommended", UNSET)

        submit_vrbo_guest_review_body = cls(
            rating=rating,
            category_ratings=category_ratings,
            is_reviewee_recommended=is_reviewee_recommended,
        )


        submit_vrbo_guest_review_body.additional_properties = d
        return submit_vrbo_guest_review_body

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
