from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.update_airbnb_booking_settings_response_200_data_settings_booking_mode import UpdateAirbnbBookingSettingsResponse200DataSettingsBookingMode
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_airbnb_booking_settings_response_200_data_settings_advance_notice import UpdateAirbnbBookingSettingsResponse200DataSettingsAdvanceNotice
  from ..models.update_airbnb_booking_settings_response_200_data_settings_booking_window import UpdateAirbnbBookingSettingsResponse200DataSettingsBookingWindow
  from ..models.update_airbnb_booking_settings_response_200_data_settings_cancellation import UpdateAirbnbBookingSettingsResponse200DataSettingsCancellation
  from ..models.update_airbnb_booking_settings_response_200_data_settings_check_in import UpdateAirbnbBookingSettingsResponse200DataSettingsCheckIn
  from ..models.update_airbnb_booking_settings_response_200_data_settings_check_out import UpdateAirbnbBookingSettingsResponse200DataSettingsCheckOut
  from ..models.update_airbnb_booking_settings_response_200_data_settings_instant_book import UpdateAirbnbBookingSettingsResponse200DataSettingsInstantBook
  from ..models.update_airbnb_booking_settings_response_200_data_settings_preparation_time import UpdateAirbnbBookingSettingsResponse200DataSettingsPreparationTime





T = TypeVar("T", bound="UpdateAirbnbBookingSettingsResponse200DataSettings")



@_attrs_define
class UpdateAirbnbBookingSettingsResponse200DataSettings:
    """ 
        Attributes:
            booking_mode (UpdateAirbnbBookingSettingsResponse200DataSettingsBookingMode | Unset): Derived from
                `instantBook`. `request_to_book` means every booking needs the host to approve it.
            instant_book (UpdateAirbnbBookingSettingsResponse200DataSettingsInstantBook | Unset): Instant Book state. All
                three fields describe ONE Airbnb value, `instant_booking_allowed_category`.
            check_in (UpdateAirbnbBookingSettingsResponse200DataSettingsCheckIn | Unset): Check-in window as hours of the
                day, or `FLEXIBLE`.
            check_out (UpdateAirbnbBookingSettingsResponse200DataSettingsCheckOut | Unset):
            advance_notice (UpdateAirbnbBookingSettingsResponse200DataSettingsAdvanceNotice | Unset): How much notice a
                booking needs.
            preparation_time (UpdateAirbnbBookingSettingsResponse200DataSettingsPreparationTime | Unset): Airbnb's
                `turnover_days` — nights blocked between two stays.
            booking_window (UpdateAirbnbBookingSettingsResponse200DataSettingsBookingWindow | Unset): How far ahead guests
                may book.
            cancellation (UpdateAirbnbBookingSettingsResponse200DataSettingsCancellation | Unset):
     """

    booking_mode: UpdateAirbnbBookingSettingsResponse200DataSettingsBookingMode | Unset = UNSET
    instant_book: UpdateAirbnbBookingSettingsResponse200DataSettingsInstantBook | Unset = UNSET
    check_in: UpdateAirbnbBookingSettingsResponse200DataSettingsCheckIn | Unset = UNSET
    check_out: UpdateAirbnbBookingSettingsResponse200DataSettingsCheckOut | Unset = UNSET
    advance_notice: UpdateAirbnbBookingSettingsResponse200DataSettingsAdvanceNotice | Unset = UNSET
    preparation_time: UpdateAirbnbBookingSettingsResponse200DataSettingsPreparationTime | Unset = UNSET
    booking_window: UpdateAirbnbBookingSettingsResponse200DataSettingsBookingWindow | Unset = UNSET
    cancellation: UpdateAirbnbBookingSettingsResponse200DataSettingsCancellation | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_airbnb_booking_settings_response_200_data_settings_advance_notice import UpdateAirbnbBookingSettingsResponse200DataSettingsAdvanceNotice
        from ..models.update_airbnb_booking_settings_response_200_data_settings_booking_window import UpdateAirbnbBookingSettingsResponse200DataSettingsBookingWindow
        from ..models.update_airbnb_booking_settings_response_200_data_settings_cancellation import UpdateAirbnbBookingSettingsResponse200DataSettingsCancellation
        from ..models.update_airbnb_booking_settings_response_200_data_settings_check_in import UpdateAirbnbBookingSettingsResponse200DataSettingsCheckIn
        from ..models.update_airbnb_booking_settings_response_200_data_settings_check_out import UpdateAirbnbBookingSettingsResponse200DataSettingsCheckOut
        from ..models.update_airbnb_booking_settings_response_200_data_settings_instant_book import UpdateAirbnbBookingSettingsResponse200DataSettingsInstantBook
        from ..models.update_airbnb_booking_settings_response_200_data_settings_preparation_time import UpdateAirbnbBookingSettingsResponse200DataSettingsPreparationTime
        booking_mode: str | Unset = UNSET
        if not isinstance(self.booking_mode, Unset):
            booking_mode = self.booking_mode.value


        instant_book: dict[str, Any] | Unset = UNSET
        if not isinstance(self.instant_book, Unset):
            instant_book = self.instant_book.to_dict()

        check_in: dict[str, Any] | Unset = UNSET
        if not isinstance(self.check_in, Unset):
            check_in = self.check_in.to_dict()

        check_out: dict[str, Any] | Unset = UNSET
        if not isinstance(self.check_out, Unset):
            check_out = self.check_out.to_dict()

        advance_notice: dict[str, Any] | Unset = UNSET
        if not isinstance(self.advance_notice, Unset):
            advance_notice = self.advance_notice.to_dict()

        preparation_time: dict[str, Any] | Unset = UNSET
        if not isinstance(self.preparation_time, Unset):
            preparation_time = self.preparation_time.to_dict()

        booking_window: dict[str, Any] | Unset = UNSET
        if not isinstance(self.booking_window, Unset):
            booking_window = self.booking_window.to_dict()

        cancellation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cancellation, Unset):
            cancellation = self.cancellation.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if booking_mode is not UNSET:
            field_dict["bookingMode"] = booking_mode
        if instant_book is not UNSET:
            field_dict["instantBook"] = instant_book
        if check_in is not UNSET:
            field_dict["checkIn"] = check_in
        if check_out is not UNSET:
            field_dict["checkOut"] = check_out
        if advance_notice is not UNSET:
            field_dict["advanceNotice"] = advance_notice
        if preparation_time is not UNSET:
            field_dict["preparationTime"] = preparation_time
        if booking_window is not UNSET:
            field_dict["bookingWindow"] = booking_window
        if cancellation is not UNSET:
            field_dict["cancellation"] = cancellation

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_airbnb_booking_settings_response_200_data_settings_advance_notice import UpdateAirbnbBookingSettingsResponse200DataSettingsAdvanceNotice
        from ..models.update_airbnb_booking_settings_response_200_data_settings_booking_window import UpdateAirbnbBookingSettingsResponse200DataSettingsBookingWindow
        from ..models.update_airbnb_booking_settings_response_200_data_settings_cancellation import UpdateAirbnbBookingSettingsResponse200DataSettingsCancellation
        from ..models.update_airbnb_booking_settings_response_200_data_settings_check_in import UpdateAirbnbBookingSettingsResponse200DataSettingsCheckIn
        from ..models.update_airbnb_booking_settings_response_200_data_settings_check_out import UpdateAirbnbBookingSettingsResponse200DataSettingsCheckOut
        from ..models.update_airbnb_booking_settings_response_200_data_settings_instant_book import UpdateAirbnbBookingSettingsResponse200DataSettingsInstantBook
        from ..models.update_airbnb_booking_settings_response_200_data_settings_preparation_time import UpdateAirbnbBookingSettingsResponse200DataSettingsPreparationTime
        d = dict(src_dict)
        _booking_mode = d.pop("bookingMode", UNSET)
        booking_mode: UpdateAirbnbBookingSettingsResponse200DataSettingsBookingMode | Unset
        if isinstance(_booking_mode,  Unset):
            booking_mode = UNSET
        else:
            booking_mode = UpdateAirbnbBookingSettingsResponse200DataSettingsBookingMode(_booking_mode)




        _instant_book = d.pop("instantBook", UNSET)
        instant_book: UpdateAirbnbBookingSettingsResponse200DataSettingsInstantBook | Unset
        if isinstance(_instant_book,  Unset):
            instant_book = UNSET
        else:
            instant_book = UpdateAirbnbBookingSettingsResponse200DataSettingsInstantBook.from_dict(_instant_book)




        _check_in = d.pop("checkIn", UNSET)
        check_in: UpdateAirbnbBookingSettingsResponse200DataSettingsCheckIn | Unset
        if isinstance(_check_in,  Unset):
            check_in = UNSET
        else:
            check_in = UpdateAirbnbBookingSettingsResponse200DataSettingsCheckIn.from_dict(_check_in)




        _check_out = d.pop("checkOut", UNSET)
        check_out: UpdateAirbnbBookingSettingsResponse200DataSettingsCheckOut | Unset
        if isinstance(_check_out,  Unset):
            check_out = UNSET
        else:
            check_out = UpdateAirbnbBookingSettingsResponse200DataSettingsCheckOut.from_dict(_check_out)




        _advance_notice = d.pop("advanceNotice", UNSET)
        advance_notice: UpdateAirbnbBookingSettingsResponse200DataSettingsAdvanceNotice | Unset
        if isinstance(_advance_notice,  Unset):
            advance_notice = UNSET
        else:
            advance_notice = UpdateAirbnbBookingSettingsResponse200DataSettingsAdvanceNotice.from_dict(_advance_notice)




        _preparation_time = d.pop("preparationTime", UNSET)
        preparation_time: UpdateAirbnbBookingSettingsResponse200DataSettingsPreparationTime | Unset
        if isinstance(_preparation_time,  Unset):
            preparation_time = UNSET
        else:
            preparation_time = UpdateAirbnbBookingSettingsResponse200DataSettingsPreparationTime.from_dict(_preparation_time)




        _booking_window = d.pop("bookingWindow", UNSET)
        booking_window: UpdateAirbnbBookingSettingsResponse200DataSettingsBookingWindow | Unset
        if isinstance(_booking_window,  Unset):
            booking_window = UNSET
        else:
            booking_window = UpdateAirbnbBookingSettingsResponse200DataSettingsBookingWindow.from_dict(_booking_window)




        _cancellation = d.pop("cancellation", UNSET)
        cancellation: UpdateAirbnbBookingSettingsResponse200DataSettingsCancellation | Unset
        if isinstance(_cancellation,  Unset):
            cancellation = UNSET
        else:
            cancellation = UpdateAirbnbBookingSettingsResponse200DataSettingsCancellation.from_dict(_cancellation)




        update_airbnb_booking_settings_response_200_data_settings = cls(
            booking_mode=booking_mode,
            instant_book=instant_book,
            check_in=check_in,
            check_out=check_out,
            advance_notice=advance_notice,
            preparation_time=preparation_time,
            booking_window=booking_window,
            cancellation=cancellation,
        )


        update_airbnb_booking_settings_response_200_data_settings.additional_properties = d
        return update_airbnb_booking_settings_response_200_data_settings

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
