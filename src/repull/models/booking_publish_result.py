from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.booking_publish_section_error import BookingPublishSectionError





T = TypeVar("T", bound="BookingPublishResult")



@_attrs_define
class BookingPublishResult:
    """ A publish is not one call to Booking.com: it is several independent Content API calls (details, description,
    amenities, rooms, photos, pricing), each of which can fail on its own. A PARTIAL publish is normal — what succeeded
    stays applied; there is no rollback. Fix the failing sections and publish again; re-publishing an unchanged section
    is harmless.

    A property whose Content API credentials do not cover a section answers 403 for that section alone — the rest still
    land, and the failure is reported here rather than swallowed.

        Attributes:
            published (bool): True only when EVERY attempted section reached Booking.com.
            sections (list[str]): Sections that landed on Booking.com. Example: ['details', 'description', 'photos'].
            errors (list[BookingPublishSectionError]): Per-section failures. Empty when `published` is true.
            reason (str | Unset): Set when the publish never started at all — most often because the listing is not mapped
                to any Booking.com property yet. Finish the Connect flow (`POST /v1/connect/booking/map-rooms`) and publish
                again.
            hotel_id (None | str | Unset): The Booking.com property this publish wrote into — resolved from the listing's
                mapping, or the one you named. Always read it back: a listing can be mapped to several properties, and this
                states which one actually received the content. Null when the listing is mapped to no property, in which case
                nothing was pushed.
     """

    published: bool
    sections: list[str]
    errors: list[BookingPublishSectionError]
    reason: str | Unset = UNSET
    hotel_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.booking_publish_section_error import BookingPublishSectionError
        published = self.published

        sections = self.sections



        errors = []
        for errors_item_data in self.errors:
            errors_item = errors_item_data.to_dict()
            errors.append(errors_item)



        reason = self.reason

        hotel_id: None | str | Unset
        if isinstance(self.hotel_id, Unset):
            hotel_id = UNSET
        else:
            hotel_id = self.hotel_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "published": published,
            "sections": sections,
            "errors": errors,
        })
        if reason is not UNSET:
            field_dict["reason"] = reason
        if hotel_id is not UNSET:
            field_dict["hotelId"] = hotel_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.booking_publish_section_error import BookingPublishSectionError
        d = dict(src_dict)
        published = d.pop("published")

        sections = cast(list[str], d.pop("sections"))


        errors = []
        _errors = d.pop("errors")
        for errors_item_data in (_errors):
            errors_item = BookingPublishSectionError.from_dict(errors_item_data)



            errors.append(errors_item)


        reason = d.pop("reason", UNSET)

        def _parse_hotel_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hotel_id = _parse_hotel_id(d.pop("hotelId", UNSET))


        booking_publish_result = cls(
            published=published,
            sections=sections,
            errors=errors,
            reason=reason,
            hotel_id=hotel_id,
        )


        booking_publish_result.additional_properties = d
        return booking_publish_result

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
