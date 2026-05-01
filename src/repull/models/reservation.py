from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.reservation_platform import ReservationPlatform
from ..models.reservation_status import ReservationStatus
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="Reservation")



@_attrs_define
class Reservation:
    """ A booking/reservation from a connected PMS

        Attributes:
            id (int | Unset): Internal Repull reservation ID
            confirmation_code (str | Unset): PMS confirmation code Example: HA-123456.
            property_id (int | Unset): Property ID
            platform (ReservationPlatform | Unset): Booking source Example: airbnb.
            status (ReservationStatus | Unset):  Example: confirmed.
            check_in (datetime.date | Unset):  Example: 2026-04-15.
            check_out (datetime.date | Unset):  Example: 2026-04-20.
            guest_first_name (str | Unset):  Example: John.
            guest_last_name (str | Unset):  Example: Smith.
            guest_email (str | Unset):
            guest_phone (str | Unset):
            guest_count (int | Unset):  Example: 4.
            total_price (float | Unset):  Example: 1250.
            currency (str | Unset):  Example: USD.
            provider (str | Unset):  Example: guesty.
     """

    id: int | Unset = UNSET
    confirmation_code: str | Unset = UNSET
    property_id: int | Unset = UNSET
    platform: ReservationPlatform | Unset = UNSET
    status: ReservationStatus | Unset = UNSET
    check_in: datetime.date | Unset = UNSET
    check_out: datetime.date | Unset = UNSET
    guest_first_name: str | Unset = UNSET
    guest_last_name: str | Unset = UNSET
    guest_email: str | Unset = UNSET
    guest_phone: str | Unset = UNSET
    guest_count: int | Unset = UNSET
    total_price: float | Unset = UNSET
    currency: str | Unset = UNSET
    provider: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        confirmation_code = self.confirmation_code

        property_id = self.property_id

        platform: str | Unset = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.value


        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        check_in: str | Unset = UNSET
        if not isinstance(self.check_in, Unset):
            check_in = self.check_in.isoformat()

        check_out: str | Unset = UNSET
        if not isinstance(self.check_out, Unset):
            check_out = self.check_out.isoformat()

        guest_first_name = self.guest_first_name

        guest_last_name = self.guest_last_name

        guest_email = self.guest_email

        guest_phone = self.guest_phone

        guest_count = self.guest_count

        total_price = self.total_price

        currency = self.currency

        provider = self.provider


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if confirmation_code is not UNSET:
            field_dict["confirmationCode"] = confirmation_code
        if property_id is not UNSET:
            field_dict["propertyId"] = property_id
        if platform is not UNSET:
            field_dict["platform"] = platform
        if status is not UNSET:
            field_dict["status"] = status
        if check_in is not UNSET:
            field_dict["checkIn"] = check_in
        if check_out is not UNSET:
            field_dict["checkOut"] = check_out
        if guest_first_name is not UNSET:
            field_dict["guestFirstName"] = guest_first_name
        if guest_last_name is not UNSET:
            field_dict["guestLastName"] = guest_last_name
        if guest_email is not UNSET:
            field_dict["guestEmail"] = guest_email
        if guest_phone is not UNSET:
            field_dict["guestPhone"] = guest_phone
        if guest_count is not UNSET:
            field_dict["guestCount"] = guest_count
        if total_price is not UNSET:
            field_dict["totalPrice"] = total_price
        if currency is not UNSET:
            field_dict["currency"] = currency
        if provider is not UNSET:
            field_dict["provider"] = provider

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        confirmation_code = d.pop("confirmationCode", UNSET)

        property_id = d.pop("propertyId", UNSET)

        _platform = d.pop("platform", UNSET)
        platform: ReservationPlatform | Unset
        if isinstance(_platform,  Unset):
            platform = UNSET
        else:
            platform = ReservationPlatform(_platform)




        _status = d.pop("status", UNSET)
        status: ReservationStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = ReservationStatus(_status)




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




        guest_first_name = d.pop("guestFirstName", UNSET)

        guest_last_name = d.pop("guestLastName", UNSET)

        guest_email = d.pop("guestEmail", UNSET)

        guest_phone = d.pop("guestPhone", UNSET)

        guest_count = d.pop("guestCount", UNSET)

        total_price = d.pop("totalPrice", UNSET)

        currency = d.pop("currency", UNSET)

        provider = d.pop("provider", UNSET)

        reservation = cls(
            id=id,
            confirmation_code=confirmation_code,
            property_id=property_id,
            platform=platform,
            status=status,
            check_in=check_in,
            check_out=check_out,
            guest_first_name=guest_first_name,
            guest_last_name=guest_last_name,
            guest_email=guest_email,
            guest_phone=guest_phone,
            guest_count=guest_count,
            total_price=total_price,
            currency=currency,
            provider=provider,
        )


        reservation.additional_properties = d
        return reservation

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
