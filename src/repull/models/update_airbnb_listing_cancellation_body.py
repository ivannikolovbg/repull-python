from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.update_airbnb_listing_cancellation_body_short_stay_policy import UpdateAirbnbListingCancellationBodyShortStayPolicy
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_airbnb_listing_cancellation_body_non_refundable import UpdateAirbnbListingCancellationBodyNonRefundable





T = TypeVar("T", bound="UpdateAirbnbListingCancellationBody")



@_attrs_define
class UpdateAirbnbListingCancellationBody:
    """ 
        Attributes:
            short_stay_policy (UpdateAirbnbListingCancellationBodyShortStayPolicy | Unset):
            long_stay_policy (None | str | Unset):
            non_refundable (UpdateAirbnbListingCancellationBodyNonRefundable | Unset):
     """

    short_stay_policy: UpdateAirbnbListingCancellationBodyShortStayPolicy | Unset = UNSET
    long_stay_policy: None | str | Unset = UNSET
    non_refundable: UpdateAirbnbListingCancellationBodyNonRefundable | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_airbnb_listing_cancellation_body_non_refundable import UpdateAirbnbListingCancellationBodyNonRefundable
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
        from ..models.update_airbnb_listing_cancellation_body_non_refundable import UpdateAirbnbListingCancellationBodyNonRefundable
        d = dict(src_dict)
        _short_stay_policy = d.pop("shortStayPolicy", UNSET)
        short_stay_policy: UpdateAirbnbListingCancellationBodyShortStayPolicy | Unset
        if isinstance(_short_stay_policy,  Unset):
            short_stay_policy = UNSET
        else:
            short_stay_policy = UpdateAirbnbListingCancellationBodyShortStayPolicy(_short_stay_policy)




        def _parse_long_stay_policy(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        long_stay_policy = _parse_long_stay_policy(d.pop("longStayPolicy", UNSET))


        _non_refundable = d.pop("nonRefundable", UNSET)
        non_refundable: UpdateAirbnbListingCancellationBodyNonRefundable | Unset
        if isinstance(_non_refundable,  Unset):
            non_refundable = UNSET
        else:
            non_refundable = UpdateAirbnbListingCancellationBodyNonRefundable.from_dict(_non_refundable)




        update_airbnb_listing_cancellation_body = cls(
            short_stay_policy=short_stay_policy,
            long_stay_policy=long_stay_policy,
            non_refundable=non_refundable,
        )

        return update_airbnb_listing_cancellation_body

