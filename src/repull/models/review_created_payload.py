from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.review_webhook_object import ReviewWebhookObject





T = TypeVar("T", bound="ReviewCreatedPayload")



@_attrs_define
class ReviewCreatedPayload:
    """ Payload for `review.created`. A new review was received on a reservation. `data.object.reviewerRole` disambiguates
    guest vs host authorship.

        Attributes:
            object_ (ReviewWebhookObject): Lightweight review snapshot delivered as `data.object` on `review.*` events.
                Fetch the full review (category ratings, public text, private feedback, response body) via `GET
                /v1/reviews/{id}`.
     """

    object_: ReviewWebhookObject
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.review_webhook_object import ReviewWebhookObject
        object_ = self.object_.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "object": object_,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.review_webhook_object import ReviewWebhookObject
        d = dict(src_dict)
        object_ = ReviewWebhookObject.from_dict(d.pop("object"))




        review_created_payload = cls(
            object_=object_,
        )


        review_created_payload.additional_properties = d
        return review_created_payload

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
