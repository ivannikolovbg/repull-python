from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="ReplyBookingReviewBody")



@_attrs_define
class ReplyBookingReviewBody:
    """ 
        Attributes:
            property_id (str): Booking.com hotel/property id.
            review_id (str): Booking.com review id (from `GET /v1/channels/booking/reviews`).
            response (str): Public host reply text.
     """

    property_id: str
    review_id: str
    response: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        property_id = self.property_id

        review_id = self.review_id

        response = self.response


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "property_id": property_id,
            "review_id": review_id,
            "response": response,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        property_id = d.pop("property_id")

        review_id = d.pop("review_id")

        response = d.pop("response")

        reply_booking_review_body = cls(
            property_id=property_id,
            review_id=review_id,
            response=response,
        )


        reply_booking_review_body.additional_properties = d
        return reply_booking_review_body

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
