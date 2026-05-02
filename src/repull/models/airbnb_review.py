from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="AirbnbReview")



@_attrs_define
class AirbnbReview:
    """ An Airbnb review (guest → host or host → guest).

        Attributes:
            id (str | Unset):
            reservation_code (None | str | Unset):
            rating (int | None | Unset):
            comment (None | str | Unset):
            response (None | str | Unset):
            created_at (datetime.datetime | None | Unset):
     """

    id: str | Unset = UNSET
    reservation_code: None | str | Unset = UNSET
    rating: int | None | Unset = UNSET
    comment: None | str | Unset = UNSET
    response: None | str | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        reservation_code: None | str | Unset
        if isinstance(self.reservation_code, Unset):
            reservation_code = UNSET
        else:
            reservation_code = self.reservation_code

        rating: int | None | Unset
        if isinstance(self.rating, Unset):
            rating = UNSET
        else:
            rating = self.rating

        comment: None | str | Unset
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        response: None | str | Unset
        if isinstance(self.response, Unset):
            response = UNSET
        else:
            response = self.response

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if reservation_code is not UNSET:
            field_dict["reservationCode"] = reservation_code
        if rating is not UNSET:
            field_dict["rating"] = rating
        if comment is not UNSET:
            field_dict["comment"] = comment
        if response is not UNSET:
            field_dict["response"] = response
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_reservation_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reservation_code = _parse_reservation_code(d.pop("reservationCode", UNSET))


        def _parse_rating(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rating = _parse_rating(d.pop("rating", UNSET))


        def _parse_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment = _parse_comment(d.pop("comment", UNSET))


        def _parse_response(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        response = _parse_response(d.pop("response", UNSET))


        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = isoparse(data)



                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("createdAt", UNSET))


        airbnb_review = cls(
            id=id,
            reservation_code=reservation_code,
            rating=rating,
            comment=comment,
            response=response,
            created_at=created_at,
        )


        airbnb_review.additional_properties = d
        return airbnb_review

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
