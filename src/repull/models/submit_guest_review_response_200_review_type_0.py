from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="SubmitGuestReviewResponse200ReviewType0")



@_attrs_define
class SubmitGuestReviewResponse200ReviewType0:
    """ Airbnb: the review as stored after the submission — the same object `GET /v1/reviews/{id}` returns, with
    `publicReview`, `rating`, `categories` and `submittedAt` set. It can stay `hidden` until the guest reviews too.

     """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        submit_guest_review_response_200_review_type_0 = cls(
        )


        submit_guest_review_response_200_review_type_0.additional_properties = d
        return submit_guest_review_response_200_review_type_0

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
