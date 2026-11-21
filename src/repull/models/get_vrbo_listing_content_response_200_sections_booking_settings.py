from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_vrbo_listing_content_response_200_sections_booking_settings_booking_type import GetVrboListingContentResponse200SectionsBookingSettingsBookingType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_vrbo_listing_content_response_200_sections_booking_settings_access_type_options_item import GetVrboListingContentResponse200SectionsBookingSettingsAccessTypeOptionsItem
  from ..models.get_vrbo_listing_content_response_200_sections_booking_settings_min_nights_range import GetVrboListingContentResponse200SectionsBookingSettingsMinNightsRange





T = TypeVar("T", bound="GetVrboListingContentResponse200SectionsBookingSettings")



@_attrs_define
class GetVrboListingContentResponse200SectionsBookingSettings:
    """ 
        Attributes:
            booking_type (GetVrboListingContentResponse200SectionsBookingSettingsBookingType | Unset):
            instant_booking_eligible (bool | None | Unset):
            min_nights (int | None | Unset):
            min_nights_range (GetVrboListingContentResponse200SectionsBookingSettingsMinNightsRange | Unset):
            min_days_before_booking (int | None | Unset):
            min_days_before_booking_options (list[int] | Unset):
            max_months_before_booking (int | None | Unset):
            max_months_before_booking_options (list[int] | Unset):
            max_length_of_stay (int | None | Unset):
            access_type (None | str | Unset):
            access_type_options (list[GetVrboListingContentResponse200SectionsBookingSettingsAccessTypeOptionsItem] |
                Unset):
            check_in_time (None | str | Unset):
            check_out_time (None | str | Unset):
     """

    booking_type: GetVrboListingContentResponse200SectionsBookingSettingsBookingType | Unset = UNSET
    instant_booking_eligible: bool | None | Unset = UNSET
    min_nights: int | None | Unset = UNSET
    min_nights_range: GetVrboListingContentResponse200SectionsBookingSettingsMinNightsRange | Unset = UNSET
    min_days_before_booking: int | None | Unset = UNSET
    min_days_before_booking_options: list[int] | Unset = UNSET
    max_months_before_booking: int | None | Unset = UNSET
    max_months_before_booking_options: list[int] | Unset = UNSET
    max_length_of_stay: int | None | Unset = UNSET
    access_type: None | str | Unset = UNSET
    access_type_options: list[GetVrboListingContentResponse200SectionsBookingSettingsAccessTypeOptionsItem] | Unset = UNSET
    check_in_time: None | str | Unset = UNSET
    check_out_time: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_vrbo_listing_content_response_200_sections_booking_settings_access_type_options_item import GetVrboListingContentResponse200SectionsBookingSettingsAccessTypeOptionsItem
        from ..models.get_vrbo_listing_content_response_200_sections_booking_settings_min_nights_range import GetVrboListingContentResponse200SectionsBookingSettingsMinNightsRange
        booking_type: str | Unset = UNSET
        if not isinstance(self.booking_type, Unset):
            booking_type = self.booking_type.value


        instant_booking_eligible: bool | None | Unset
        if isinstance(self.instant_booking_eligible, Unset):
            instant_booking_eligible = UNSET
        else:
            instant_booking_eligible = self.instant_booking_eligible

        min_nights: int | None | Unset
        if isinstance(self.min_nights, Unset):
            min_nights = UNSET
        else:
            min_nights = self.min_nights

        min_nights_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.min_nights_range, Unset):
            min_nights_range = self.min_nights_range.to_dict()

        min_days_before_booking: int | None | Unset
        if isinstance(self.min_days_before_booking, Unset):
            min_days_before_booking = UNSET
        else:
            min_days_before_booking = self.min_days_before_booking

        min_days_before_booking_options: list[int] | Unset = UNSET
        if not isinstance(self.min_days_before_booking_options, Unset):
            min_days_before_booking_options = self.min_days_before_booking_options



        max_months_before_booking: int | None | Unset
        if isinstance(self.max_months_before_booking, Unset):
            max_months_before_booking = UNSET
        else:
            max_months_before_booking = self.max_months_before_booking

        max_months_before_booking_options: list[int] | Unset = UNSET
        if not isinstance(self.max_months_before_booking_options, Unset):
            max_months_before_booking_options = self.max_months_before_booking_options



        max_length_of_stay: int | None | Unset
        if isinstance(self.max_length_of_stay, Unset):
            max_length_of_stay = UNSET
        else:
            max_length_of_stay = self.max_length_of_stay

        access_type: None | str | Unset
        if isinstance(self.access_type, Unset):
            access_type = UNSET
        else:
            access_type = self.access_type

        access_type_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.access_type_options, Unset):
            access_type_options = []
            for access_type_options_item_data in self.access_type_options:
                access_type_options_item = access_type_options_item_data.to_dict()
                access_type_options.append(access_type_options_item)



        check_in_time: None | str | Unset
        if isinstance(self.check_in_time, Unset):
            check_in_time = UNSET
        else:
            check_in_time = self.check_in_time

        check_out_time: None | str | Unset
        if isinstance(self.check_out_time, Unset):
            check_out_time = UNSET
        else:
            check_out_time = self.check_out_time


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if booking_type is not UNSET:
            field_dict["bookingType"] = booking_type
        if instant_booking_eligible is not UNSET:
            field_dict["instantBookingEligible"] = instant_booking_eligible
        if min_nights is not UNSET:
            field_dict["minNights"] = min_nights
        if min_nights_range is not UNSET:
            field_dict["minNightsRange"] = min_nights_range
        if min_days_before_booking is not UNSET:
            field_dict["minDaysBeforeBooking"] = min_days_before_booking
        if min_days_before_booking_options is not UNSET:
            field_dict["minDaysBeforeBookingOptions"] = min_days_before_booking_options
        if max_months_before_booking is not UNSET:
            field_dict["maxMonthsBeforeBooking"] = max_months_before_booking
        if max_months_before_booking_options is not UNSET:
            field_dict["maxMonthsBeforeBookingOptions"] = max_months_before_booking_options
        if max_length_of_stay is not UNSET:
            field_dict["maxLengthOfStay"] = max_length_of_stay
        if access_type is not UNSET:
            field_dict["accessType"] = access_type
        if access_type_options is not UNSET:
            field_dict["accessTypeOptions"] = access_type_options
        if check_in_time is not UNSET:
            field_dict["checkInTime"] = check_in_time
        if check_out_time is not UNSET:
            field_dict["checkOutTime"] = check_out_time

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_vrbo_listing_content_response_200_sections_booking_settings_access_type_options_item import GetVrboListingContentResponse200SectionsBookingSettingsAccessTypeOptionsItem
        from ..models.get_vrbo_listing_content_response_200_sections_booking_settings_min_nights_range import GetVrboListingContentResponse200SectionsBookingSettingsMinNightsRange
        d = dict(src_dict)
        _booking_type = d.pop("bookingType", UNSET)
        booking_type: GetVrboListingContentResponse200SectionsBookingSettingsBookingType | Unset
        if isinstance(_booking_type,  Unset):
            booking_type = UNSET
        else:
            booking_type = GetVrboListingContentResponse200SectionsBookingSettingsBookingType(_booking_type)




        def _parse_instant_booking_eligible(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        instant_booking_eligible = _parse_instant_booking_eligible(d.pop("instantBookingEligible", UNSET))


        def _parse_min_nights(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_nights = _parse_min_nights(d.pop("minNights", UNSET))


        _min_nights_range = d.pop("minNightsRange", UNSET)
        min_nights_range: GetVrboListingContentResponse200SectionsBookingSettingsMinNightsRange | Unset
        if isinstance(_min_nights_range,  Unset):
            min_nights_range = UNSET
        else:
            min_nights_range = GetVrboListingContentResponse200SectionsBookingSettingsMinNightsRange.from_dict(_min_nights_range)




        def _parse_min_days_before_booking(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_days_before_booking = _parse_min_days_before_booking(d.pop("minDaysBeforeBooking", UNSET))


        min_days_before_booking_options = cast(list[int], d.pop("minDaysBeforeBookingOptions", UNSET))


        def _parse_max_months_before_booking(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_months_before_booking = _parse_max_months_before_booking(d.pop("maxMonthsBeforeBooking", UNSET))


        max_months_before_booking_options = cast(list[int], d.pop("maxMonthsBeforeBookingOptions", UNSET))


        def _parse_max_length_of_stay(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_length_of_stay = _parse_max_length_of_stay(d.pop("maxLengthOfStay", UNSET))


        def _parse_access_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        access_type = _parse_access_type(d.pop("accessType", UNSET))


        _access_type_options = d.pop("accessTypeOptions", UNSET)
        access_type_options: list[GetVrboListingContentResponse200SectionsBookingSettingsAccessTypeOptionsItem] | Unset = UNSET
        if _access_type_options is not UNSET:
            access_type_options = []
            for access_type_options_item_data in _access_type_options:
                access_type_options_item = GetVrboListingContentResponse200SectionsBookingSettingsAccessTypeOptionsItem.from_dict(access_type_options_item_data)



                access_type_options.append(access_type_options_item)


        def _parse_check_in_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        check_in_time = _parse_check_in_time(d.pop("checkInTime", UNSET))


        def _parse_check_out_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        check_out_time = _parse_check_out_time(d.pop("checkOutTime", UNSET))


        get_vrbo_listing_content_response_200_sections_booking_settings = cls(
            booking_type=booking_type,
            instant_booking_eligible=instant_booking_eligible,
            min_nights=min_nights,
            min_nights_range=min_nights_range,
            min_days_before_booking=min_days_before_booking,
            min_days_before_booking_options=min_days_before_booking_options,
            max_months_before_booking=max_months_before_booking,
            max_months_before_booking_options=max_months_before_booking_options,
            max_length_of_stay=max_length_of_stay,
            access_type=access_type,
            access_type_options=access_type_options,
            check_in_time=check_in_time,
            check_out_time=check_out_time,
        )


        get_vrbo_listing_content_response_200_sections_booking_settings.additional_properties = d
        return get_vrbo_listing_content_response_200_sections_booking_settings

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
