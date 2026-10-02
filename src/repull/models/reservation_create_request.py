from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.reservation_create_request_platform import ReservationCreateRequestPlatform
from ..models.reservation_create_request_status import ReservationCreateRequestStatus
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.reservation_guest_input import ReservationGuestInput





T = TypeVar("T", bound="ReservationCreateRequest")



@_attrs_define
class ReservationCreateRequest:
    """ Which fields a listing takes depends on whether it is managed in a PMS — see the operation description and `GET
    /v1/listings/{id}` → `capabilities.reservations`. A field the listing cannot take is refused by name (`422
    unsupported_field`), never dropped.

        Attributes:
            listing_id (int): Internal Repull property id — see `GET /v1/properties`. Example: 4118.
            check_in (datetime.date):  Example: 2026-10-01.
            check_out (datetime.date): Must be after `checkIn`. Example: 2026-10-05.
            guest (ReservationGuestInput): The guest on a new reservation. Matched against existing guests on email (then
                phone) plus name, so repeat guests are not duplicated.
            platform (ReservationCreateRequestPlatform | Unset): OTA platforms are deliberately absent — those reservations
                are owned by the channel and arrive through sync. `owner` is refused on a PMS listing (block owner stays in the
                PMS). Default: ReservationCreateRequestPlatform.DIRECT.
            status (ReservationCreateRequestStatus | Unset): `confirmed` (default) or `tentative` (an optional hold, where
                the PMS has one). On a listing not managed in a PMS the value is passed to the reservation pipeline as before.
                Default: ReservationCreateRequestStatus.CONFIRMED.
            adults (int | Unset):  Example: 2.
            children (int | Unset):  Example: 1.
            guest_count (int | Unset): Total guests. On a PMS listing without `adults`, used as the adult count. Example: 3.
            total_price (float | Unset): PMS listings only: the total for the whole stay, in the listing's currency.
                Honoured where `capabilities.reservations.customPrice` is true; omit it and the PMS prices the stay (from its
                quote where it has one). Refused on a listing not managed in a PMS, whose rate engine prices the stay. Example:
                880.
            notes (str | Unset): PMS listings only: booking notes stored in the PMS. Example: Late arrival, around 22:00..
            unit_id (str | Unset): PMS listings only: book this unit (`GET /v1/listings/{id}` → `units[].id`). Refused by
                PMSs that cannot target a unit. Example: 3f1c9a20.
            send_confirmation_email (bool | Unset): PMS listings only: ask the PMS to email the guest its own confirmation,
                where the PMS supports it.
            check_in_time (str | Unset): Listings not managed in a PMS only. Example: 16:00.
            check_out_time (str | Unset): Listings not managed in a PMS only. Example: 10:00.
            guest_id (int | Unset): Listings not managed in a PMS only: attach an existing guest instead of
                matching/creating one. Must belong to this workspace. Example: 91234.
            currency (str | Unset): Listings not managed in a PMS only (a PMS books in the property's currency). Example:
                USD.
     """

    listing_id: int
    check_in: datetime.date
    check_out: datetime.date
    guest: ReservationGuestInput
    platform: ReservationCreateRequestPlatform | Unset = ReservationCreateRequestPlatform.DIRECT
    status: ReservationCreateRequestStatus | Unset = ReservationCreateRequestStatus.CONFIRMED
    adults: int | Unset = UNSET
    children: int | Unset = UNSET
    guest_count: int | Unset = UNSET
    total_price: float | Unset = UNSET
    notes: str | Unset = UNSET
    unit_id: str | Unset = UNSET
    send_confirmation_email: bool | Unset = UNSET
    check_in_time: str | Unset = UNSET
    check_out_time: str | Unset = UNSET
    guest_id: int | Unset = UNSET
    currency: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.reservation_guest_input import ReservationGuestInput
        listing_id = self.listing_id

        check_in = self.check_in.isoformat()

        check_out = self.check_out.isoformat()

        guest = self.guest.to_dict()

        platform: str | Unset = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.value


        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        adults = self.adults

        children = self.children

        guest_count = self.guest_count

        total_price = self.total_price

        notes = self.notes

        unit_id = self.unit_id

        send_confirmation_email = self.send_confirmation_email

        check_in_time = self.check_in_time

        check_out_time = self.check_out_time

        guest_id = self.guest_id

        currency = self.currency


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "listingId": listing_id,
            "checkIn": check_in,
            "checkOut": check_out,
            "guest": guest,
        })
        if platform is not UNSET:
            field_dict["platform"] = platform
        if status is not UNSET:
            field_dict["status"] = status
        if adults is not UNSET:
            field_dict["adults"] = adults
        if children is not UNSET:
            field_dict["children"] = children
        if guest_count is not UNSET:
            field_dict["guestCount"] = guest_count
        if total_price is not UNSET:
            field_dict["totalPrice"] = total_price
        if notes is not UNSET:
            field_dict["notes"] = notes
        if unit_id is not UNSET:
            field_dict["unitId"] = unit_id
        if send_confirmation_email is not UNSET:
            field_dict["sendConfirmationEmail"] = send_confirmation_email
        if check_in_time is not UNSET:
            field_dict["checkInTime"] = check_in_time
        if check_out_time is not UNSET:
            field_dict["checkOutTime"] = check_out_time
        if guest_id is not UNSET:
            field_dict["guestId"] = guest_id
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reservation_guest_input import ReservationGuestInput
        d = dict(src_dict)
        listing_id = d.pop("listingId")

        check_in = isoparse(d.pop("checkIn")).date()




        check_out = isoparse(d.pop("checkOut")).date()




        guest = ReservationGuestInput.from_dict(d.pop("guest"))




        _platform = d.pop("platform", UNSET)
        platform: ReservationCreateRequestPlatform | Unset
        if isinstance(_platform,  Unset):
            platform = UNSET
        else:
            platform = ReservationCreateRequestPlatform(_platform)




        _status = d.pop("status", UNSET)
        status: ReservationCreateRequestStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = ReservationCreateRequestStatus(_status)




        adults = d.pop("adults", UNSET)

        children = d.pop("children", UNSET)

        guest_count = d.pop("guestCount", UNSET)

        total_price = d.pop("totalPrice", UNSET)

        notes = d.pop("notes", UNSET)

        unit_id = d.pop("unitId", UNSET)

        send_confirmation_email = d.pop("sendConfirmationEmail", UNSET)

        check_in_time = d.pop("checkInTime", UNSET)

        check_out_time = d.pop("checkOutTime", UNSET)

        guest_id = d.pop("guestId", UNSET)

        currency = d.pop("currency", UNSET)

        reservation_create_request = cls(
            listing_id=listing_id,
            check_in=check_in,
            check_out=check_out,
            guest=guest,
            platform=platform,
            status=status,
            adults=adults,
            children=children,
            guest_count=guest_count,
            total_price=total_price,
            notes=notes,
            unit_id=unit_id,
            send_confirmation_email=send_confirmation_email,
            check_in_time=check_in_time,
            check_out_time=check_out_time,
            guest_id=guest_id,
            currency=currency,
        )

        return reservation_create_request

