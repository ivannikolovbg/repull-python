from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_airbnb_booking_settings_body_advance_notice import UpdateAirbnbBookingSettingsBodyAdvanceNotice
  from ..models.update_airbnb_booking_settings_body_booking_window import UpdateAirbnbBookingSettingsBodyBookingWindow
  from ..models.update_airbnb_booking_settings_body_cancellation import UpdateAirbnbBookingSettingsBodyCancellation
  from ..models.update_airbnb_booking_settings_body_check_in import UpdateAirbnbBookingSettingsBodyCheckIn
  from ..models.update_airbnb_booking_settings_body_check_out import UpdateAirbnbBookingSettingsBodyCheckOut
  from ..models.update_airbnb_booking_settings_body_instant_book import UpdateAirbnbBookingSettingsBodyInstantBook
  from ..models.update_airbnb_booking_settings_body_preparation_time import UpdateAirbnbBookingSettingsBodyPreparationTime





T = TypeVar("T", bound="UpdateAirbnbBookingSettingsBody")



@_attrs_define
class UpdateAirbnbBookingSettingsBody:
    """ Partial update — a field you do not send is left as it is. Unknown fields are refused with `422`, so a typo can
    never be silently dropped.

        Attributes:
            instant_book (UpdateAirbnbBookingSettingsBodyInstantBook | Unset): Send `enabled`, `guestCategory`, or `enabled`
                + `requiresGoodTrackRecord`. `requiresGoodTrackRecord` alone is refused — it selects WHICH guests may Instant
                Book, so it needs `enabled: true` (or an explicit category) with it. Contradictory combinations are refused.
            check_in (UpdateAirbnbBookingSettingsBodyCheckIn | Unset): `start` must be earlier than `end` unless either is
                `FLEXIBLE`.
            check_out (UpdateAirbnbBookingSettingsBodyCheckOut | Unset):
            cancellation (UpdateAirbnbBookingSettingsBodyCancellation | Unset):
            advance_notice (UpdateAirbnbBookingSettingsBodyAdvanceNotice | Unset): Send `hours`, `allowRequestToBook`, or
                both. The half you omit keeps the value Airbnb currently holds.
            preparation_time (UpdateAirbnbBookingSettingsBodyPreparationTime | Unset):
            booking_window (UpdateAirbnbBookingSettingsBodyBookingWindow | Unset): Send `days`, or `unlimited: true`.
                Sending both is refused.
     """

    instant_book: UpdateAirbnbBookingSettingsBodyInstantBook | Unset = UNSET
    check_in: UpdateAirbnbBookingSettingsBodyCheckIn | Unset = UNSET
    check_out: UpdateAirbnbBookingSettingsBodyCheckOut | Unset = UNSET
    cancellation: UpdateAirbnbBookingSettingsBodyCancellation | Unset = UNSET
    advance_notice: UpdateAirbnbBookingSettingsBodyAdvanceNotice | Unset = UNSET
    preparation_time: UpdateAirbnbBookingSettingsBodyPreparationTime | Unset = UNSET
    booking_window: UpdateAirbnbBookingSettingsBodyBookingWindow | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_airbnb_booking_settings_body_advance_notice import UpdateAirbnbBookingSettingsBodyAdvanceNotice
        from ..models.update_airbnb_booking_settings_body_booking_window import UpdateAirbnbBookingSettingsBodyBookingWindow
        from ..models.update_airbnb_booking_settings_body_cancellation import UpdateAirbnbBookingSettingsBodyCancellation
        from ..models.update_airbnb_booking_settings_body_check_in import UpdateAirbnbBookingSettingsBodyCheckIn
        from ..models.update_airbnb_booking_settings_body_check_out import UpdateAirbnbBookingSettingsBodyCheckOut
        from ..models.update_airbnb_booking_settings_body_instant_book import UpdateAirbnbBookingSettingsBodyInstantBook
        from ..models.update_airbnb_booking_settings_body_preparation_time import UpdateAirbnbBookingSettingsBodyPreparationTime
        instant_book: dict[str, Any] | Unset = UNSET
        if not isinstance(self.instant_book, Unset):
            instant_book = self.instant_book.to_dict()

        check_in: dict[str, Any] | Unset = UNSET
        if not isinstance(self.check_in, Unset):
            check_in = self.check_in.to_dict()

        check_out: dict[str, Any] | Unset = UNSET
        if not isinstance(self.check_out, Unset):
            check_out = self.check_out.to_dict()

        cancellation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cancellation, Unset):
            cancellation = self.cancellation.to_dict()

        advance_notice: dict[str, Any] | Unset = UNSET
        if not isinstance(self.advance_notice, Unset):
            advance_notice = self.advance_notice.to_dict()

        preparation_time: dict[str, Any] | Unset = UNSET
        if not isinstance(self.preparation_time, Unset):
            preparation_time = self.preparation_time.to_dict()

        booking_window: dict[str, Any] | Unset = UNSET
        if not isinstance(self.booking_window, Unset):
            booking_window = self.booking_window.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if instant_book is not UNSET:
            field_dict["instantBook"] = instant_book
        if check_in is not UNSET:
            field_dict["checkIn"] = check_in
        if check_out is not UNSET:
            field_dict["checkOut"] = check_out
        if cancellation is not UNSET:
            field_dict["cancellation"] = cancellation
        if advance_notice is not UNSET:
            field_dict["advanceNotice"] = advance_notice
        if preparation_time is not UNSET:
            field_dict["preparationTime"] = preparation_time
        if booking_window is not UNSET:
            field_dict["bookingWindow"] = booking_window

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_airbnb_booking_settings_body_advance_notice import UpdateAirbnbBookingSettingsBodyAdvanceNotice
        from ..models.update_airbnb_booking_settings_body_booking_window import UpdateAirbnbBookingSettingsBodyBookingWindow
        from ..models.update_airbnb_booking_settings_body_cancellation import UpdateAirbnbBookingSettingsBodyCancellation
        from ..models.update_airbnb_booking_settings_body_check_in import UpdateAirbnbBookingSettingsBodyCheckIn
        from ..models.update_airbnb_booking_settings_body_check_out import UpdateAirbnbBookingSettingsBodyCheckOut
        from ..models.update_airbnb_booking_settings_body_instant_book import UpdateAirbnbBookingSettingsBodyInstantBook
        from ..models.update_airbnb_booking_settings_body_preparation_time import UpdateAirbnbBookingSettingsBodyPreparationTime
        d = dict(src_dict)
        _instant_book = d.pop("instantBook", UNSET)
        instant_book: UpdateAirbnbBookingSettingsBodyInstantBook | Unset
        if isinstance(_instant_book,  Unset):
            instant_book = UNSET
        else:
            instant_book = UpdateAirbnbBookingSettingsBodyInstantBook.from_dict(_instant_book)




        _check_in = d.pop("checkIn", UNSET)
        check_in: UpdateAirbnbBookingSettingsBodyCheckIn | Unset
        if isinstance(_check_in,  Unset):
            check_in = UNSET
        else:
            check_in = UpdateAirbnbBookingSettingsBodyCheckIn.from_dict(_check_in)




        _check_out = d.pop("checkOut", UNSET)
        check_out: UpdateAirbnbBookingSettingsBodyCheckOut | Unset
        if isinstance(_check_out,  Unset):
            check_out = UNSET
        else:
            check_out = UpdateAirbnbBookingSettingsBodyCheckOut.from_dict(_check_out)




        _cancellation = d.pop("cancellation", UNSET)
        cancellation: UpdateAirbnbBookingSettingsBodyCancellation | Unset
        if isinstance(_cancellation,  Unset):
            cancellation = UNSET
        else:
            cancellation = UpdateAirbnbBookingSettingsBodyCancellation.from_dict(_cancellation)




        _advance_notice = d.pop("advanceNotice", UNSET)
        advance_notice: UpdateAirbnbBookingSettingsBodyAdvanceNotice | Unset
        if isinstance(_advance_notice,  Unset):
            advance_notice = UNSET
        else:
            advance_notice = UpdateAirbnbBookingSettingsBodyAdvanceNotice.from_dict(_advance_notice)




        _preparation_time = d.pop("preparationTime", UNSET)
        preparation_time: UpdateAirbnbBookingSettingsBodyPreparationTime | Unset
        if isinstance(_preparation_time,  Unset):
            preparation_time = UNSET
        else:
            preparation_time = UpdateAirbnbBookingSettingsBodyPreparationTime.from_dict(_preparation_time)




        _booking_window = d.pop("bookingWindow", UNSET)
        booking_window: UpdateAirbnbBookingSettingsBodyBookingWindow | Unset
        if isinstance(_booking_window,  Unset):
            booking_window = UNSET
        else:
            booking_window = UpdateAirbnbBookingSettingsBodyBookingWindow.from_dict(_booking_window)




        update_airbnb_booking_settings_body = cls(
            instant_book=instant_book,
            check_in=check_in,
            check_out=check_out,
            cancellation=cancellation,
            advance_notice=advance_notice,
            preparation_time=preparation_time,
            booking_window=booking_window,
        )

        return update_airbnb_booking_settings_body

