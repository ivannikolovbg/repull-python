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
  from ..models.reservation_quote_response_breakdown_type_0 import ReservationQuoteResponseBreakdownType0





T = TypeVar("T", bound="ReservationQuoteResponse")



@_attrs_define
class ReservationQuoteResponse:
    """ 
        Attributes:
            listing_id (str | Unset):  Example: 4118.
            provider (str | Unset): The PMS that priced it. Example: hostaway.
            check_in (datetime.date | Unset):
            check_out (datetime.date | Unset):
            available (bool | Unset): Whether the PMS would take the booking as asked. Example: True.
            total (float | None | Unset): Total for the stay, in `currency`. Null when the PMS gave no price (e.g. not
                available). Example: 880.
            currency (None | str | Unset):  Example: USD.
            breakdown (None | ReservationQuoteResponseBreakdownType0 | Unset): The parts the PMS itemized; absent parts were
                not itemized.
            restrictions (list[str] | Unset): The PMS's reasons, verbatim, when `available` is false.
     """

    listing_id: str | Unset = UNSET
    provider: str | Unset = UNSET
    check_in: datetime.date | Unset = UNSET
    check_out: datetime.date | Unset = UNSET
    available: bool | Unset = UNSET
    total: float | None | Unset = UNSET
    currency: None | str | Unset = UNSET
    breakdown: None | ReservationQuoteResponseBreakdownType0 | Unset = UNSET
    restrictions: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.reservation_quote_response_breakdown_type_0 import ReservationQuoteResponseBreakdownType0
        listing_id = self.listing_id

        provider = self.provider

        check_in: str | Unset = UNSET
        if not isinstance(self.check_in, Unset):
            check_in = self.check_in.isoformat()

        check_out: str | Unset = UNSET
        if not isinstance(self.check_out, Unset):
            check_out = self.check_out.isoformat()

        available = self.available

        total: float | None | Unset
        if isinstance(self.total, Unset):
            total = UNSET
        else:
            total = self.total

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        breakdown: dict[str, Any] | None | Unset
        if isinstance(self.breakdown, Unset):
            breakdown = UNSET
        elif isinstance(self.breakdown, ReservationQuoteResponseBreakdownType0):
            breakdown = self.breakdown.to_dict()
        else:
            breakdown = self.breakdown

        restrictions: list[str] | Unset = UNSET
        if not isinstance(self.restrictions, Unset):
            restrictions = self.restrictions




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if provider is not UNSET:
            field_dict["provider"] = provider
        if check_in is not UNSET:
            field_dict["checkIn"] = check_in
        if check_out is not UNSET:
            field_dict["checkOut"] = check_out
        if available is not UNSET:
            field_dict["available"] = available
        if total is not UNSET:
            field_dict["total"] = total
        if currency is not UNSET:
            field_dict["currency"] = currency
        if breakdown is not UNSET:
            field_dict["breakdown"] = breakdown
        if restrictions is not UNSET:
            field_dict["restrictions"] = restrictions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reservation_quote_response_breakdown_type_0 import ReservationQuoteResponseBreakdownType0
        d = dict(src_dict)
        listing_id = d.pop("listingId", UNSET)

        provider = d.pop("provider", UNSET)

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




        available = d.pop("available", UNSET)

        def _parse_total(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        total = _parse_total(d.pop("total", UNSET))


        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))


        def _parse_breakdown(data: object) -> None | ReservationQuoteResponseBreakdownType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                breakdown_type_0 = ReservationQuoteResponseBreakdownType0.from_dict(data)



                return breakdown_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ReservationQuoteResponseBreakdownType0 | Unset, data)

        breakdown = _parse_breakdown(d.pop("breakdown", UNSET))


        restrictions = cast(list[str], d.pop("restrictions", UNSET))


        reservation_quote_response = cls(
            listing_id=listing_id,
            provider=provider,
            check_in=check_in,
            check_out=check_out,
            available=available,
            total=total,
            currency=currency,
            breakdown=breakdown,
            restrictions=restrictions,
        )


        reservation_quote_response.additional_properties = d
        return reservation_quote_response

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
