from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.submit_vrbo_guest_review_body_category_ratings_item_category import SubmitVrboGuestReviewBodyCategoryRatingsItemCategory
from ..types import UNSET, Unset






T = TypeVar("T", bound="SubmitVrboGuestReviewBodyCategoryRatingsItem")



@_attrs_define
class SubmitVrboGuestReviewBodyCategoryRatingsItem:
    """ 
        Attributes:
            category (SubmitVrboGuestReviewBodyCategoryRatingsItemCategory | Unset):
            rating (int | Unset):
     """

    category: SubmitVrboGuestReviewBodyCategoryRatingsItemCategory | Unset = UNSET
    rating: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        category: str | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value


        rating = self.rating


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if category is not UNSET:
            field_dict["category"] = category
        if rating is not UNSET:
            field_dict["rating"] = rating

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _category = d.pop("category", UNSET)
        category: SubmitVrboGuestReviewBodyCategoryRatingsItemCategory | Unset
        if isinstance(_category,  Unset):
            category = UNSET
        else:
            category = SubmitVrboGuestReviewBodyCategoryRatingsItemCategory(_category)




        rating = d.pop("rating", UNSET)

        submit_vrbo_guest_review_body_category_ratings_item = cls(
            category=category,
            rating=rating,
        )


        submit_vrbo_guest_review_body_category_ratings_item.additional_properties = d
        return submit_vrbo_guest_review_body_category_ratings_item

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
