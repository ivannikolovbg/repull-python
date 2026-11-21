from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="VrboReservationActionResponse200DataPenalties")



@_attrs_define
class VrboReservationActionResponse200DataPenalties:
    """ `cancel`: Vrbo's terms for a host cancellation.

        Attributes:
            cancellation_fee (None | str | Unset):
            listing_hidden (None | str | Unset):
            dates_blocked (bool | Unset):
     """

    cancellation_fee: None | str | Unset = UNSET
    listing_hidden: None | str | Unset = UNSET
    dates_blocked: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        cancellation_fee: None | str | Unset
        if isinstance(self.cancellation_fee, Unset):
            cancellation_fee = UNSET
        else:
            cancellation_fee = self.cancellation_fee

        listing_hidden: None | str | Unset
        if isinstance(self.listing_hidden, Unset):
            listing_hidden = UNSET
        else:
            listing_hidden = self.listing_hidden

        dates_blocked = self.dates_blocked


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if cancellation_fee is not UNSET:
            field_dict["cancellationFee"] = cancellation_fee
        if listing_hidden is not UNSET:
            field_dict["listingHidden"] = listing_hidden
        if dates_blocked is not UNSET:
            field_dict["datesBlocked"] = dates_blocked

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_cancellation_fee(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cancellation_fee = _parse_cancellation_fee(d.pop("cancellationFee", UNSET))


        def _parse_listing_hidden(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        listing_hidden = _parse_listing_hidden(d.pop("listingHidden", UNSET))


        dates_blocked = d.pop("datesBlocked", UNSET)

        vrbo_reservation_action_response_200_data_penalties = cls(
            cancellation_fee=cancellation_fee,
            listing_hidden=listing_hidden,
            dates_blocked=dates_blocked,
        )


        vrbo_reservation_action_response_200_data_penalties.additional_properties = d
        return vrbo_reservation_action_response_200_data_penalties

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
