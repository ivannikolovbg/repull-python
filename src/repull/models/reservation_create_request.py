from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.reservation_create_request_platform import ReservationCreateRequestPlatform
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.reservation_guest_input import ReservationGuestInput





T = TypeVar("T", bound="ReservationCreateRequest")



@_attrs_define
class ReservationCreateRequest:
    """ 
        Attributes:
            listing_id (int): Internal Repull property id — see `GET /v1/properties`. Example: 4118.
            check_in (datetime.date):  Example: 2026-10-01.
            check_out (datetime.date): Must be after `checkIn`. Example: 2026-10-05.
            guest (ReservationGuestInput): The guest on a new reservation. Matched against existing guests on email (then
                phone) plus name, so repeat guests are not duplicated.
            platform (ReservationCreateRequestPlatform | Unset): OTA platforms are deliberately absent — those reservations
                are owned by the channel and arrive through sync. Default: ReservationCreateRequestPlatform.DIRECT.
            status (str | Unset): Lifecycle status to open the reservation in. Defaults to confirmed. Default: 'accept'.
            check_in_time (str | Unset):  Example: 16:00.
            check_out_time (str | Unset):  Example: 10:00.
            guest_id (int | Unset): Attach an existing guest instead of matching/creating one. Must belong to this
                workspace. Example: 91234.
            guest_count (int | Unset):  Example: 2.
            currency (str | Unset):  Example: USD.
     """

    listing_id: int
    check_in: datetime.date
    check_out: datetime.date
    guest: ReservationGuestInput
    platform: ReservationCreateRequestPlatform | Unset = ReservationCreateRequestPlatform.DIRECT
    status: str | Unset = 'accept'
    check_in_time: str | Unset = UNSET
    check_out_time: str | Unset = UNSET
    guest_id: int | Unset = UNSET
    guest_count: int | Unset = UNSET
    currency: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.reservation_guest_input import ReservationGuestInput
        listing_id = self.listing_id

        check_in = self.check_in.isoformat()

        check_out = self.check_out.isoformat()

        guest = self.guest.to_dict()

        platform: str | Unset = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.value


        status = self.status

        check_in_time = self.check_in_time

        check_out_time = self.check_out_time

        guest_id = self.guest_id

        guest_count = self.guest_count

        currency = self.currency


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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
        if check_in_time is not UNSET:
            field_dict["checkInTime"] = check_in_time
        if check_out_time is not UNSET:
            field_dict["checkOutTime"] = check_out_time
        if guest_id is not UNSET:
            field_dict["guestId"] = guest_id
        if guest_count is not UNSET:
            field_dict["guestCount"] = guest_count
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




        status = d.pop("status", UNSET)

        check_in_time = d.pop("checkInTime", UNSET)

        check_out_time = d.pop("checkOutTime", UNSET)

        guest_id = d.pop("guestId", UNSET)

        guest_count = d.pop("guestCount", UNSET)

        currency = d.pop("currency", UNSET)

        reservation_create_request = cls(
            listing_id=listing_id,
            check_in=check_in,
            check_out=check_out,
            guest=guest,
            platform=platform,
            status=status,
            check_in_time=check_in_time,
            check_out_time=check_out_time,
            guest_id=guest_id,
            guest_count=guest_count,
            currency=currency,
        )


        reservation_create_request.additional_properties = d
        return reservation_create_request

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
