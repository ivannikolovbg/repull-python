from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.reservation_platform_type_1 import ReservationPlatformType1
from ..models.reservation_platform_type_2_type_1 import ReservationPlatformType2Type1
from ..models.reservation_platform_type_3_type_1 import ReservationPlatformType3Type1
from ..models.reservation_source_type_1 import ReservationSourceType1
from ..models.reservation_source_type_2_type_1 import ReservationSourceType2Type1
from ..models.reservation_source_type_3_type_1 import ReservationSourceType3Type1
from ..models.reservation_status import ReservationStatus
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.reservation_financials import ReservationFinancials
  from ..models.reservation_guest_details import ReservationGuestDetails
  from ..models.reservation_occupancy import ReservationOccupancy
  from ..models.reservation_primary_guest import ReservationPrimaryGuest





T = TypeVar("T", bound="Reservation")



@_attrs_define
class Reservation:
    """ A booking/reservation from a connected PMS. Identical shape between list-row (`GET /v1/reservations`) and detail
    (`GET /v1/reservations/{id}`) — SDK consumers can use the same type for both.

    The canonical (post-2026-05) shape uses nested `primaryGuest`, `occupancy`, `financials` blocks. The legacy flat
    fields (`guestId`, `totalPrice`, `currency`, `guestDetails`) remain populated for back-compat and are marked
    `deprecated` here. New consumers should read from the nested blocks; existing consumers continue to work unchanged.

        Attributes:
            id (str): Internal Repull reservation ID
            listing_id (str): Internal Repull listing ID this reservation is on.
            check_in (datetime.date):  Example: 2026-04-15.
            check_out (datetime.date):  Example: 2026-04-20.
            status (ReservationStatus):  Example: confirmed.
            confirmation_code (str): Channel-side confirmation code (Airbnb HMxxx, Booking.com numeric, etc.). Example:
                HMXYZ123.
            created_at (datetime.datetime): When the reservation row was created in Repull (not the booking-on-channel
                timestamp).
            guest_id (str | Unset): DEPRECATED — use `primaryGuest.id`. Internal Repull guest ID. Kept populated for back-
                compat.
            source (None | ReservationSourceType1 | ReservationSourceType2Type1 | ReservationSourceType3Type1 | Unset):
                Booking source / channel. Lowercase. May be null on legacy rows. Canonical name as of 2026-05; `platform` is
                kept as an alias. Example: airbnb.
            platform (None | ReservationPlatformType1 | ReservationPlatformType2Type1 | ReservationPlatformType3Type1 |
                Unset): DEPRECATED alias for `source`. Same value, kept for back-compat. Example: airbnb.
            primary_guest (ReservationPrimaryGuest | Unset): Inline guest summary resolved by JOIN-ing the `guests` table.
                Populated for every reservation that has a linked guest row; OMITTED entirely (not null) for owner-blocks / pre-
                arrival rows / partial-sync gaps. Always optional-chain in SDK consumers.
            occupancy (ReservationOccupancy | Unset): Normalized guest counts for the stay. Mirrors the legacy
                `guestDetails.numberOf*` fields under canonical short names. Omitted when no count fields are present on the
                reservation.
            financials (ReservationFinancials | Unset): Normalized money block. `totalPrice` is a `number` (NOT a decimal-
                as-string) — the legacy top-level `totalPrice` string field is kept on the parent for back-compat but is
                deprecated.
            total_price (str | Unset): DEPRECATED — use `financials.totalPrice` (a number). Decimal-as-string (precision 10,
                scale 2) kept for back-compat. Example: 1250.00.
            currency (str | Unset): DEPRECATED — use `financials.currency`. ISO 4217 currency code. Example: USD.
            guest_details (ReservationGuestDetails | Unset): DEPRECATED — use `occupancy` for normalized counts and
                `primaryGuest` for guest identity. Raw guest details from the source channel; shape varies by platform.
            booked_at (datetime.datetime | None | Unset): When the booking was made on the source channel (when reported by
                the channel).
            guest_name (None | str | Unset): Pre-resolved display name (`firstName lastName`) from the joined guest row.
                Undefined when no first name is available.
     """

    id: str
    listing_id: str
    check_in: datetime.date
    check_out: datetime.date
    status: ReservationStatus
    confirmation_code: str
    created_at: datetime.datetime
    guest_id: str | Unset = UNSET
    source: None | ReservationSourceType1 | ReservationSourceType2Type1 | ReservationSourceType3Type1 | Unset = UNSET
    platform: None | ReservationPlatformType1 | ReservationPlatformType2Type1 | ReservationPlatformType3Type1 | Unset = UNSET
    primary_guest: ReservationPrimaryGuest | Unset = UNSET
    occupancy: ReservationOccupancy | Unset = UNSET
    financials: ReservationFinancials | Unset = UNSET
    total_price: str | Unset = UNSET
    currency: str | Unset = UNSET
    guest_details: ReservationGuestDetails | Unset = UNSET
    booked_at: datetime.datetime | None | Unset = UNSET
    guest_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.reservation_financials import ReservationFinancials
        from ..models.reservation_guest_details import ReservationGuestDetails
        from ..models.reservation_occupancy import ReservationOccupancy
        from ..models.reservation_primary_guest import ReservationPrimaryGuest
        id = self.id

        listing_id = self.listing_id

        check_in = self.check_in.isoformat()

        check_out = self.check_out.isoformat()

        status = self.status.value

        confirmation_code = self.confirmation_code

        created_at = self.created_at.isoformat()

        guest_id = self.guest_id

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        elif isinstance(self.source, ReservationSourceType1):
            source = self.source.value
        elif isinstance(self.source, ReservationSourceType2Type1):
            source = self.source.value
        elif isinstance(self.source, ReservationSourceType3Type1):
            source = self.source.value
        else:
            source = self.source

        platform: None | str | Unset
        if isinstance(self.platform, Unset):
            platform = UNSET
        elif isinstance(self.platform, ReservationPlatformType1):
            platform = self.platform.value
        elif isinstance(self.platform, ReservationPlatformType2Type1):
            platform = self.platform.value
        elif isinstance(self.platform, ReservationPlatformType3Type1):
            platform = self.platform.value
        else:
            platform = self.platform

        primary_guest: dict[str, Any] | Unset = UNSET
        if not isinstance(self.primary_guest, Unset):
            primary_guest = self.primary_guest.to_dict()

        occupancy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.occupancy, Unset):
            occupancy = self.occupancy.to_dict()

        financials: dict[str, Any] | Unset = UNSET
        if not isinstance(self.financials, Unset):
            financials = self.financials.to_dict()

        total_price = self.total_price

        currency = self.currency

        guest_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.guest_details, Unset):
            guest_details = self.guest_details.to_dict()

        booked_at: None | str | Unset
        if isinstance(self.booked_at, Unset):
            booked_at = UNSET
        elif isinstance(self.booked_at, datetime.datetime):
            booked_at = self.booked_at.isoformat()
        else:
            booked_at = self.booked_at

        guest_name: None | str | Unset
        if isinstance(self.guest_name, Unset):
            guest_name = UNSET
        else:
            guest_name = self.guest_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "listingId": listing_id,
            "checkIn": check_in,
            "checkOut": check_out,
            "status": status,
            "confirmationCode": confirmation_code,
            "createdAt": created_at,
        })
        if guest_id is not UNSET:
            field_dict["guestId"] = guest_id
        if source is not UNSET:
            field_dict["source"] = source
        if platform is not UNSET:
            field_dict["platform"] = platform
        if primary_guest is not UNSET:
            field_dict["primaryGuest"] = primary_guest
        if occupancy is not UNSET:
            field_dict["occupancy"] = occupancy
        if financials is not UNSET:
            field_dict["financials"] = financials
        if total_price is not UNSET:
            field_dict["totalPrice"] = total_price
        if currency is not UNSET:
            field_dict["currency"] = currency
        if guest_details is not UNSET:
            field_dict["guestDetails"] = guest_details
        if booked_at is not UNSET:
            field_dict["bookedAt"] = booked_at
        if guest_name is not UNSET:
            field_dict["guestName"] = guest_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reservation_financials import ReservationFinancials
        from ..models.reservation_guest_details import ReservationGuestDetails
        from ..models.reservation_occupancy import ReservationOccupancy
        from ..models.reservation_primary_guest import ReservationPrimaryGuest
        d = dict(src_dict)
        id = d.pop("id")

        listing_id = d.pop("listingId")

        check_in = isoparse(d.pop("checkIn")).date()




        check_out = isoparse(d.pop("checkOut")).date()




        status = ReservationStatus(d.pop("status"))




        confirmation_code = d.pop("confirmationCode")

        created_at = isoparse(d.pop("createdAt"))




        guest_id = d.pop("guestId", UNSET)

        def _parse_source(data: object) -> None | ReservationSourceType1 | ReservationSourceType2Type1 | ReservationSourceType3Type1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_type_1 = ReservationSourceType1(data)



                return source_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_type_2_type_1 = ReservationSourceType2Type1(data)



                return source_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_type_3_type_1 = ReservationSourceType3Type1(data)



                return source_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ReservationSourceType1 | ReservationSourceType2Type1 | ReservationSourceType3Type1 | Unset, data)

        source = _parse_source(d.pop("source", UNSET))


        def _parse_platform(data: object) -> None | ReservationPlatformType1 | ReservationPlatformType2Type1 | ReservationPlatformType3Type1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                platform_type_1 = ReservationPlatformType1(data)



                return platform_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                platform_type_2_type_1 = ReservationPlatformType2Type1(data)



                return platform_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                platform_type_3_type_1 = ReservationPlatformType3Type1(data)



                return platform_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ReservationPlatformType1 | ReservationPlatformType2Type1 | ReservationPlatformType3Type1 | Unset, data)

        platform = _parse_platform(d.pop("platform", UNSET))


        _primary_guest = d.pop("primaryGuest", UNSET)
        primary_guest: ReservationPrimaryGuest | Unset
        if isinstance(_primary_guest,  Unset):
            primary_guest = UNSET
        else:
            primary_guest = ReservationPrimaryGuest.from_dict(_primary_guest)




        _occupancy = d.pop("occupancy", UNSET)
        occupancy: ReservationOccupancy | Unset
        if isinstance(_occupancy,  Unset):
            occupancy = UNSET
        else:
            occupancy = ReservationOccupancy.from_dict(_occupancy)




        _financials = d.pop("financials", UNSET)
        financials: ReservationFinancials | Unset
        if isinstance(_financials,  Unset):
            financials = UNSET
        else:
            financials = ReservationFinancials.from_dict(_financials)




        total_price = d.pop("totalPrice", UNSET)

        currency = d.pop("currency", UNSET)

        _guest_details = d.pop("guestDetails", UNSET)
        guest_details: ReservationGuestDetails | Unset
        if isinstance(_guest_details,  Unset):
            guest_details = UNSET
        else:
            guest_details = ReservationGuestDetails.from_dict(_guest_details)




        def _parse_booked_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                booked_at_type_0 = isoparse(data)



                return booked_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        booked_at = _parse_booked_at(d.pop("bookedAt", UNSET))


        def _parse_guest_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        guest_name = _parse_guest_name(d.pop("guestName", UNSET))


        reservation = cls(
            id=id,
            listing_id=listing_id,
            check_in=check_in,
            check_out=check_out,
            status=status,
            confirmation_code=confirmation_code,
            created_at=created_at,
            guest_id=guest_id,
            source=source,
            platform=platform,
            primary_guest=primary_guest,
            occupancy=occupancy,
            financials=financials,
            total_price=total_price,
            currency=currency,
            guest_details=guest_details,
            booked_at=booked_at,
            guest_name=guest_name,
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
