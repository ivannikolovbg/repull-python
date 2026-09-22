from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_airbnb_offer_body_type import CreateAirbnbOfferBodyType
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.create_airbnb_offer_body_guest_details import CreateAirbnbOfferBodyGuestDetails





T = TypeVar("T", bound="CreateAirbnbOfferBody")



@_attrs_define
class CreateAirbnbOfferBody:
    """ 
        Attributes:
            type_ (CreateAirbnbOfferBodyType): What to create.
            thread_id (str): Airbnb message-thread id the offer answers. (`threadId` is accepted too.) Example: 2675957479.
            block_instant_booking (bool | Unset): Pre-approval only: require the guest to book through the pre-approval
                rather than Instant Book. (`blockInstantBooking` is accepted too.) Default: False.
            listing_id (str | Unset): Offer only (required): the AIRBNB listing id, as a string. Example:
                955656266214757921.
            start_date (datetime.date | Unset): Offer only (required): first night. Example: 2026-10-01.
            nights (int | Unset): Offer only (required). Example: 4.
            total_price (float | Unset): Offer only (required): total for the stay, in the listing’s Airbnb currency.
                Example: 880.
            guest_details (CreateAirbnbOfferBodyGuestDetails | Unset): Offer only (required). `number_of_guests` is adults +
                children; if omitted it is computed from them.
     """

    type_: CreateAirbnbOfferBodyType
    thread_id: str
    block_instant_booking: bool | Unset = False
    listing_id: str | Unset = UNSET
    start_date: datetime.date | Unset = UNSET
    nights: int | Unset = UNSET
    total_price: float | Unset = UNSET
    guest_details: CreateAirbnbOfferBodyGuestDetails | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.create_airbnb_offer_body_guest_details import CreateAirbnbOfferBodyGuestDetails
        type_ = self.type_.value

        thread_id = self.thread_id

        block_instant_booking = self.block_instant_booking

        listing_id = self.listing_id

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        nights = self.nights

        total_price = self.total_price

        guest_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.guest_details, Unset):
            guest_details = self.guest_details.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "type": type_,
            "thread_id": thread_id,
        })
        if block_instant_booking is not UNSET:
            field_dict["block_instant_booking"] = block_instant_booking
        if listing_id is not UNSET:
            field_dict["listing_id"] = listing_id
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if nights is not UNSET:
            field_dict["nights"] = nights
        if total_price is not UNSET:
            field_dict["total_price"] = total_price
        if guest_details is not UNSET:
            field_dict["guest_details"] = guest_details

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_airbnb_offer_body_guest_details import CreateAirbnbOfferBodyGuestDetails
        d = dict(src_dict)
        type_ = CreateAirbnbOfferBodyType(d.pop("type"))




        thread_id = d.pop("thread_id")

        block_instant_booking = d.pop("block_instant_booking", UNSET)

        listing_id = d.pop("listing_id", UNSET)

        _start_date = d.pop("start_date", UNSET)
        start_date: datetime.date | Unset
        if isinstance(_start_date,  Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date).date()




        nights = d.pop("nights", UNSET)

        total_price = d.pop("total_price", UNSET)

        _guest_details = d.pop("guest_details", UNSET)
        guest_details: CreateAirbnbOfferBodyGuestDetails | Unset
        if isinstance(_guest_details,  Unset):
            guest_details = UNSET
        else:
            guest_details = CreateAirbnbOfferBodyGuestDetails.from_dict(_guest_details)




        create_airbnb_offer_body = cls(
            type_=type_,
            thread_id=thread_id,
            block_instant_booking=block_instant_booking,
            listing_id=listing_id,
            start_date=start_date,
            nights=nights,
            total_price=total_price,
            guest_details=guest_details,
        )

        return create_airbnb_offer_body

