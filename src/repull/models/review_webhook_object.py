from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.review_webhook_object_reviewer_role import ReviewWebhookObjectReviewerRole
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="ReviewWebhookObject")



@_attrs_define
class ReviewWebhookObject:
    """ Lightweight review snapshot delivered as `data.object` on `review.*` events. Fetch the full review (category
    ratings, public text, private feedback, response body) via `GET /v1/reviews/{id}`.

        Attributes:
            id (int): Repull-internal review id. Pass to `GET /v1/reviews/{id}`. Example: 90210.
            channel (None | str): Source channel the review came from. Example: airbnb.
            customer_id (int): Workspace (customer) id. Example: 1.
            reviewer_role (ReviewWebhookObjectReviewerRole): Who wrote the review — `guest` (about the host/property) or
                `host` (about the guest). Example: guest.
            listing_id (int | None | Unset): Repull listing id the review is about. Example: 5668.
            reservation_id (int | None | Unset): Repull reservation id the review is attached to, if known. Example: 215906.
            rating (int | None | Unset): Overall star rating, if present. Example: 5.
            submitted_at (datetime.datetime | None | Unset): When the review was submitted on the source channel. Example:
                2026-05-01T09:00:00.000Z.
     """

    id: int
    channel: None | str
    customer_id: int
    reviewer_role: ReviewWebhookObjectReviewerRole
    listing_id: int | None | Unset = UNSET
    reservation_id: int | None | Unset = UNSET
    rating: int | None | Unset = UNSET
    submitted_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        channel: None | str
        channel = self.channel

        customer_id = self.customer_id

        reviewer_role = self.reviewer_role.value

        listing_id: int | None | Unset
        if isinstance(self.listing_id, Unset):
            listing_id = UNSET
        else:
            listing_id = self.listing_id

        reservation_id: int | None | Unset
        if isinstance(self.reservation_id, Unset):
            reservation_id = UNSET
        else:
            reservation_id = self.reservation_id

        rating: int | None | Unset
        if isinstance(self.rating, Unset):
            rating = UNSET
        else:
            rating = self.rating

        submitted_at: None | str | Unset
        if isinstance(self.submitted_at, Unset):
            submitted_at = UNSET
        elif isinstance(self.submitted_at, datetime.datetime):
            submitted_at = self.submitted_at.isoformat()
        else:
            submitted_at = self.submitted_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "channel": channel,
            "customerId": customer_id,
            "reviewerRole": reviewer_role,
        })
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if reservation_id is not UNSET:
            field_dict["reservationId"] = reservation_id
        if rating is not UNSET:
            field_dict["rating"] = rating
        if submitted_at is not UNSET:
            field_dict["submittedAt"] = submitted_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_channel(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        channel = _parse_channel(d.pop("channel"))


        customer_id = d.pop("customerId")

        reviewer_role = ReviewWebhookObjectReviewerRole(d.pop("reviewerRole"))




        def _parse_listing_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        listing_id = _parse_listing_id(d.pop("listingId", UNSET))


        def _parse_reservation_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        reservation_id = _parse_reservation_id(d.pop("reservationId", UNSET))


        def _parse_rating(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rating = _parse_rating(d.pop("rating", UNSET))


        def _parse_submitted_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                submitted_at_type_0 = isoparse(data)



                return submitted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        submitted_at = _parse_submitted_at(d.pop("submittedAt", UNSET))


        review_webhook_object = cls(
            id=id,
            channel=channel,
            customer_id=customer_id,
            reviewer_role=reviewer_role,
            listing_id=listing_id,
            reservation_id=reservation_id,
            rating=rating,
            submitted_at=submitted_at,
        )


        review_webhook_object.additional_properties = d
        return review_webhook_object

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
