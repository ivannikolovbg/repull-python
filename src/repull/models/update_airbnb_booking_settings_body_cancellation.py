from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.update_airbnb_booking_settings_body_cancellation_short_stay_policy import UpdateAirbnbBookingSettingsBodyCancellationShortStayPolicy
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_airbnb_booking_settings_body_cancellation_non_refundable import UpdateAirbnbBookingSettingsBodyCancellationNonRefundable





T = TypeVar("T", bound="UpdateAirbnbBookingSettingsBodyCancellation")



@_attrs_define
class UpdateAirbnbBookingSettingsBodyCancellation:
    """ 
        Attributes:
            short_stay_policy (UpdateAirbnbBookingSettingsBodyCancellationShortStayPolicy | Unset):
            long_stay_policy (None | str | Unset):
            non_refundable (UpdateAirbnbBookingSettingsBodyCancellationNonRefundable | Unset): `enabled: true` requires
                `discountPercent`; `enabled: false` sets the price factor to 1.0 (no discount). Repull converts the percentage
                to the factor Airbnb stores — 10% becomes 0.9 — and refuses anything over 30%, which is Airbnb's 0.7 floor.
     """

    short_stay_policy: UpdateAirbnbBookingSettingsBodyCancellationShortStayPolicy | Unset = UNSET
    long_stay_policy: None | str | Unset = UNSET
    non_refundable: UpdateAirbnbBookingSettingsBodyCancellationNonRefundable | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_airbnb_booking_settings_body_cancellation_non_refundable import UpdateAirbnbBookingSettingsBodyCancellationNonRefundable
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
        from ..models.update_airbnb_booking_settings_body_cancellation_non_refundable import UpdateAirbnbBookingSettingsBodyCancellationNonRefundable
        d = dict(src_dict)
        _short_stay_policy = d.pop("shortStayPolicy", UNSET)
        short_stay_policy: UpdateAirbnbBookingSettingsBodyCancellationShortStayPolicy | Unset
        if isinstance(_short_stay_policy,  Unset):
            short_stay_policy = UNSET
        else:
            short_stay_policy = UpdateAirbnbBookingSettingsBodyCancellationShortStayPolicy(_short_stay_policy)




        def _parse_long_stay_policy(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        long_stay_policy = _parse_long_stay_policy(d.pop("longStayPolicy", UNSET))


        _non_refundable = d.pop("nonRefundable", UNSET)
        non_refundable: UpdateAirbnbBookingSettingsBodyCancellationNonRefundable | Unset
        if isinstance(_non_refundable,  Unset):
            non_refundable = UNSET
        else:
            non_refundable = UpdateAirbnbBookingSettingsBodyCancellationNonRefundable.from_dict(_non_refundable)




        update_airbnb_booking_settings_body_cancellation = cls(
            short_stay_policy=short_stay_policy,
            long_stay_policy=long_stay_policy,
            non_refundable=non_refundable,
        )

        return update_airbnb_booking_settings_body_cancellation

