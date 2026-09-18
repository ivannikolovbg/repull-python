from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_airbnb_booking_settings_response_200_data_check_in_end_type_1 import GetAirbnbBookingSettingsResponse200DataCheckInEndType1
from ..models.get_airbnb_booking_settings_response_200_data_check_in_start_type_1 import GetAirbnbBookingSettingsResponse200DataCheckInStartType1
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GetAirbnbBookingSettingsResponse200DataCheckIn")



@_attrs_define
class GetAirbnbBookingSettingsResponse200DataCheckIn:
    """ Check-in window as hours of the day, or `FLEXIBLE`.

        Attributes:
            start (GetAirbnbBookingSettingsResponse200DataCheckInStartType1 | int | None | Unset):
            end (GetAirbnbBookingSettingsResponse200DataCheckInEndType1 | int | None | Unset):
     """

    start: GetAirbnbBookingSettingsResponse200DataCheckInStartType1 | int | None | Unset = UNSET
    end: GetAirbnbBookingSettingsResponse200DataCheckInEndType1 | int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        start: int | None | str | Unset
        if isinstance(self.start, Unset):
            start = UNSET
        elif isinstance(self.start, GetAirbnbBookingSettingsResponse200DataCheckInStartType1):
            start = self.start.value
        else:
            start = self.start

        end: int | None | str | Unset
        if isinstance(self.end, Unset):
            end = UNSET
        elif isinstance(self.end, GetAirbnbBookingSettingsResponse200DataCheckInEndType1):
            end = self.end.value
        else:
            end = self.end


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_start(data: object) -> GetAirbnbBookingSettingsResponse200DataCheckInStartType1 | int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_type_1 = GetAirbnbBookingSettingsResponse200DataCheckInStartType1(data)



                return start_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetAirbnbBookingSettingsResponse200DataCheckInStartType1 | int | None | Unset, data)

        start = _parse_start(d.pop("start", UNSET))


        def _parse_end(data: object) -> GetAirbnbBookingSettingsResponse200DataCheckInEndType1 | int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_type_1 = GetAirbnbBookingSettingsResponse200DataCheckInEndType1(data)



                return end_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetAirbnbBookingSettingsResponse200DataCheckInEndType1 | int | None | Unset, data)

        end = _parse_end(d.pop("end", UNSET))


        get_airbnb_booking_settings_response_200_data_check_in = cls(
            start=start,
            end=end,
        )


        get_airbnb_booking_settings_response_200_data_check_in.additional_properties = d
        return get_airbnb_booking_settings_response_200_data_check_in

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
