from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GetReservationSummaryResponse200TotalsItem")



@_attrs_define
class GetReservationSummaryResponse200TotalsItem:
    """ 
        Attributes:
            currency (None | str): Money is never added across currencies: a period with two currencies has one row per
                currency. Example: CAD.
            reservations (int): Guest stays with at least one night counted (owner stays are in `ownerStays`). Example: 212.
            nights (int): Guest nights counted. Example: 1104.
            revenue (float): What guests paid (`financials.totalPrice`). With `basis=stay`, a stay that crosses the window
                or a month edge brings only the share of its nights inside. Example: 18250.4.
            payout (float): What the host receives (`financials.host.revenue`), for reservations where it is known. Example:
                18250.4.
            cancelled (int):  Example: 18.
            pending (int): Requests awaiting an answer; not in revenue or nights. Example: 2.
            owner_stays (int):  Example: 3.
            owner_nights (int):  Example: 12.
            month (str | Unset): Present when grouped by `month` (YYYY-MM). Example: 2026-12.
            listing_id (str | Unset): Present when grouped by `listing`. Example: 4011.
            listing_name (None | str | Unset): Present when grouped by `listing`. Example: Lakeside Cabin.
            channel (str | Unset): Present when grouped by `channel`. Example: airbnb.
            reservations_with_payout (int | Unset): How many reservations `payout` covers.
            average_nightly_rate (float | None | Unset): Accommodation per night (revenue per night when the accommodation
                subtotal is unknown). Example: 178.5.
            average_stay_nights (float | None | Unset):  Example: 5.2.
            average_lead_time_days (float | None | Unset): Days between booking and check-in. Example: 41.
            occupancy (float | None | Unset): Guest nights / available nights, 0–1. Only with `basis=stay`, and not when
                grouped by `channel`. Blocked nights are not subtracted from availability. Example: 0.6431.
            available_nights (float | None | Unset): Active listings × days in the period (one listing per row when grouped
                by `listing`). Example: 1716.
            cancelled_revenue (float | Unset):  Example: 18250.4.
     """

    currency: None | str
    reservations: int
    nights: int
    revenue: float
    payout: float
    cancelled: int
    pending: int
    owner_stays: int
    owner_nights: int
    month: str | Unset = UNSET
    listing_id: str | Unset = UNSET
    listing_name: None | str | Unset = UNSET
    channel: str | Unset = UNSET
    reservations_with_payout: int | Unset = UNSET
    average_nightly_rate: float | None | Unset = UNSET
    average_stay_nights: float | None | Unset = UNSET
    average_lead_time_days: float | None | Unset = UNSET
    occupancy: float | None | Unset = UNSET
    available_nights: float | None | Unset = UNSET
    cancelled_revenue: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        currency: None | str
        currency = self.currency

        reservations = self.reservations

        nights = self.nights

        revenue = self.revenue

        payout = self.payout

        cancelled = self.cancelled

        pending = self.pending

        owner_stays = self.owner_stays

        owner_nights = self.owner_nights

        month = self.month

        listing_id = self.listing_id

        listing_name: None | str | Unset
        if isinstance(self.listing_name, Unset):
            listing_name = UNSET
        else:
            listing_name = self.listing_name

        channel = self.channel

        reservations_with_payout = self.reservations_with_payout

        average_nightly_rate: float | None | Unset
        if isinstance(self.average_nightly_rate, Unset):
            average_nightly_rate = UNSET
        else:
            average_nightly_rate = self.average_nightly_rate

        average_stay_nights: float | None | Unset
        if isinstance(self.average_stay_nights, Unset):
            average_stay_nights = UNSET
        else:
            average_stay_nights = self.average_stay_nights

        average_lead_time_days: float | None | Unset
        if isinstance(self.average_lead_time_days, Unset):
            average_lead_time_days = UNSET
        else:
            average_lead_time_days = self.average_lead_time_days

        occupancy: float | None | Unset
        if isinstance(self.occupancy, Unset):
            occupancy = UNSET
        else:
            occupancy = self.occupancy

        available_nights: float | None | Unset
        if isinstance(self.available_nights, Unset):
            available_nights = UNSET
        else:
            available_nights = self.available_nights

        cancelled_revenue = self.cancelled_revenue


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "currency": currency,
            "reservations": reservations,
            "nights": nights,
            "revenue": revenue,
            "payout": payout,
            "cancelled": cancelled,
            "pending": pending,
            "ownerStays": owner_stays,
            "ownerNights": owner_nights,
        })
        if month is not UNSET:
            field_dict["month"] = month
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if listing_name is not UNSET:
            field_dict["listingName"] = listing_name
        if channel is not UNSET:
            field_dict["channel"] = channel
        if reservations_with_payout is not UNSET:
            field_dict["reservationsWithPayout"] = reservations_with_payout
        if average_nightly_rate is not UNSET:
            field_dict["averageNightlyRate"] = average_nightly_rate
        if average_stay_nights is not UNSET:
            field_dict["averageStayNights"] = average_stay_nights
        if average_lead_time_days is not UNSET:
            field_dict["averageLeadTimeDays"] = average_lead_time_days
        if occupancy is not UNSET:
            field_dict["occupancy"] = occupancy
        if available_nights is not UNSET:
            field_dict["availableNights"] = available_nights
        if cancelled_revenue is not UNSET:
            field_dict["cancelledRevenue"] = cancelled_revenue

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_currency(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        currency = _parse_currency(d.pop("currency"))


        reservations = d.pop("reservations")

        nights = d.pop("nights")

        revenue = d.pop("revenue")

        payout = d.pop("payout")

        cancelled = d.pop("cancelled")

        pending = d.pop("pending")

        owner_stays = d.pop("ownerStays")

        owner_nights = d.pop("ownerNights")

        month = d.pop("month", UNSET)

        listing_id = d.pop("listingId", UNSET)

        def _parse_listing_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        listing_name = _parse_listing_name(d.pop("listingName", UNSET))


        channel = d.pop("channel", UNSET)

        reservations_with_payout = d.pop("reservationsWithPayout", UNSET)

        def _parse_average_nightly_rate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        average_nightly_rate = _parse_average_nightly_rate(d.pop("averageNightlyRate", UNSET))


        def _parse_average_stay_nights(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        average_stay_nights = _parse_average_stay_nights(d.pop("averageStayNights", UNSET))


        def _parse_average_lead_time_days(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        average_lead_time_days = _parse_average_lead_time_days(d.pop("averageLeadTimeDays", UNSET))


        def _parse_occupancy(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        occupancy = _parse_occupancy(d.pop("occupancy", UNSET))


        def _parse_available_nights(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        available_nights = _parse_available_nights(d.pop("availableNights", UNSET))


        cancelled_revenue = d.pop("cancelledRevenue", UNSET)

        get_reservation_summary_response_200_totals_item = cls(
            currency=currency,
            reservations=reservations,
            nights=nights,
            revenue=revenue,
            payout=payout,
            cancelled=cancelled,
            pending=pending,
            owner_stays=owner_stays,
            owner_nights=owner_nights,
            month=month,
            listing_id=listing_id,
            listing_name=listing_name,
            channel=channel,
            reservations_with_payout=reservations_with_payout,
            average_nightly_rate=average_nightly_rate,
            average_stay_nights=average_stay_nights,
            average_lead_time_days=average_lead_time_days,
            occupancy=occupancy,
            available_nights=available_nights,
            cancelled_revenue=cancelled_revenue,
        )


        get_reservation_summary_response_200_totals_item.additional_properties = d
        return get_reservation_summary_response_200_totals_item

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
