from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.update_airbnb_booking_settings_body_instant_book_guest_category import UpdateAirbnbBookingSettingsBodyInstantBookGuestCategory
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="UpdateAirbnbBookingSettingsBodyInstantBook")



@_attrs_define
class UpdateAirbnbBookingSettingsBodyInstantBook:
    """ Send `enabled`, `guestCategory`, or `enabled` + `requiresGoodTrackRecord`. `requiresGoodTrackRecord` alone is
    refused — it selects WHICH guests may Instant Book, so it needs `enabled: true` (or an explicit category) with it.
    Contradictory combinations are refused.

        Attributes:
            enabled (bool | None | Unset):
            guest_category (UpdateAirbnbBookingSettingsBodyInstantBookGuestCategory | Unset):
            requires_good_track_record (bool | None | Unset):
     """

    enabled: bool | None | Unset = UNSET
    guest_category: UpdateAirbnbBookingSettingsBodyInstantBookGuestCategory | Unset = UNSET
    requires_good_track_record: bool | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        enabled: bool | None | Unset
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        guest_category: str | Unset = UNSET
        if not isinstance(self.guest_category, Unset):
            guest_category = self.guest_category.value


        requires_good_track_record: bool | None | Unset
        if isinstance(self.requires_good_track_record, Unset):
            requires_good_track_record = UNSET
        else:
            requires_good_track_record = self.requires_good_track_record


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if guest_category is not UNSET:
            field_dict["guestCategory"] = guest_category
        if requires_good_track_record is not UNSET:
            field_dict["requiresGoodTrackRecord"] = requires_good_track_record

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))


        _guest_category = d.pop("guestCategory", UNSET)
        guest_category: UpdateAirbnbBookingSettingsBodyInstantBookGuestCategory | Unset
        if isinstance(_guest_category,  Unset):
            guest_category = UNSET
        else:
            guest_category = UpdateAirbnbBookingSettingsBodyInstantBookGuestCategory(_guest_category)




        def _parse_requires_good_track_record(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        requires_good_track_record = _parse_requires_good_track_record(d.pop("requiresGoodTrackRecord", UNSET))


        update_airbnb_booking_settings_body_instant_book = cls(
            enabled=enabled,
            guest_category=guest_category,
            requires_good_track_record=requires_good_track_record,
        )

        return update_airbnb_booking_settings_body_instant_book

