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






T = TypeVar("T", bound="AirbnbAlterationCreateRequest")



@_attrs_define
class AirbnbAlterationCreateRequest:
    """ A proposed change to an existing Airbnb reservation. `confirmation_code` names the reservation; at least one of
    `check_in`, `check_out`, `number_of_guests`, `total_price` or `listing_id` must be sent with it, because an
    alteration that changes nothing is not something Airbnb can act on (it is refused with `422 invalid_params`).

    Unknown fields are refused rather than silently dropped. The older connector-native spellings (`start_date`,
    `end_date`, `total_price_override`, and an Airbnb guest-details object in place of `number_of_guests`) are still
    accepted for existing integrations; send the canonical names above in new code, and never a canonical field and its
    older spelling with different values.

        Attributes:
            confirmation_code (str): Airbnb confirmation code of the reservation to alter. `GET
                /v1/channels/airbnb/reservations` lists them. Example: HMX4CMA2X9.
            check_in (datetime.date | Unset): New check-in date, `YYYY-MM-DD`. Example: 2026-08-02.
            check_out (datetime.date | Unset): New check-out date, `YYYY-MM-DD`. Must be after `check_in` when both are
                sent. Example: 2026-08-06.
            number_of_guests (int | Unset): New guest count for the stay. Example: 3.
            total_price (float | Unset): New total for the whole stay, in the listing currency. Sent to Airbnb as the
                alteration's price override. Example: 640.
            listing_id (int | Unset): Move the reservation to this listing — a **listing transfer**. This is the **Repull**
                listing id (the `id` from `GET /v1/properties`), the same id every other Airbnb channel route takes; Repull
                verifies you own it, that it is active and connected to Airbnb, and translates it to the Airbnb listing id
                before sending it. Airbnb decides whether to honour the move. Example: 4118.
            airbnb_listing_id (str | Unset): The transfer target as the **Airbnb** listing id, for callers who hold that
                instead of the Repull id. Prefer `listing_id`. Sending both is allowed only when they name the same listing.
                Example: 18871326.
     """

    confirmation_code: str
    check_in: datetime.date | Unset = UNSET
    check_out: datetime.date | Unset = UNSET
    number_of_guests: int | Unset = UNSET
    total_price: float | Unset = UNSET
    listing_id: int | Unset = UNSET
    airbnb_listing_id: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        confirmation_code = self.confirmation_code

        check_in: str | Unset = UNSET
        if not isinstance(self.check_in, Unset):
            check_in = self.check_in.isoformat()

        check_out: str | Unset = UNSET
        if not isinstance(self.check_out, Unset):
            check_out = self.check_out.isoformat()

        number_of_guests = self.number_of_guests

        total_price = self.total_price

        listing_id = self.listing_id

        airbnb_listing_id = self.airbnb_listing_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "confirmation_code": confirmation_code,
        })
        if check_in is not UNSET:
            field_dict["check_in"] = check_in
        if check_out is not UNSET:
            field_dict["check_out"] = check_out
        if number_of_guests is not UNSET:
            field_dict["number_of_guests"] = number_of_guests
        if total_price is not UNSET:
            field_dict["total_price"] = total_price
        if listing_id is not UNSET:
            field_dict["listing_id"] = listing_id
        if airbnb_listing_id is not UNSET:
            field_dict["airbnb_listing_id"] = airbnb_listing_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        confirmation_code = d.pop("confirmation_code")

        _check_in = d.pop("check_in", UNSET)
        check_in: datetime.date | Unset
        if isinstance(_check_in,  Unset):
            check_in = UNSET
        else:
            check_in = isoparse(_check_in).date()




        _check_out = d.pop("check_out", UNSET)
        check_out: datetime.date | Unset
        if isinstance(_check_out,  Unset):
            check_out = UNSET
        else:
            check_out = isoparse(_check_out).date()




        number_of_guests = d.pop("number_of_guests", UNSET)

        total_price = d.pop("total_price", UNSET)

        listing_id = d.pop("listing_id", UNSET)

        airbnb_listing_id = d.pop("airbnb_listing_id", UNSET)

        airbnb_alteration_create_request = cls(
            confirmation_code=confirmation_code,
            check_in=check_in,
            check_out=check_out,
            number_of_guests=number_of_guests,
            total_price=total_price,
            listing_id=listing_id,
            airbnb_listing_id=airbnb_listing_id,
        )

        return airbnb_alteration_create_request

