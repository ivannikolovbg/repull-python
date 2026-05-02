from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.airbnb_reservation_status import AirbnbReservationStatus
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="AirbnbReservation")



@_attrs_define
class AirbnbReservation:
    """ An Airbnb reservation as returned by the channel API. Use `confirmationCode` to address it in Airbnb operations.

        Attributes:
            confirmation_code (str | Unset):  Example: HMABC12345.
            listing_id (str | Unset):
            status (AirbnbReservationStatus | Unset):  Example: accepted.
            check_in (datetime.date | Unset):
            check_out (datetime.date | Unset):
            guest_name (None | str | Unset):
            guest_count (int | None | Unset):
            total_price (float | None | Unset):
            currency (None | str | Unset):
     """

    confirmation_code: str | Unset = UNSET
    listing_id: str | Unset = UNSET
    status: AirbnbReservationStatus | Unset = UNSET
    check_in: datetime.date | Unset = UNSET
    check_out: datetime.date | Unset = UNSET
    guest_name: None | str | Unset = UNSET
    guest_count: int | None | Unset = UNSET
    total_price: float | None | Unset = UNSET
    currency: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        confirmation_code = self.confirmation_code

        listing_id = self.listing_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        check_in: str | Unset = UNSET
        if not isinstance(self.check_in, Unset):
            check_in = self.check_in.isoformat()

        check_out: str | Unset = UNSET
        if not isinstance(self.check_out, Unset):
            check_out = self.check_out.isoformat()

        guest_name: None | str | Unset
        if isinstance(self.guest_name, Unset):
            guest_name = UNSET
        else:
            guest_name = self.guest_name

        guest_count: int | None | Unset
        if isinstance(self.guest_count, Unset):
            guest_count = UNSET
        else:
            guest_count = self.guest_count

        total_price: float | None | Unset
        if isinstance(self.total_price, Unset):
            total_price = UNSET
        else:
            total_price = self.total_price

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if confirmation_code is not UNSET:
            field_dict["confirmationCode"] = confirmation_code
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if status is not UNSET:
            field_dict["status"] = status
        if check_in is not UNSET:
            field_dict["checkIn"] = check_in
        if check_out is not UNSET:
            field_dict["checkOut"] = check_out
        if guest_name is not UNSET:
            field_dict["guestName"] = guest_name
        if guest_count is not UNSET:
            field_dict["guestCount"] = guest_count
        if total_price is not UNSET:
            field_dict["totalPrice"] = total_price
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        confirmation_code = d.pop("confirmationCode", UNSET)

        listing_id = d.pop("listingId", UNSET)

        _status = d.pop("status", UNSET)
        status: AirbnbReservationStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = AirbnbReservationStatus(_status)




        _check_in = d.pop("checkIn", UNSET)
        check_in: datetime.date | Unset
        if isinstance(_check_in,  Unset):
            check_in = UNSET
        else:
            check_in = isoparse(_check_in).date()




        _check_out = d.pop("checkOut", UNSET)
        check_out: datetime.date | Unset
        if isinstance(_check_out,  Unset):
            check_out = UNSET
        else:
            check_out = isoparse(_check_out).date()




        def _parse_guest_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        guest_name = _parse_guest_name(d.pop("guestName", UNSET))


        def _parse_guest_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        guest_count = _parse_guest_count(d.pop("guestCount", UNSET))


        def _parse_total_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        total_price = _parse_total_price(d.pop("totalPrice", UNSET))


        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))


        airbnb_reservation = cls(
            confirmation_code=confirmation_code,
            listing_id=listing_id,
            status=status,
            check_in=check_in,
            check_out=check_out,
            guest_name=guest_name,
            guest_count=guest_count,
            total_price=total_price,
            currency=currency,
        )


        airbnb_reservation.additional_properties = d
        return airbnb_reservation

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
