from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.booking_publish_section_error_code import BookingPublishSectionErrorCode






T = TypeVar("T", bound="BookingPublishSectionError")



@_attrs_define
class BookingPublishSectionError:
    """ One section of a publish that did not reach Booking.com.

        Attributes:
            section (str): Which part of the listing this failure is about — e.g. `details`, `description`, `amenities`,
                `rooms`, `photos`, `pricing`. Example: description.
            message (str): Booking.com's own reason, verbatim, or ours when we refused to send an empty section.
            code (BookingPublishSectionErrorCode): `no_content` — there was nothing canonical to send for this section;
                write the content, then publish again. `rejected` — Booking.com refused the section as sent; fix the content, or
                the property's Content API permissions, and publish again.

                Airbnb's third code, `locked`, has no Booking.com counterpart and never appears here.
     """

    section: str
    message: str
    code: BookingPublishSectionErrorCode
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        section = self.section

        message = self.message

        code = self.code.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "section": section,
            "message": message,
            "code": code,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        section = d.pop("section")

        message = d.pop("message")

        code = BookingPublishSectionErrorCode(d.pop("code"))




        booking_publish_section_error = cls(
            section=section,
            message=message,
            code=code,
        )


        booking_publish_section_error.additional_properties = d
        return booking_publish_section_error

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
