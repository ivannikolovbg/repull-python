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
  from ..models.create_conversation_special_offer_body_guests import CreateConversationSpecialOfferBodyGuests





T = TypeVar("T", bound="CreateConversationSpecialOfferBody")



@_attrs_define
class CreateConversationSpecialOfferBody:
    """ 
        Attributes:
            check_in (datetime.date):  Example: 2026-10-01.
            check_out (datetime.date): Must be after `checkIn`. Example: 2026-10-05.
            guests (CreateConversationSpecialOfferBodyGuests):
            total_price (float): Total the guest pays for the whole stay, in the listing’s Airbnb currency. Example: 880.
            listing_id (int | Unset): Repull listing id to offer. Defaults to the listing the conversation is about.
                Example: 23892.
     """

    check_in: datetime.date
    check_out: datetime.date
    guests: CreateConversationSpecialOfferBodyGuests
    total_price: float
    listing_id: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.create_conversation_special_offer_body_guests import CreateConversationSpecialOfferBodyGuests
        check_in = self.check_in.isoformat()

        check_out = self.check_out.isoformat()

        guests = self.guests.to_dict()

        total_price = self.total_price

        listing_id = self.listing_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "checkIn": check_in,
            "checkOut": check_out,
            "guests": guests,
            "totalPrice": total_price,
        })
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_conversation_special_offer_body_guests import CreateConversationSpecialOfferBodyGuests
        d = dict(src_dict)
        check_in = isoparse(d.pop("checkIn")).date()




        check_out = isoparse(d.pop("checkOut")).date()




        guests = CreateConversationSpecialOfferBodyGuests.from_dict(d.pop("guests"))




        total_price = d.pop("totalPrice")

        listing_id = d.pop("listingId", UNSET)

        create_conversation_special_offer_body = cls(
            check_in=check_in,
            check_out=check_out,
            guests=guests,
            total_price=total_price,
            listing_id=listing_id,
        )

        return create_conversation_special_offer_body

