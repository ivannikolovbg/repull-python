from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.update_vrbo_listing_booking_settings_body_booking_type import UpdateVrboListingBookingSettingsBodyBookingType
from ..models.update_vrbo_listing_booking_settings_body_max_months_before_booking import UpdateVrboListingBookingSettingsBodyMaxMonthsBeforeBooking
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="UpdateVrboListingBookingSettingsBody")



@_attrs_define
class UpdateVrboListingBookingSettingsBody:
    """ 
        Attributes:
            booking_type (UpdateVrboListingBookingSettingsBodyBookingType | Unset):
            min_nights (int | Unset):
            min_days_before_booking (int | Unset): One of the read's `minDaysBeforeBookingOptions`.
            max_months_before_booking (UpdateVrboListingBookingSettingsBodyMaxMonthsBeforeBooking | Unset):
            max_length_of_stay (int | None | Unset):
            access_type (str | Unset): One of the read's `accessTypeOptions[].value`.
     """

    booking_type: UpdateVrboListingBookingSettingsBodyBookingType | Unset = UNSET
    min_nights: int | Unset = UNSET
    min_days_before_booking: int | Unset = UNSET
    max_months_before_booking: UpdateVrboListingBookingSettingsBodyMaxMonthsBeforeBooking | Unset = UNSET
    max_length_of_stay: int | None | Unset = UNSET
    access_type: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        booking_type: str | Unset = UNSET
        if not isinstance(self.booking_type, Unset):
            booking_type = self.booking_type.value


        min_nights = self.min_nights

        min_days_before_booking = self.min_days_before_booking

        max_months_before_booking: int | Unset = UNSET
        if not isinstance(self.max_months_before_booking, Unset):
            max_months_before_booking = self.max_months_before_booking.value


        max_length_of_stay: int | None | Unset
        if isinstance(self.max_length_of_stay, Unset):
            max_length_of_stay = UNSET
        else:
            max_length_of_stay = self.max_length_of_stay

        access_type = self.access_type


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if booking_type is not UNSET:
            field_dict["bookingType"] = booking_type
        if min_nights is not UNSET:
            field_dict["minNights"] = min_nights
        if min_days_before_booking is not UNSET:
            field_dict["minDaysBeforeBooking"] = min_days_before_booking
        if max_months_before_booking is not UNSET:
            field_dict["maxMonthsBeforeBooking"] = max_months_before_booking
        if max_length_of_stay is not UNSET:
            field_dict["maxLengthOfStay"] = max_length_of_stay
        if access_type is not UNSET:
            field_dict["accessType"] = access_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _booking_type = d.pop("bookingType", UNSET)
        booking_type: UpdateVrboListingBookingSettingsBodyBookingType | Unset
        if isinstance(_booking_type,  Unset):
            booking_type = UNSET
        else:
            booking_type = UpdateVrboListingBookingSettingsBodyBookingType(_booking_type)




        min_nights = d.pop("minNights", UNSET)

        min_days_before_booking = d.pop("minDaysBeforeBooking", UNSET)

        _max_months_before_booking = d.pop("maxMonthsBeforeBooking", UNSET)
        max_months_before_booking: UpdateVrboListingBookingSettingsBodyMaxMonthsBeforeBooking | Unset
        if isinstance(_max_months_before_booking,  Unset):
            max_months_before_booking = UNSET
        else:
            max_months_before_booking = UpdateVrboListingBookingSettingsBodyMaxMonthsBeforeBooking(_max_months_before_booking)




        def _parse_max_length_of_stay(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_length_of_stay = _parse_max_length_of_stay(d.pop("maxLengthOfStay", UNSET))


        access_type = d.pop("accessType", UNSET)

        update_vrbo_listing_booking_settings_body = cls(
            booking_type=booking_type,
            min_nights=min_nights,
            min_days_before_booking=min_days_before_booking,
            max_months_before_booking=max_months_before_booking,
            max_length_of_stay=max_length_of_stay,
            access_type=access_type,
        )

        return update_vrbo_listing_booking_settings_body

