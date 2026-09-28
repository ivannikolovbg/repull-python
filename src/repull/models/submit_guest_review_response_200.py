from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SubmitGuestReviewResponse200")



@_attrs_define
class SubmitGuestReviewResponse200:
    """ 
        Attributes:
            id (str | Unset):
            external_review_id (str | Unset):
            submitted (bool | Unset):
     """

    id: str | Unset = UNSET
    external_review_id: str | Unset = UNSET
    submitted: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        external_review_id = self.external_review_id

        submitted = self.submitted


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

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        external_review_id = d.pop("externalReviewId", UNSET)

        submitted = d.pop("submitted", UNSET)

        submit_guest_review_response_200 = cls(
            id=id,
            external_review_id=external_review_id,
            submitted=submitted,
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
