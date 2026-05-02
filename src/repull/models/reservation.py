from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.reservation_platform_type_1 import ReservationPlatformType1
from ..models.reservation_platform_type_2_type_1 import ReservationPlatformType2Type1
from ..models.reservation_platform_type_3_type_1 import ReservationPlatformType3Type1
from ..models.reservation_status import ReservationStatus
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.reservation_guest_details import ReservationGuestDetails





T = TypeVar("T", bound="Reservation")



@_attrs_define
class Reservation:
    """ A booking/reservation from a connected PMS. Identical shape between list-row (`GET /v1/reservations`) and detail
    (`GET /v1/reservations/{id}`) — SDK consumers can use the same type for both.

        Attributes:
            id (int): Internal Repull reservation ID
            listing_id (int): Internal Repull listing ID this reservation is on.
            guest_id (int): Internal Repull guest ID. Use `GET /v1/guests/{id}` for the full profile.
            check_in (datetime.date):  Example: 2026-04-15.
            check_out (datetime.date):  Example: 2026-04-20.
            status (ReservationStatus):  Example: confirmed.
            total_price (str): Decimal-as-string (precision 10, scale 2) to preserve precision across mixed-currency totals.
                Example: 1250.00.
            currency (str): ISO 4217 currency code. Example: USD.
            confirmation_code (str): Channel-side confirmation code (Airbnb HMxxx, Booking.com numeric, etc.). Example:
                HMXYZ123.
            guest_details (ReservationGuestDetails): Raw guest details from the source channel (firstName, lastName, email,
                phone, count, etc.). Shape varies by platform — use the dedicated guest endpoint for a normalized profile.
            created_at (datetime.datetime): When the reservation row was created in Repull (not the booking-on-channel
                timestamp).
            platform (None | ReservationPlatformType1 | ReservationPlatformType2Type1 | ReservationPlatformType3Type1 |
                Unset): Booking source. Lowercase. May be null on legacy rows. Example: airbnb.
            guest_name (None | str | Unset): Pre-resolved display name (`firstName lastName`) extracted from `guestDetails`.
                Null when no first name is available.
     """

    id: int
    listing_id: int
    guest_id: int
    check_in: datetime.date
    check_out: datetime.date
    status: ReservationStatus
    total_price: str
    currency: str
    confirmation_code: str
    guest_details: ReservationGuestDetails
    created_at: datetime.datetime
    platform: None | ReservationPlatformType1 | ReservationPlatformType2Type1 | ReservationPlatformType3Type1 | Unset = UNSET
    guest_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.reservation_guest_details import ReservationGuestDetails
        id = self.id

        listing_id = self.listing_id

        guest_id = self.guest_id

        check_in = self.check_in.isoformat()

        check_out = self.check_out.isoformat()

        status = self.status.value

        total_price = self.total_price

        currency = self.currency

        confirmation_code = self.confirmation_code

        guest_details = self.guest_details.to_dict()

        created_at = self.created_at.isoformat()

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
            "guestId": guest_id,
            "checkIn": check_in,
            "checkOut": check_out,
            "status": status,
            "totalPrice": total_price,
            "currency": currency,
            "confirmationCode": confirmation_code,
            "guestDetails": guest_details,
            "createdAt": created_at,
        })
        if platform is not UNSET:
            field_dict["platform"] = platform
        if guest_name is not UNSET:
            field_dict["guestName"] = guest_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reservation_guest_details import ReservationGuestDetails
        d = dict(src_dict)
        id = d.pop("id")

        listing_id = d.pop("listingId")

        guest_id = d.pop("guestId")

        check_in = isoparse(d.pop("checkIn")).date()




        check_out = isoparse(d.pop("checkOut")).date()




        status = ReservationStatus(d.pop("status"))




        total_price = d.pop("totalPrice")

        currency = d.pop("currency")

        confirmation_code = d.pop("confirmationCode")

        guest_details = ReservationGuestDetails.from_dict(d.pop("guestDetails"))




        created_at = isoparse(d.pop("createdAt"))




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
            guest_id=guest_id,
            check_in=check_in,
            check_out=check_out,
            status=status,
            total_price=total_price,
            currency=currency,
            confirmation_code=confirmation_code,
            guest_details=guest_details,
            created_at=created_at,
            platform=platform,
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
