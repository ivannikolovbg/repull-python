from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.update_airbnb_booking_settings_response_200_data_applied_item import UpdateAirbnbBookingSettingsResponse200DataAppliedItem
from typing import cast

if TYPE_CHECKING:
  from ..models.update_airbnb_booking_settings_response_200_data_settings import UpdateAirbnbBookingSettingsResponse200DataSettings





T = TypeVar("T", bound="UpdateAirbnbBookingSettingsResponse200Data")



@_attrs_define
class UpdateAirbnbBookingSettingsResponse200Data:
    """ 
        Attributes:
            applied (list[UpdateAirbnbBookingSettingsResponse200DataAppliedItem]): Which upstream groups this request wrote.
            settings (UpdateAirbnbBookingSettingsResponse200DataSettings):
     """

    applied: list[UpdateAirbnbBookingSettingsResponse200DataAppliedItem]
    settings: UpdateAirbnbBookingSettingsResponse200DataSettings
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_airbnb_booking_settings_response_200_data_settings import UpdateAirbnbBookingSettingsResponse200DataSettings
        applied = []
        for applied_item_data in self.applied:
            applied_item = applied_item_data.value
            applied.append(applied_item)



        settings = self.settings.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "applied": applied,
            "settings": settings,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_airbnb_booking_settings_response_200_data_settings import UpdateAirbnbBookingSettingsResponse200DataSettings
        d = dict(src_dict)
        applied = []
        _applied = d.pop("applied")
        for applied_item_data in (_applied):
            applied_item = UpdateAirbnbBookingSettingsResponse200DataAppliedItem(applied_item_data)



            applied.append(applied_item)


        settings = UpdateAirbnbBookingSettingsResponse200DataSettings.from_dict(d.pop("settings"))




        update_airbnb_booking_settings_response_200_data = cls(
            applied=applied,
            settings=settings,
        )


        update_airbnb_booking_settings_response_200_data.additional_properties = d
        return update_airbnb_booking_settings_response_200_data

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
