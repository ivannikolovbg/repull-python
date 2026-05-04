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

if TYPE_CHECKING:
  from ..models.reservation_created_payload_guests import ReservationCreatedPayloadGuests
  from ..models.reservation_created_payload_pricing import ReservationCreatedPayloadPricing
  from ..models.reservation_created_payload_primary_guest import ReservationCreatedPayloadPrimaryGuest





T = TypeVar("T", bound="ReservationCreatedPayload")



@_attrs_define
class ReservationCreatedPayload:
    """ Payload for `reservation.created`. A new reservation arrived from any connected channel or direct booking.

        Attributes:
            id (int | Unset):  Example: 215906.
            confirmation_code (str | Unset):  Example: HMA1234567.
            listing_id (int | Unset):  Example: 6250.
            platform (str | Unset):  Example: airbnb.
            status (str | Unset):  Example: confirmed.
            check_in (datetime.date | Unset):  Example: 2026-06-01.
            check_out (datetime.date | Unset):  Example: 2026-06-05.
            nights (int | Unset):  Example: 4.
            guests (ReservationCreatedPayloadGuests | Unset):
            primary_guest (ReservationCreatedPayloadPrimaryGuest | Unset):
            pricing (ReservationCreatedPayloadPricing | Unset):
            created_at (datetime.datetime | Unset):  Example: 2026-05-01T12:34:56.000Z.
     """

    id: int | Unset = UNSET
    confirmation_code: str | Unset = UNSET
    listing_id: int | Unset = UNSET
    platform: str | Unset = UNSET
    status: str | Unset = UNSET
    check_in: datetime.date | Unset = UNSET
    check_out: datetime.date | Unset = UNSET
    nights: int | Unset = UNSET
    guests: ReservationCreatedPayloadGuests | Unset = UNSET
    primary_guest: ReservationCreatedPayloadPrimaryGuest | Unset = UNSET
    pricing: ReservationCreatedPayloadPricing | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.reservation_created_payload_guests import ReservationCreatedPayloadGuests
        from ..models.reservation_created_payload_pricing import ReservationCreatedPayloadPricing
        from ..models.reservation_created_payload_primary_guest import ReservationCreatedPayloadPrimaryGuest
        id = self.id

        confirmation_code = self.confirmation_code

        listing_id = self.listing_id

        platform = self.platform

        status = self.status

        check_in: str | Unset = UNSET
        if not isinstance(self.check_in, Unset):
            check_in = self.check_in.isoformat()

        check_out: str | Unset = UNSET
        if not isinstance(self.check_out, Unset):
            check_out = self.check_out.isoformat()

        nights = self.nights

        guests: dict[str, Any] | Unset = UNSET
        if not isinstance(self.guests, Unset):
            guests = self.guests.to_dict()

        primary_guest: dict[str, Any] | Unset = UNSET
        if not isinstance(self.primary_guest, Unset):
            primary_guest = self.primary_guest.to_dict()

        pricing: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pricing, Unset):
            pricing = self.pricing.to_dict()

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if confirmation_code is not UNSET:
            field_dict["confirmationCode"] = confirmation_code
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if platform is not UNSET:
            field_dict["platform"] = platform
        if status is not UNSET:
            field_dict["status"] = status
        if check_in is not UNSET:
            field_dict["checkIn"] = check_in
        if check_out is not UNSET:
            field_dict["checkOut"] = check_out
        if nights is not UNSET:
            field_dict["nights"] = nights
        if guests is not UNSET:
            field_dict["guests"] = guests
        if primary_guest is not UNSET:
            field_dict["primaryGuest"] = primary_guest
        if pricing is not UNSET:
            field_dict["pricing"] = pricing
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reservation_created_payload_guests import ReservationCreatedPayloadGuests
        from ..models.reservation_created_payload_pricing import ReservationCreatedPayloadPricing
        from ..models.reservation_created_payload_primary_guest import ReservationCreatedPayloadPrimaryGuest
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        confirmation_code = d.pop("confirmationCode", UNSET)

        listing_id = d.pop("listingId", UNSET)

        platform = d.pop("platform", UNSET)

        status = d.pop("status", UNSET)

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




        nights = d.pop("nights", UNSET)

        _guests = d.pop("guests", UNSET)
        guests: ReservationCreatedPayloadGuests | Unset
        if isinstance(_guests,  Unset):
            guests = UNSET
        else:
            guests = ReservationCreatedPayloadGuests.from_dict(_guests)




        _primary_guest = d.pop("primaryGuest", UNSET)
        primary_guest: ReservationCreatedPayloadPrimaryGuest | Unset
        if isinstance(_primary_guest,  Unset):
            primary_guest = UNSET
        else:
            primary_guest = ReservationCreatedPayloadPrimaryGuest.from_dict(_primary_guest)




        _pricing = d.pop("pricing", UNSET)
        pricing: ReservationCreatedPayloadPricing | Unset
        if isinstance(_pricing,  Unset):
            pricing = UNSET
        else:
            pricing = ReservationCreatedPayloadPricing.from_dict(_pricing)




        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        reservation_created_payload = cls(
            id=id,
            confirmation_code=confirmation_code,
            listing_id=listing_id,
            platform=platform,
            status=status,
            check_in=check_in,
            check_out=check_out,
            nights=nights,
            guests=guests,
            primary_guest=primary_guest,
            pricing=pricing,
            created_at=created_at,
        )


        reservation_created_payload.additional_properties = d
        return reservation_created_payload

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
