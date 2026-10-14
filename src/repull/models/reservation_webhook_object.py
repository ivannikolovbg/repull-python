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






T = TypeVar("T", bound="ReservationWebhookObject")



@_attrs_define
class ReservationWebhookObject:
    """ Lightweight reservation snapshot delivered as `data.object` on every reservation webhook event. Stable across
    `reservation.created`, `reservation.updated`, and `reservation.cancelled`. Fetch the full reservation via `GET
    /v1/reservations/{id}` if you need pricing, guest contact info, or audit history — those are deliberately omitted to
    keep deliveries small.

    **Stay terms are the one exception to that rule.** `cancellationPolicy`, `checkInTime` and `checkOutTime` ride on
    every delivery, because the decisions they drive — is a refund owed, when can housekeeping turn the unit over — are
    made at the moment the webhook lands, not on a follow-up fetch. They are operational parameters of the booking, not
    contact or payment data. Guest email, payment method and payment reference stay off the snapshot; see `GET
    /v1/reservations/{id}`.

    All three are `null` when the source channel did not supply them. They are never defaulted: a fabricated policy is
    worse than a missing one.

        Attributes:
            id (int): Repull-internal reservation id. Pass to `GET /v1/reservations/{id}`. Example: 900001.
            uid (str): Channel-side confirmation code (Airbnb HM-prefixed, Booking.com numeric, etc.). Stable across the
                lifetime of the reservation. Example: HMEXAMPLE1.
            channel (str): Source channel — `airbnb`, `booking`, `vrbo`, `direct`, `owner`, `mid_stay_clean`, etc. Example:
                airbnb.
            listing_id (int): Repull listing id this reservation is on. Example: 5668.
            customer_id (int): Workspace (customer) id this reservation belongs to. Example: 1.
            checkin_date (datetime.date): Check-in date (local property date, no timezone). Example: 2026-06-10.
            checkout_date (datetime.date): Check-out date (local property date, no timezone). Example: 2026-06-16.
            status (str): Lifecycle status — typically `confirmed`, `cancelled`, `pending`, `inquiry`. Example: confirmed.
            cancellation_policy (None | str | Unset): Cancellation policy the booking was made under, **verbatim from the
                source channel** — not normalised, because the codes do not mean the same thing across channels.

                - Airbnb, Vrbo, direct and owner bookings carry a named code: `flexible`, `moderate`, `firm_14`,
                `strict_14_with_grace_period`, `better_strict_with_grace_period`, `super_strict_30`, `super_strict_60`,
                `tiered_pricing_non_refundable`, `long_term_flexible`, `flexible_new`.
                - **Booking.com carries its numeric policy id as a string** (`"1"`, `"74"`, `"121"`). It is not self-describing
                — resolve it against the property's policy set on Booking.com.

                `null` when the channel supplied none (iCal-imported bookings, some legacy direct rows). Example: firm_14.
            check_in_time (None | str | Unset): Local check-in time, `HH:MM` on a 24-hour clock in the **property's own
                timezone** — not UTC, and not the subscriber's. Usually inherited from the listing policy, but per-reservation
                where the channel or an agreed early check-in overrides it. `null` when unknown. Example: 16:00.
            check_out_time (None | str | Unset): Local check-out time, `HH:MM` on a 24-hour clock in the property's own
                timezone. Pair it with `checkoutDate` to schedule the turnover. `null` when unknown. Example: 10:00.
            guest_notes (None | str | Unset): What the guest wrote with the booking — on Booking.com, the estimated arrival
                time and special requests. Free text. `null` when there were none. Example: Approximate time of arrival: between
                15:00 and 16:00.
            conversation_id (None | str | Unset): The conversation with this guest — pass it to `GET /v1/conversations/{id}`
                and `/v1/conversations/{id}/messages`. It is the same conversation from inquiry through pre-approval to the
                confirmed booking, and the same id the message webhooks carry, so a booking links straight to the messages that
                led to it. `null` when the channel has no conversation for this booking. Example: 164743.
            external_thread_id (None | str | Unset): The channel's own id for that conversation (Airbnb thread id,
                Booking.com conversation id, …). `null` when there is none. Example: 2680544213.
            inquiry_id (None | str | Unset): The inquiry this booking came from (`GET /v1/inquiries`), when the guest asked
                before booking. When an inquiry turns into a booking, `inquiry.updated` fires with `status: "booked"` and this
                reservation's id. `null` for bookings with no inquiry. Example: 25173.
     """

    id: int
    uid: str
    channel: str
    listing_id: int
    customer_id: int
    checkin_date: datetime.date
    checkout_date: datetime.date
    status: str
    cancellation_policy: None | str | Unset = UNSET
    check_in_time: None | str | Unset = UNSET
    check_out_time: None | str | Unset = UNSET
    guest_notes: None | str | Unset = UNSET
    conversation_id: None | str | Unset = UNSET
    external_thread_id: None | str | Unset = UNSET
    inquiry_id: None | str | Unset = UNSET
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

        cancellation_policy: None | str | Unset
        if isinstance(self.cancellation_policy, Unset):
            cancellation_policy = UNSET
        else:
            cancellation_policy = self.cancellation_policy

        check_in_time: None | str | Unset
        if isinstance(self.check_in_time, Unset):
            check_in_time = UNSET
        else:
            check_in_time = self.check_in_time

        check_out_time: None | str | Unset
        if isinstance(self.check_out_time, Unset):
            check_out_time = UNSET
        else:
            check_out_time = self.check_out_time

        guest_notes: None | str | Unset
        if isinstance(self.guest_notes, Unset):
            guest_notes = UNSET
        else:
            guest_notes = self.guest_notes

        conversation_id: None | str | Unset
        if isinstance(self.conversation_id, Unset):
            conversation_id = UNSET
        else:
            conversation_id = self.conversation_id

        external_thread_id: None | str | Unset
        if isinstance(self.external_thread_id, Unset):
            external_thread_id = UNSET
        else:
            external_thread_id = self.external_thread_id

        inquiry_id: None | str | Unset
        if isinstance(self.inquiry_id, Unset):
            inquiry_id = UNSET
        else:
            inquiry_id = self.inquiry_id


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
        if cancellation_policy is not UNSET:
            field_dict["cancellationPolicy"] = cancellation_policy
        if check_in_time is not UNSET:
            field_dict["checkInTime"] = check_in_time
        if check_out_time is not UNSET:
            field_dict["checkOutTime"] = check_out_time
        if guest_notes is not UNSET:
            field_dict["guestNotes"] = guest_notes
        if conversation_id is not UNSET:
            field_dict["conversationId"] = conversation_id
        if external_thread_id is not UNSET:
            field_dict["externalThreadId"] = external_thread_id
        if inquiry_id is not UNSET:
            field_dict["inquiryId"] = inquiry_id

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

        def _parse_cancellation_policy(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cancellation_policy = _parse_cancellation_policy(d.pop("cancellationPolicy", UNSET))


        def _parse_check_in_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        check_in_time = _parse_check_in_time(d.pop("checkInTime", UNSET))


        def _parse_check_out_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        check_out_time = _parse_check_out_time(d.pop("checkOutTime", UNSET))


        def _parse_guest_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        guest_notes = _parse_guest_notes(d.pop("guestNotes", UNSET))


        def _parse_conversation_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        conversation_id = _parse_conversation_id(d.pop("conversationId", UNSET))


        def _parse_external_thread_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_thread_id = _parse_external_thread_id(d.pop("externalThreadId", UNSET))


        def _parse_inquiry_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        inquiry_id = _parse_inquiry_id(d.pop("inquiryId", UNSET))


        reservation_webhook_object = cls(
            id=id,
            uid=uid,
            channel=channel,
            listing_id=listing_id,
            customer_id=customer_id,
            checkin_date=checkin_date,
            checkout_date=checkout_date,
            status=status,
            cancellation_policy=cancellation_policy,
            check_in_time=check_in_time,
            check_out_time=check_out_time,
            guest_notes=guest_notes,
            conversation_id=conversation_id,
            external_thread_id=external_thread_id,
            inquiry_id=inquiry_id,
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
