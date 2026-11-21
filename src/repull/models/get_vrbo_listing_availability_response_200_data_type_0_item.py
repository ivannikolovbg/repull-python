from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_vrbo_listing_availability_response_200_data_type_0_item_blocked_by_type_1 import GetVrboListingAvailabilityResponse200DataType0ItemBlockedByType1
from ..models.get_vrbo_listing_availability_response_200_data_type_0_item_blocked_by_type_2_type_1 import GetVrboListingAvailabilityResponse200DataType0ItemBlockedByType2Type1
from ..models.get_vrbo_listing_availability_response_200_data_type_0_item_blocked_by_type_3_type_1 import GetVrboListingAvailabilityResponse200DataType0ItemBlockedByType3Type1
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="GetVrboListingAvailabilityResponse200DataType0Item")



@_attrs_define
class GetVrboListingAvailabilityResponse200DataType0Item:
    """ 
        Attributes:
            date (datetime.date | Unset):
            available (bool | Unset):
            blocked_by (GetVrboListingAvailabilityResponse200DataType0ItemBlockedByType1 |
                GetVrboListingAvailabilityResponse200DataType0ItemBlockedByType2Type1 |
                GetVrboListingAvailabilityResponse200DataType0ItemBlockedByType3Type1 | None | Unset):
            reservation_ref (None | str | Unset):
            nightly_rate (float | None | Unset):
            currency (None | str | Unset):
            min_stay (int | None | Unset):
            check_in (bool | None | Unset):
            check_out (bool | None | Unset):
     """

    date: datetime.date | Unset = UNSET
    available: bool | Unset = UNSET
    blocked_by: GetVrboListingAvailabilityResponse200DataType0ItemBlockedByType1 | GetVrboListingAvailabilityResponse200DataType0ItemBlockedByType2Type1 | GetVrboListingAvailabilityResponse200DataType0ItemBlockedByType3Type1 | None | Unset = UNSET
    reservation_ref: None | str | Unset = UNSET
    nightly_rate: float | None | Unset = UNSET
    currency: None | str | Unset = UNSET
    min_stay: int | None | Unset = UNSET
    check_in: bool | None | Unset = UNSET
    check_out: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        available = self.available

        blocked_by: None | str | Unset
        if isinstance(self.blocked_by, Unset):
            blocked_by = UNSET
        elif isinstance(self.blocked_by, GetVrboListingAvailabilityResponse200DataType0ItemBlockedByType1):
            blocked_by = self.blocked_by.value
        elif isinstance(self.blocked_by, GetVrboListingAvailabilityResponse200DataType0ItemBlockedByType2Type1):
            blocked_by = self.blocked_by.value
        elif isinstance(self.blocked_by, GetVrboListingAvailabilityResponse200DataType0ItemBlockedByType3Type1):
            blocked_by = self.blocked_by.value
        else:
            blocked_by = self.blocked_by

        reservation_ref: None | str | Unset
        if isinstance(self.reservation_ref, Unset):
            reservation_ref = UNSET
        else:
            reservation_ref = self.reservation_ref

        nightly_rate: float | None | Unset
        if isinstance(self.nightly_rate, Unset):
            nightly_rate = UNSET
        else:
            nightly_rate = self.nightly_rate

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        min_stay: int | None | Unset
        if isinstance(self.min_stay, Unset):
            min_stay = UNSET
        else:
            min_stay = self.min_stay

        check_in: bool | None | Unset
        if isinstance(self.check_in, Unset):
            check_in = UNSET
        else:
            check_in = self.check_in

        check_out: bool | None | Unset
        if isinstance(self.check_out, Unset):
            check_out = UNSET
        else:
            check_out = self.check_out


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if date is not UNSET:
            field_dict["date"] = date
        if available is not UNSET:
            field_dict["available"] = available
        if blocked_by is not UNSET:
            field_dict["blockedBy"] = blocked_by
        if reservation_ref is not UNSET:
            field_dict["reservationRef"] = reservation_ref
        if nightly_rate is not UNSET:
            field_dict["nightlyRate"] = nightly_rate
        if currency is not UNSET:
            field_dict["currency"] = currency
        if min_stay is not UNSET:
            field_dict["minStay"] = min_stay
        if check_in is not UNSET:
            field_dict["checkIn"] = check_in
        if check_out is not UNSET:
            field_dict["checkOut"] = check_out

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _date = d.pop("date", UNSET)
        date: datetime.date | Unset
        if isinstance(_date,  Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()




        available = d.pop("available", UNSET)

        def _parse_blocked_by(data: object) -> GetVrboListingAvailabilityResponse200DataType0ItemBlockedByType1 | GetVrboListingAvailabilityResponse200DataType0ItemBlockedByType2Type1 | GetVrboListingAvailabilityResponse200DataType0ItemBlockedByType3Type1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                blocked_by_type_1 = GetVrboListingAvailabilityResponse200DataType0ItemBlockedByType1(data)



                return blocked_by_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                blocked_by_type_2_type_1 = GetVrboListingAvailabilityResponse200DataType0ItemBlockedByType2Type1(data)



                return blocked_by_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                blocked_by_type_3_type_1 = GetVrboListingAvailabilityResponse200DataType0ItemBlockedByType3Type1(data)



                return blocked_by_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetVrboListingAvailabilityResponse200DataType0ItemBlockedByType1 | GetVrboListingAvailabilityResponse200DataType0ItemBlockedByType2Type1 | GetVrboListingAvailabilityResponse200DataType0ItemBlockedByType3Type1 | None | Unset, data)

        blocked_by = _parse_blocked_by(d.pop("blockedBy", UNSET))


        def _parse_reservation_ref(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reservation_ref = _parse_reservation_ref(d.pop("reservationRef", UNSET))


        def _parse_nightly_rate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        nightly_rate = _parse_nightly_rate(d.pop("nightlyRate", UNSET))


        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))


        def _parse_min_stay(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_stay = _parse_min_stay(d.pop("minStay", UNSET))


        def _parse_check_in(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        check_in = _parse_check_in(d.pop("checkIn", UNSET))


        def _parse_check_out(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        check_out = _parse_check_out(d.pop("checkOut", UNSET))


        get_vrbo_listing_availability_response_200_data_type_0_item = cls(
            date=date,
            available=available,
            blocked_by=blocked_by,
            reservation_ref=reservation_ref,
            nightly_rate=nightly_rate,
            currency=currency,
            min_stay=min_stay,
            check_in=check_in,
            check_out=check_out,
        )


        get_vrbo_listing_availability_response_200_data_type_0_item.additional_properties = d
        return get_vrbo_listing_availability_response_200_data_type_0_item

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
