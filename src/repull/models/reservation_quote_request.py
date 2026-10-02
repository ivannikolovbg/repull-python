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






T = TypeVar("T", bound="ReservationQuoteRequest")



@_attrs_define
class ReservationQuoteRequest:
    """ 
        Attributes:
            listing_id (int):  Example: 4118.
            check_in (datetime.date):  Example: 2026-10-01.
            check_out (datetime.date): Must be after `checkIn`. Example: 2026-10-05.
            adults (int | Unset):  Example: 2.
            children (int | Unset):  Example: 1.
            guest_count (int | Unset): Total guests, when you do not split adults and children. Example: 3.
            unit_id (str | Unset): Quote one unit (`GET /v1/listings/{id}` → `units[].id`). Example: 3f1c9a20.
     """

    listing_id: int
    check_in: datetime.date
    check_out: datetime.date
    adults: int | Unset = UNSET
    children: int | Unset = UNSET
    guest_count: int | Unset = UNSET
    unit_id: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        listing_id = self.listing_id

        check_in = self.check_in.isoformat()

        check_out = self.check_out.isoformat()

        adults = self.adults

        children = self.children

        guest_count = self.guest_count

        unit_id = self.unit_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "listingId": listing_id,
            "checkIn": check_in,
            "checkOut": check_out,
        })
        if adults is not UNSET:
            field_dict["adults"] = adults
        if children is not UNSET:
            field_dict["children"] = children
        if guest_count is not UNSET:
            field_dict["guestCount"] = guest_count
        if unit_id is not UNSET:
            field_dict["unitId"] = unit_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        listing_id = d.pop("listingId")

        check_in = isoparse(d.pop("checkIn")).date()




        check_out = isoparse(d.pop("checkOut")).date()




        adults = d.pop("adults", UNSET)

        children = d.pop("children", UNSET)

        guest_count = d.pop("guestCount", UNSET)

        unit_id = d.pop("unitId", UNSET)

        reservation_quote_request = cls(
            listing_id=listing_id,
            check_in=check_in,
            check_out=check_out,
            adults=adults,
            children=children,
            guest_count=guest_count,
            unit_id=unit_id,
        )

        return reservation_quote_request

