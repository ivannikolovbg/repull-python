from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.review_platform import ReviewPlatform
from ..models.review_reviewer_role import ReviewReviewerRole
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.review_category import ReviewCategory
  from ..models.review_response import ReviewResponse





T = TypeVar("T", bound="Review")



@_attrs_define
class Review:
    """ A guest or host review unified across channels. Returned by `GET /v1/reviews` and `GET /v1/reviews/{id}`. Populated
    from main vanio's unified `reviews` table after the per-channel backfill cron has run.

        Attributes:
            id (str | Unset): Internal Repull review id — pass back to `/v1/reviews/{id}`.
            external_id (str | Unset): ID in the source channel (Airbnb review id, Booking review id, etc.).
            platform (ReviewPlatform | Unset):
            listing_id (None | str | Unset): Internal Repull listing id the review is attached to.
            reservation_id (None | str | Unset):
            reservation_confirmation_code (None | str | Unset): Channel-side confirmation code for the reservation being
                reviewed.
            guest_id (None | str | Unset):
            guest_name (None | str | Unset):
            guest_avatar (None | str | Unset):
            reviewer_role (ReviewReviewerRole | Unset): Who wrote the review — `guest` (about the host/property) or `host`
                (about the guest).
            rating (float | None | Unset): Overall rating on the platform's scale (typically 1..5). May be `null` for review
                types that lack a numeric overall score.
            categories (list[ReviewCategory] | Unset):
            public_review (None | str | Unset): Public-facing review text shown on the listing page.
            private_feedback (None | str | Unset): Private feedback the reviewer sent only to the host.
            is_reviewee_recommended (bool | None | Unset): Did the reviewer recommend the reviewee? Used for guest-side
                reviews.
            response (None | ReviewResponse | Unset):
            submitted_at (datetime.datetime | None | Unset):
            updated_at (datetime.datetime | None | Unset):
            expires_at (datetime.datetime | None | Unset): When the review window closes (Airbnb has a 14-day window after
                checkout).
            hidden (bool | Unset):
            language (None | str | Unset): Detected language (ISO 639-1) of the review body.
     """

    id: str | Unset = UNSET
    external_id: str | Unset = UNSET
    platform: ReviewPlatform | Unset = UNSET
    listing_id: None | str | Unset = UNSET
    reservation_id: None | str | Unset = UNSET
    reservation_confirmation_code: None | str | Unset = UNSET
    guest_id: None | str | Unset = UNSET
    guest_name: None | str | Unset = UNSET
    guest_avatar: None | str | Unset = UNSET
    reviewer_role: ReviewReviewerRole | Unset = UNSET
    rating: float | None | Unset = UNSET
    categories: list[ReviewCategory] | Unset = UNSET
    public_review: None | str | Unset = UNSET
    private_feedback: None | str | Unset = UNSET
    is_reviewee_recommended: bool | None | Unset = UNSET
    response: None | ReviewResponse | Unset = UNSET
    submitted_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    expires_at: datetime.datetime | None | Unset = UNSET
    hidden: bool | Unset = UNSET
    language: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.review_category import ReviewCategory
        from ..models.review_response import ReviewResponse
        id = self.id

        external_id = self.external_id

        platform: str | Unset = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.value


        listing_id: None | str | Unset
        if isinstance(self.listing_id, Unset):
            listing_id = UNSET
        else:
            listing_id = self.listing_id

        reservation_id: None | str | Unset
        if isinstance(self.reservation_id, Unset):
            reservation_id = UNSET
        else:
            reservation_id = self.reservation_id

        reservation_confirmation_code: None | str | Unset
        if isinstance(self.reservation_confirmation_code, Unset):
            reservation_confirmation_code = UNSET
        else:
            reservation_confirmation_code = self.reservation_confirmation_code

        guest_id: None | str | Unset
        if isinstance(self.guest_id, Unset):
            guest_id = UNSET
        else:
            guest_id = self.guest_id

        guest_name: None | str | Unset
        if isinstance(self.guest_name, Unset):
            guest_name = UNSET
        else:
            guest_name = self.guest_name

        guest_avatar: None | str | Unset
        if isinstance(self.guest_avatar, Unset):
            guest_avatar = UNSET
        else:
            guest_avatar = self.guest_avatar

        reviewer_role: str | Unset = UNSET
        if not isinstance(self.reviewer_role, Unset):
            reviewer_role = self.reviewer_role.value


        rating: float | None | Unset
        if isinstance(self.rating, Unset):
            rating = UNSET
        else:
            rating = self.rating

        categories: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.categories, Unset):
            categories = []
            for categories_item_data in self.categories:
                categories_item = categories_item_data.to_dict()
                categories.append(categories_item)



        public_review: None | str | Unset
        if isinstance(self.public_review, Unset):
            public_review = UNSET
        else:
            public_review = self.public_review

        private_feedback: None | str | Unset
        if isinstance(self.private_feedback, Unset):
            private_feedback = UNSET
        else:
            private_feedback = self.private_feedback

        is_reviewee_recommended: bool | None | Unset
        if isinstance(self.is_reviewee_recommended, Unset):
            is_reviewee_recommended = UNSET
        else:
            is_reviewee_recommended = self.is_reviewee_recommended

        response: dict[str, Any] | None | Unset
        if isinstance(self.response, Unset):
            response = UNSET
        elif isinstance(self.response, ReviewResponse):
            response = self.response.to_dict()
        else:
            response = self.response

        submitted_at: None | str | Unset
        if isinstance(self.submitted_at, Unset):
            submitted_at = UNSET
        elif isinstance(self.submitted_at, datetime.datetime):
            submitted_at = self.submitted_at.isoformat()
        else:
            submitted_at = self.submitted_at

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        hidden = self.hidden

        language: None | str | Unset
        if isinstance(self.language, Unset):
            language = UNSET
        else:
            language = self.language


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if platform is not UNSET:
            field_dict["platform"] = platform
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if reservation_id is not UNSET:
            field_dict["reservationId"] = reservation_id
        if reservation_confirmation_code is not UNSET:
            field_dict["reservationConfirmationCode"] = reservation_confirmation_code
        if guest_id is not UNSET:
            field_dict["guestId"] = guest_id
        if guest_name is not UNSET:
            field_dict["guestName"] = guest_name
        if guest_avatar is not UNSET:
            field_dict["guestAvatar"] = guest_avatar
        if reviewer_role is not UNSET:
            field_dict["reviewerRole"] = reviewer_role
        if rating is not UNSET:
            field_dict["rating"] = rating
        if categories is not UNSET:
            field_dict["categories"] = categories
        if public_review is not UNSET:
            field_dict["publicReview"] = public_review
        if private_feedback is not UNSET:
            field_dict["privateFeedback"] = private_feedback
        if is_reviewee_recommended is not UNSET:
            field_dict["isRevieweeRecommended"] = is_reviewee_recommended
        if response is not UNSET:
            field_dict["response"] = response
        if submitted_at is not UNSET:
            field_dict["submittedAt"] = submitted_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if language is not UNSET:
            field_dict["language"] = language

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.review_category import ReviewCategory
        from ..models.review_response import ReviewResponse
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        external_id = d.pop("externalId", UNSET)

        _platform = d.pop("platform", UNSET)
        platform: ReviewPlatform | Unset
        if isinstance(_platform,  Unset):
            platform = UNSET
        else:
            platform = ReviewPlatform(_platform)




        def _parse_listing_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        listing_id = _parse_listing_id(d.pop("listingId", UNSET))


        def _parse_reservation_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reservation_id = _parse_reservation_id(d.pop("reservationId", UNSET))


        def _parse_reservation_confirmation_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reservation_confirmation_code = _parse_reservation_confirmation_code(d.pop("reservationConfirmationCode", UNSET))


        def _parse_guest_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        guest_id = _parse_guest_id(d.pop("guestId", UNSET))


        def _parse_guest_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        guest_name = _parse_guest_name(d.pop("guestName", UNSET))


        def _parse_guest_avatar(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        guest_avatar = _parse_guest_avatar(d.pop("guestAvatar", UNSET))


        _reviewer_role = d.pop("reviewerRole", UNSET)
        reviewer_role: ReviewReviewerRole | Unset
        if isinstance(_reviewer_role,  Unset):
            reviewer_role = UNSET
        else:
            reviewer_role = ReviewReviewerRole(_reviewer_role)




        def _parse_rating(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        rating = _parse_rating(d.pop("rating", UNSET))


        _categories = d.pop("categories", UNSET)
        categories: list[ReviewCategory] | Unset = UNSET
        if _categories is not UNSET:
            categories = []
            for categories_item_data in _categories:
                categories_item = ReviewCategory.from_dict(categories_item_data)



                categories.append(categories_item)


        def _parse_public_review(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        public_review = _parse_public_review(d.pop("publicReview", UNSET))


        def _parse_private_feedback(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        private_feedback = _parse_private_feedback(d.pop("privateFeedback", UNSET))


        def _parse_is_reviewee_recommended(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_reviewee_recommended = _parse_is_reviewee_recommended(d.pop("isRevieweeRecommended", UNSET))


        def _parse_response(data: object) -> None | ReviewResponse | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_type_1 = ReviewResponse.from_dict(data)



                return response_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ReviewResponse | Unset, data)

        response = _parse_response(d.pop("response", UNSET))


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


        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = isoparse(data)



                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updatedAt", UNSET))


        def _parse_expires_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = isoparse(data)



                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expires_at = _parse_expires_at(d.pop("expiresAt", UNSET))


        hidden = d.pop("hidden", UNSET)

        def _parse_language(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        language = _parse_language(d.pop("language", UNSET))


        review = cls(
            id=id,
            external_id=external_id,
            platform=platform,
            listing_id=listing_id,
            reservation_id=reservation_id,
            reservation_confirmation_code=reservation_confirmation_code,
            guest_id=guest_id,
            guest_name=guest_name,
            guest_avatar=guest_avatar,
            reviewer_role=reviewer_role,
            rating=rating,
            categories=categories,
            public_review=public_review,
            private_feedback=private_feedback,
            is_reviewee_recommended=is_reviewee_recommended,
            response=response,
            submitted_at=submitted_at,
            updated_at=updated_at,
            expires_at=expires_at,
            hidden=hidden,
            language=language,
        )


        review.additional_properties = d
        return review

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
