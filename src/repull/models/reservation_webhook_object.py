from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="ReservationWebhookObject")



@_attrs_define
class ReservationWebhookObject:
    """ Lightweight reservation snapshot delivered as `data.object` on every reservation webhook event. Stable across
    `reservation.created`, `reservation.updated`, and `reservation.cancelled`. Fetch the full reservation via `GET
    /v1/reservations/{id}` if you need pricing, guest contact info, or audit history — those are deliberately omitted to
    keep deliveries small.

        Attributes:
            id (int): Repull-internal reservation id. Pass to `GET /v1/reservations/{id}`. Example: 212605.
            uid (str): Channel-side confirmation code (Airbnb HM-prefixed, Booking.com numeric, etc.). Stable across the
                lifetime of the reservation. Example: HMX4CMA2X9.
            channel (str): Source channel — `airbnb`, `booking`, `vrbo`, `direct`, `owner`, `mid_stay_clean`, etc. Example:
                airbnb.
            listing_id (int): Repull listing id this reservation is on. Example: 5668.
            customer_id (int): Workspace (customer) id this reservation belongs to. Example: 1.
            checkin_date (datetime.date): Check-in date (local property date, no timezone). Example: 2026-06-10.
            checkout_date (datetime.date): Check-out date (local property date, no timezone). Example: 2026-06-16.
            status (str): Lifecycle status — typically `confirmed`, `cancelled`, `pending`, `inquiry`. Example: confirmed.
     """

    id: int
    uid: str
    channel: str
    listing_id: int
    customer_id: int
    checkin_date: datetime.date
    checkout_date: datetime.date
    status: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uid = self.uid

        channel = self.channel

        listing_id = self.listing_id

        customer_id = self.customer_id

        checkin_date = self.checkin_date.isoformat()

        checkout_date = self.checkout_date.isoformat()

        status = self.status


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "uid": uid,
            "channel": channel,
            "listingId": listing_id,
            "customerId": customer_id,
            "checkinDate": checkin_date,
            "checkoutDate": checkout_date,
            "status": status,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        uid = d.pop("uid")

        channel = d.pop("channel")

        listing_id = d.pop("listingId")

        customer_id = d.pop("customerId")

        checkin_date = isoparse(d.pop("checkinDate")).date()




        checkout_date = isoparse(d.pop("checkoutDate")).date()




        status = d.pop("status")

        reservation_webhook_object = cls(
            id=id,
            uid=uid,
            channel=channel,
            listing_id=listing_id,
            customer_id=customer_id,
            checkin_date=checkin_date,
            checkout_date=checkout_date,
            status=status,
        )


        reservation_webhook_object.additional_properties = d
        return reservation_webhook_object

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
