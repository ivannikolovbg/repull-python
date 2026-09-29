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
  from ..models.create_conversation_special_offer_body_fees_item import CreateConversationSpecialOfferBodyFeesItem
  from ..models.create_conversation_special_offer_body_guests import CreateConversationSpecialOfferBodyGuests





T = TypeVar("T", bound="CreateConversationSpecialOfferBody")



@_attrs_define
class CreateConversationSpecialOfferBody:
    """ Priced by `totalPrice` (Airbnb) OR by its parts — `rentalAmount`, `fees`, `damageDeposit` (VRBO) — never both. With
    `totalPrice`, `checkIn`, `checkOut` and `guests` are required.

        Attributes:
            listing_id (int | Unset): Repull listing id to offer. Defaults to the listing the conversation is about.
                Example: 23892.
            check_in (datetime.date | Unset):  Example: 2026-10-01.
            check_out (datetime.date | Unset): Must be after `checkIn`. Example: 2026-10-05.
            guests (CreateConversationSpecialOfferBodyGuests | Unset):
            total_price (float | Unset): Airbnb: the total the guest pays for the whole stay, in the listing’s Airbnb
                currency. Example: 880.
            rental_amount (float | Unset): VRBO: rent for the whole stay, excluding fees and taxes. Example: 4636.
            fees (list[CreateConversationSpecialOfferBodyFeesItem] | Unset): VRBO: the offer’s fees — replaces its fee list.
                `type` is VRBO’s fee type (`CLEANING`, `PET`, …).
            damage_deposit (float | None | Unset): VRBO: refundable damage deposit; `null` for none. Example: 500.
            message (str | Unset): VRBO: the message sent to the guest with the offer (a friendly default otherwise).
     """

    listing_id: int | Unset = UNSET
    check_in: datetime.date | Unset = UNSET
    check_out: datetime.date | Unset = UNSET
    guests: CreateConversationSpecialOfferBodyGuests | Unset = UNSET
    total_price: float | Unset = UNSET
    rental_amount: float | Unset = UNSET
    fees: list[CreateConversationSpecialOfferBodyFeesItem] | Unset = UNSET
    damage_deposit: float | None | Unset = UNSET
    message: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.create_conversation_special_offer_body_fees_item import CreateConversationSpecialOfferBodyFeesItem
        from ..models.create_conversation_special_offer_body_guests import CreateConversationSpecialOfferBodyGuests
        listing_id = self.listing_id

        check_in: str | Unset = UNSET
        if not isinstance(self.check_in, Unset):
            check_in = self.check_in.isoformat()

        check_out: str | Unset = UNSET
        if not isinstance(self.check_out, Unset):
            check_out = self.check_out.isoformat()

        guests: dict[str, Any] | Unset = UNSET
        if not isinstance(self.guests, Unset):
            guests = self.guests.to_dict()

        total_price = self.total_price

        rental_amount = self.rental_amount

        fees: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.fees, Unset):
            fees = []
            for fees_item_data in self.fees:
                fees_item = fees_item_data.to_dict()
                fees.append(fees_item)



        damage_deposit: float | None | Unset
        if isinstance(self.damage_deposit, Unset):
            damage_deposit = UNSET
        else:
            damage_deposit = self.damage_deposit

        message = self.message


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if check_in is not UNSET:
            field_dict["checkIn"] = check_in
        if check_out is not UNSET:
            field_dict["checkOut"] = check_out
        if guests is not UNSET:
            field_dict["guests"] = guests
        if total_price is not UNSET:
            field_dict["totalPrice"] = total_price
        if rental_amount is not UNSET:
            field_dict["rentalAmount"] = rental_amount
        if fees is not UNSET:
            field_dict["fees"] = fees
        if damage_deposit is not UNSET:
            field_dict["damageDeposit"] = damage_deposit
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_conversation_special_offer_body_fees_item import CreateConversationSpecialOfferBodyFeesItem
        from ..models.create_conversation_special_offer_body_guests import CreateConversationSpecialOfferBodyGuests
        d = dict(src_dict)
        listing_id = d.pop("listingId", UNSET)

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




        _guests = d.pop("guests", UNSET)
        guests: CreateConversationSpecialOfferBodyGuests | Unset
        if isinstance(_guests,  Unset):
            guests = UNSET
        else:
            guests = CreateConversationSpecialOfferBodyGuests.from_dict(_guests)




        total_price = d.pop("totalPrice", UNSET)

        rental_amount = d.pop("rentalAmount", UNSET)

        _fees = d.pop("fees", UNSET)
        fees: list[CreateConversationSpecialOfferBodyFeesItem] | Unset = UNSET
        if _fees is not UNSET:
            fees = []
            for fees_item_data in _fees:
                fees_item = CreateConversationSpecialOfferBodyFeesItem.from_dict(fees_item_data)



                fees.append(fees_item)


        def _parse_damage_deposit(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        damage_deposit = _parse_damage_deposit(d.pop("damageDeposit", UNSET))


        message = d.pop("message", UNSET)

        create_conversation_special_offer_body = cls(
            listing_id=listing_id,
            check_in=check_in,
            check_out=check_out,
            guests=guests,
            total_price=total_price,
            rental_amount=rental_amount,
            fees=fees,
            damage_deposit=damage_deposit,
            message=message,
        )

        return create_conversation_special_offer_body

