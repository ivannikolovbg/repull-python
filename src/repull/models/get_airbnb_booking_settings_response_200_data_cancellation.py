from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_airbnb_booking_settings_response_200_data_cancellation_short_stay_policy import GetAirbnbBookingSettingsResponse200DataCancellationShortStayPolicy
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_airbnb_booking_settings_response_200_data_cancellation_non_refundable import GetAirbnbBookingSettingsResponse200DataCancellationNonRefundable





T = TypeVar("T", bound="GetAirbnbBookingSettingsResponse200DataCancellation")



@_attrs_define
class GetAirbnbBookingSettingsResponse200DataCancellation:
    """ 
        Attributes:
            short_stay_policy (GetAirbnbBookingSettingsResponse200DataCancellationShortStayPolicy | Unset): Policy for stays
                under 28 nights.
            long_stay_policy (None | str | Unset): Airbnb's long-term-stay policy id, for stays of 28+ nights. Opaque.
            non_refundable (GetAirbnbBookingSettingsResponse200DataCancellationNonRefundable | Unset):
     """

    short_stay_policy: GetAirbnbBookingSettingsResponse200DataCancellationShortStayPolicy | Unset = UNSET
    long_stay_policy: None | str | Unset = UNSET
    non_refundable: GetAirbnbBookingSettingsResponse200DataCancellationNonRefundable | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_airbnb_booking_settings_response_200_data_cancellation_non_refundable import GetAirbnbBookingSettingsResponse200DataCancellationNonRefundable
        short_stay_policy: str | Unset = UNSET
        if not isinstance(self.short_stay_policy, Unset):
            short_stay_policy = self.short_stay_policy.value


        long_stay_policy: None | str | Unset
        if isinstance(self.long_stay_policy, Unset):
            long_stay_policy = UNSET
        else:
            long_stay_policy = self.long_stay_policy

        non_refundable: dict[str, Any] | Unset = UNSET
        if not isinstance(self.non_refundable, Unset):
            non_refundable = self.non_refundable.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if short_stay_policy is not UNSET:
            field_dict["shortStayPolicy"] = short_stay_policy
        if long_stay_policy is not UNSET:
            field_dict["longStayPolicy"] = long_stay_policy
        if non_refundable is not UNSET:
            field_dict["nonRefundable"] = non_refundable

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_airbnb_booking_settings_response_200_data_cancellation_non_refundable import GetAirbnbBookingSettingsResponse200DataCancellationNonRefundable
        d = dict(src_dict)
        _short_stay_policy = d.pop("shortStayPolicy", UNSET)
        short_stay_policy: GetAirbnbBookingSettingsResponse200DataCancellationShortStayPolicy | Unset
        if isinstance(_short_stay_policy,  Unset):
            short_stay_policy = UNSET
        else:
            short_stay_policy = GetAirbnbBookingSettingsResponse200DataCancellationShortStayPolicy(_short_stay_policy)




        def _parse_long_stay_policy(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        long_stay_policy = _parse_long_stay_policy(d.pop("longStayPolicy", UNSET))


        _non_refundable = d.pop("nonRefundable", UNSET)
        non_refundable: GetAirbnbBookingSettingsResponse200DataCancellationNonRefundable | Unset
        if isinstance(_non_refundable,  Unset):
            non_refundable = UNSET
        else:
            non_refundable = GetAirbnbBookingSettingsResponse200DataCancellationNonRefundable.from_dict(_non_refundable)




        get_airbnb_booking_settings_response_200_data_cancellation = cls(
            short_stay_policy=short_stay_policy,
            long_stay_policy=long_stay_policy,
            non_refundable=non_refundable,
        )


        get_airbnb_booking_settings_response_200_data_cancellation.additional_properties = d
        return get_airbnb_booking_settings_response_200_data_cancellation

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
