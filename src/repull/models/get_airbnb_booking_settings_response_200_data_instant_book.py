from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_airbnb_booking_settings_response_200_data_instant_book_guest_category import GetAirbnbBookingSettingsResponse200DataInstantBookGuestCategory
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GetAirbnbBookingSettingsResponse200DataInstantBook")



@_attrs_define
class GetAirbnbBookingSettingsResponse200DataInstantBook:
    """ Instant Book state. All three fields describe ONE Airbnb value, `instant_booking_allowed_category`.

        Attributes:
            enabled (bool | None | Unset): `false` when the category is `off` — the listing is request-to-book.
            guest_category (GetAirbnbBookingSettingsResponse200DataInstantBookGuestCategory | Unset): Which guests may
                Instant Book.
            requires_good_track_record (bool | None | Unset): `true` for `experienced_guests_only` /
                `recommended_guests_only` — Airbnb calls this a good track record.
     """

    enabled: bool | None | Unset = UNSET
    guest_category: GetAirbnbBookingSettingsResponse200DataInstantBookGuestCategory | Unset = UNSET
    requires_good_track_record: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





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
        field_dict.update(self.additional_properties)
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
        guest_category: GetAirbnbBookingSettingsResponse200DataInstantBookGuestCategory | Unset
        if isinstance(_guest_category,  Unset):
            guest_category = UNSET
        else:
            guest_category = GetAirbnbBookingSettingsResponse200DataInstantBookGuestCategory(_guest_category)




        def _parse_requires_good_track_record(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        requires_good_track_record = _parse_requires_good_track_record(d.pop("requiresGoodTrackRecord", UNSET))


        get_airbnb_booking_settings_response_200_data_instant_book = cls(
            enabled=enabled,
            guest_category=guest_category,
            requires_good_track_record=requires_good_track_record,
        )


        get_airbnb_booking_settings_response_200_data_instant_book.additional_properties = d
        return get_airbnb_booking_settings_response_200_data_instant_book

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
