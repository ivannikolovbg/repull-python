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
  from ..models.tiket_ari_day import TiketAriDay





T = TypeVar("T", bound="TiketListingPricingResponse")



@_attrs_define
class TiketListingPricingResponse:
    """ Returned by `GET /v1/channels/tiket/listings/{id}/pricing`: the listing's tiket.com room, every active rate plan of
    that room.

        Attributes:
            listing_id (str):
            property_id (str): tiket.com Hotel ID.
            room_type_code (str): The tiket.com room type the listing is mapped to.
            start (datetime.date):
            end (datetime.date): Inclusive.
            days (list[TiketAriDay]):
            price_model (None | str | Unset): `Room Based` (one `price` per night) or `Occupancy Based` (`occupancyPrices`
                per number of guests). Set per property in the tiket.com extranet. Example: Room Based.
            currency (None | str | Unset):  Example: IDR.
     """

    listing_id: str
    property_id: str
    room_type_code: str
    start: datetime.date
    end: datetime.date
    days: list[TiketAriDay]
    price_model: None | str | Unset = UNSET
    currency: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.tiket_ari_day import TiketAriDay
        listing_id = self.listing_id

        property_id = self.property_id

        room_type_code = self.room_type_code

        start = self.start.isoformat()

        end = self.end.isoformat()

        days = []
        for days_item_data in self.days:
            days_item = days_item_data.to_dict()
            days.append(days_item)



        price_model: None | str | Unset
        if isinstance(self.price_model, Unset):
            price_model = UNSET
        else:
            price_model = self.price_model

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "listingId": listing_id,
            "propertyId": property_id,
            "roomTypeCode": room_type_code,
            "start": start,
            "end": end,
            "days": days,
        })
        if price_model is not UNSET:
            field_dict["priceModel"] = price_model
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tiket_ari_day import TiketAriDay
        d = dict(src_dict)
        listing_id = d.pop("listingId")

        property_id = d.pop("propertyId")

        room_type_code = d.pop("roomTypeCode")

        start = isoparse(d.pop("start")).date()




        end = isoparse(d.pop("end")).date()




        days = []
        _days = d.pop("days")
        for days_item_data in (_days):
            days_item = TiketAriDay.from_dict(days_item_data)



            days.append(days_item)


        def _parse_price_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        price_model = _parse_price_model(d.pop("priceModel", UNSET))


        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))


        tiket_listing_pricing_response = cls(
            listing_id=listing_id,
            property_id=property_id,
            room_type_code=room_type_code,
            start=start,
            end=end,
            days=days,
            price_model=price_model,
            currency=currency,
        )


        tiket_listing_pricing_response.additional_properties = d
        return tiket_listing_pricing_response

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
