from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.reservation_guest_financials import ReservationGuestFinancials
  from ..models.reservation_host_financials import ReservationHostFinancials





T = TypeVar("T", bound="ReservationFinancials")



@_attrs_define
class ReservationFinancials:
    """ Normalized money block. `totalPrice` is a `number` (NOT a decimal-as-string) — the legacy top-level `totalPrice`
    string field is kept on the parent for back-compat but is deprecated. `totalPrice` is the GUEST-side stay total
    (what the guest paid), NOT the host payout.

    The full host/guest breakdown — accommodation subtotal, discounts, cleaning and other guest fees, channel service
    fees split host/guest, tax lines, and the expected host payout — is served inline under `host` and `guest` for EVERY
    channel. (Earlier versions of this spec sent you to `GET /v1/channels/airbnb/transactions` for the host payout; that
    endpoint is Airbnb-only and is no longer the place to look for a reservation's financials. It remains useful for
    settlement-level detail — actual payout dates and settlement status — which the reservation record does not carry.)

    Not yet served here: individual guest **payment records** (charges, refunds, schedules) and post-booking
    **adjustments** — neither is stored on the reservation breakdown.

        Attributes:
            total_price (float | None | Unset): GUEST-side stay total in `currency` — what the guest paid, not the host
                payout. Number, not string. For the host payout see `financials.host.revenue`. Example: 1250.
            currency (None | str | Unset): ISO 4217 currency code. Example: USD.
            payment_status (None | str | Unset): Payment lifecycle status (e.g. `pending`, `paid`, `refunded`).
            cancellation_policy (str | Unset): Channel cancellation policy code, verbatim from the reservation. Airbnb codes
                look like `strict_14_with_grace_period`, `moderate`, `flexible`, `tiered_pricing_non_refundable`; Booking.com
                reports a numeric policy id. Omitted when the channel did not supply one. Example: strict_14_with_grace_period.
            host (ReservationHostFinancials | Unset): HOST-side view of the stay — what it looks like on the host ledger.
                Projected from the reservation's own stored price breakdown, so it is available on every channel (Airbnb,
                Booking.com, VRBO, direct, owner), not just Airbnb.

                **Nothing here is synthesised.** A property is present only when the source breakdown genuinely carries it; a
                component the channel never reported is OMITTED rather than returned as `0`. An empty array means the channel
                reported an empty collection.
            guest (ReservationGuestFinancials | Unset): GUEST-side view of the stay — what the guest was actually charged.
                Same non-fabrication rule as `ReservationHostFinancials`: absent components are omitted, never zero-filled.
     """

    total_price: float | None | Unset = UNSET
    currency: None | str | Unset = UNSET
    payment_status: None | str | Unset = UNSET
    cancellation_policy: str | Unset = UNSET
    host: ReservationHostFinancials | Unset = UNSET
    guest: ReservationGuestFinancials | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.reservation_guest_financials import ReservationGuestFinancials
        from ..models.reservation_host_financials import ReservationHostFinancials
        total_price: float | None | Unset
        if isinstance(self.total_price, Unset):
            total_price = UNSET
        else:
            total_price = self.total_price

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        payment_status: None | str | Unset
        if isinstance(self.payment_status, Unset):
            payment_status = UNSET
        else:
            payment_status = self.payment_status

        cancellation_policy = self.cancellation_policy

        host: dict[str, Any] | Unset = UNSET
        if not isinstance(self.host, Unset):
            host = self.host.to_dict()

        guest: dict[str, Any] | Unset = UNSET
        if not isinstance(self.guest, Unset):
            guest = self.guest.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if total_price is not UNSET:
            field_dict["totalPrice"] = total_price
        if currency is not UNSET:
            field_dict["currency"] = currency
        if payment_status is not UNSET:
            field_dict["paymentStatus"] = payment_status
        if cancellation_policy is not UNSET:
            field_dict["cancellationPolicy"] = cancellation_policy
        if host is not UNSET:
            field_dict["host"] = host
        if guest is not UNSET:
            field_dict["guest"] = guest

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reservation_guest_financials import ReservationGuestFinancials
        from ..models.reservation_host_financials import ReservationHostFinancials
        d = dict(src_dict)
        def _parse_total_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        total_price = _parse_total_price(d.pop("totalPrice", UNSET))


        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))


        def _parse_payment_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payment_status = _parse_payment_status(d.pop("paymentStatus", UNSET))


        cancellation_policy = d.pop("cancellationPolicy", UNSET)

        _host = d.pop("host", UNSET)
        host: ReservationHostFinancials | Unset
        if isinstance(_host,  Unset):
            host = UNSET
        else:
            host = ReservationHostFinancials.from_dict(_host)




        _guest = d.pop("guest", UNSET)
        guest: ReservationGuestFinancials | Unset
        if isinstance(_guest,  Unset):
            guest = UNSET
        else:
            guest = ReservationGuestFinancials.from_dict(_guest)




        reservation_financials = cls(
            total_price=total_price,
            currency=currency,
            payment_status=payment_status,
            cancellation_policy=cancellation_policy,
            host=host,
            guest=guest,
        )


        reservation_financials.additional_properties = d
        return reservation_financials

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
