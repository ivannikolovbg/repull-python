from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="CreateReservationBody")



@_attrs_define
class CreateReservationBody:
    """ 
        Attributes:
            property_id (str):
            check_in (datetime.date):
            check_out (datetime.date):
            guest_first_name (str):
            guest_last_name (str):
            guest_email (str | Unset):
            guest_phone (str | Unset):
            guest_count (int | Unset):
            total_price (float | Unset):
            currency (str | Unset):
     """

    property_id: str
    check_in: datetime.date
    check_out: datetime.date
    guest_first_name: str
    guest_last_name: str
    guest_email: str | Unset = UNSET
    guest_phone: str | Unset = UNSET
    guest_count: int | Unset = UNSET
    total_price: float | Unset = UNSET
    currency: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        property_id = self.property_id

        check_in = self.check_in.isoformat()

        check_out = self.check_out.isoformat()

        guest_first_name = self.guest_first_name

        guest_last_name = self.guest_last_name

        guest_email = self.guest_email

        guest_phone = self.guest_phone

        guest_count = self.guest_count

        total_price = self.total_price

        currency = self.currency


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "propertyId": property_id,
            "checkIn": check_in,
            "checkOut": check_out,
            "guestFirstName": guest_first_name,
            "guestLastName": guest_last_name,
        })
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

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        property_id = d.pop("propertyId")

        check_in = isoparse(d.pop("checkIn")).date()




        check_out = isoparse(d.pop("checkOut")).date()




        guest_first_name = d.pop("guestFirstName")

        guest_last_name = d.pop("guestLastName")

        guest_email = d.pop("guestEmail", UNSET)

        guest_phone = d.pop("guestPhone", UNSET)

        guest_count = d.pop("guestCount", UNSET)

        total_price = d.pop("totalPrice", UNSET)

        currency = d.pop("currency", UNSET)

        create_reservation_body = cls(
            property_id=property_id,
            check_in=check_in,
            check_out=check_out,
            guest_first_name=guest_first_name,
            guest_last_name=guest_last_name,
            guest_email=guest_email,
            guest_phone=guest_phone,
            guest_count=guest_count,
            total_price=total_price,
            currency=currency,
        )


        create_reservation_body.additional_properties = d
        return create_reservation_body

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
