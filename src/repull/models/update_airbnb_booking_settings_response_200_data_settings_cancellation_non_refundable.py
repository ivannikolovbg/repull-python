from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="UpdateAirbnbBookingSettingsResponse200DataSettingsCancellationNonRefundable")



@_attrs_define
class UpdateAirbnbBookingSettingsResponse200DataSettingsCancellationNonRefundable:
    """ 
        Attributes:
            enabled (bool | None | Unset):
            discount_percent (int | None | Unset): Whole-percent discount a guest gets for giving up refundability.
            price_factor (float | None | Unset): Airbnb's own representation: `1 - discountPercent/100`.
     """

    enabled: bool | None | Unset = UNSET
    discount_percent: int | None | Unset = UNSET
    price_factor: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        enabled: bool | None | Unset
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        discount_percent: int | None | Unset
        if isinstance(self.discount_percent, Unset):
            discount_percent = UNSET
        else:
            discount_percent = self.discount_percent

        price_factor: float | None | Unset
        if isinstance(self.price_factor, Unset):
            price_factor = UNSET
        else:
            price_factor = self.price_factor


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if discount_percent is not UNSET:
            field_dict["discountPercent"] = discount_percent
        if price_factor is not UNSET:
            field_dict["priceFactor"] = price_factor

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


        def _parse_discount_percent(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        discount_percent = _parse_discount_percent(d.pop("discountPercent", UNSET))


        def _parse_price_factor(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        price_factor = _parse_price_factor(d.pop("priceFactor", UNSET))


        update_airbnb_booking_settings_response_200_data_settings_cancellation_non_refundable = cls(
            enabled=enabled,
            discount_percent=discount_percent,
            price_factor=price_factor,
        )


        update_airbnb_booking_settings_response_200_data_settings_cancellation_non_refundable.additional_properties = d
        return update_airbnb_booking_settings_response_200_data_settings_cancellation_non_refundable

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
