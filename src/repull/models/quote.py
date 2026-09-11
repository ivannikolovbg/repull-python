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
  from ..models.quote_pricing import QuotePricing





T = TypeVar("T", bound="Quote")



@_attrs_define
class Quote:
    """ 
        Attributes:
            listing_id (str | Unset):
            website_id (str | Unset):
            check_in (datetime.date | Unset):
            check_out (datetime.date | Unset):
            guests (int | Unset):
            nights (int | Unset):
            available (bool | Unset): False when the listing is unavailable for the range or outside its min/max stay. That
                is an answer, not an error.
            reason (str | Unset): Why it is unavailable. Present only when `available` is false.
            currency (str | Unset):
            available_units (float | None | Unset):
            pricing (QuotePricing | Unset):
     """

    listing_id: str | Unset = UNSET
    website_id: str | Unset = UNSET
    check_in: datetime.date | Unset = UNSET
    check_out: datetime.date | Unset = UNSET
    guests: int | Unset = UNSET
    nights: int | Unset = UNSET
    available: bool | Unset = UNSET
    reason: str | Unset = UNSET
    currency: str | Unset = UNSET
    available_units: float | None | Unset = UNSET
    pricing: QuotePricing | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.quote_pricing import QuotePricing
        listing_id = self.listing_id

        website_id = self.website_id

        check_in: str | Unset = UNSET
        if not isinstance(self.check_in, Unset):
            check_in = self.check_in.isoformat()

        check_out: str | Unset = UNSET
        if not isinstance(self.check_out, Unset):
            check_out = self.check_out.isoformat()

        guests = self.guests

        nights = self.nights

        available = self.available

        reason = self.reason

        currency = self.currency

        available_units: float | None | Unset
        if isinstance(self.available_units, Unset):
            available_units = UNSET
        else:
            available_units = self.available_units

        pricing: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pricing, Unset):
            pricing = self.pricing.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if website_id is not UNSET:
            field_dict["websiteId"] = website_id
        if check_in is not UNSET:
            field_dict["checkIn"] = check_in
        if check_out is not UNSET:
            field_dict["checkOut"] = check_out
        if guests is not UNSET:
            field_dict["guests"] = guests
        if nights is not UNSET:
            field_dict["nights"] = nights
        if available is not UNSET:
            field_dict["available"] = available
        if reason is not UNSET:
            field_dict["reason"] = reason
        if currency is not UNSET:
            field_dict["currency"] = currency
        if available_units is not UNSET:
            field_dict["availableUnits"] = available_units
        if pricing is not UNSET:
            field_dict["pricing"] = pricing

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.quote_pricing import QuotePricing
        d = dict(src_dict)
        listing_id = d.pop("listingId", UNSET)

        website_id = d.pop("websiteId", UNSET)

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




        guests = d.pop("guests", UNSET)

        nights = d.pop("nights", UNSET)

        available = d.pop("available", UNSET)

        reason = d.pop("reason", UNSET)

        currency = d.pop("currency", UNSET)

        def _parse_available_units(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        available_units = _parse_available_units(d.pop("availableUnits", UNSET))


        _pricing = d.pop("pricing", UNSET)
        pricing: QuotePricing | Unset
        if isinstance(_pricing,  Unset):
            pricing = UNSET
        else:
            pricing = QuotePricing.from_dict(_pricing)




        quote = cls(
            listing_id=listing_id,
            website_id=website_id,
            check_in=check_in,
            check_out=check_out,
            guests=guests,
            nights=nights,
            available=available,
            reason=reason,
            currency=currency,
            available_units=available_units,
            pricing=pricing,
        )


        quote.additional_properties = d
        return quote

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
