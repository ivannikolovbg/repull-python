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
  from ..models.preview_conversation_special_offer_body_fees_item import PreviewConversationSpecialOfferBodyFeesItem
  from ..models.preview_conversation_special_offer_body_guests import PreviewConversationSpecialOfferBodyGuests





T = TypeVar("T", bound="PreviewConversationSpecialOfferBody")



@_attrs_define
class PreviewConversationSpecialOfferBody:
    """ Any of the offer fields; only what is sent is changed.

        Attributes:
            check_in (datetime.date | Unset):  Example: 2026-11-26.
            check_out (datetime.date | Unset):  Example: 2026-12-06.
            guests (PreviewConversationSpecialOfferBodyGuests | Unset):
            rental_amount (float | Unset): Rent for the stay, excluding fees and taxes.
            fees (list[PreviewConversationSpecialOfferBodyFeesItem] | Unset):
            damage_deposit (float | None | Unset):
     """

    check_in: datetime.date | Unset = UNSET
    check_out: datetime.date | Unset = UNSET
    guests: PreviewConversationSpecialOfferBodyGuests | Unset = UNSET
    rental_amount: float | Unset = UNSET
    fees: list[PreviewConversationSpecialOfferBodyFeesItem] | Unset = UNSET
    damage_deposit: float | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.preview_conversation_special_offer_body_fees_item import PreviewConversationSpecialOfferBodyFeesItem
        from ..models.preview_conversation_special_offer_body_guests import PreviewConversationSpecialOfferBodyGuests
        check_in: str | Unset = UNSET
        if not isinstance(self.check_in, Unset):
            check_in = self.check_in.isoformat()

        check_out: str | Unset = UNSET
        if not isinstance(self.check_out, Unset):
            check_out = self.check_out.isoformat()

        guests: dict[str, Any] | Unset = UNSET
        if not isinstance(self.guests, Unset):
            guests = self.guests.to_dict()

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


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if check_in is not UNSET:
            field_dict["checkIn"] = check_in
        if check_out is not UNSET:
            field_dict["checkOut"] = check_out
        if guests is not UNSET:
            field_dict["guests"] = guests
        if rental_amount is not UNSET:
            field_dict["rentalAmount"] = rental_amount
        if fees is not UNSET:
            field_dict["fees"] = fees
        if damage_deposit is not UNSET:
            field_dict["damageDeposit"] = damage_deposit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.preview_conversation_special_offer_body_fees_item import PreviewConversationSpecialOfferBodyFeesItem
        from ..models.preview_conversation_special_offer_body_guests import PreviewConversationSpecialOfferBodyGuests
        d = dict(src_dict)
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
        guests: PreviewConversationSpecialOfferBodyGuests | Unset
        if isinstance(_guests,  Unset):
            guests = UNSET
        else:
            guests = PreviewConversationSpecialOfferBodyGuests.from_dict(_guests)




        rental_amount = d.pop("rentalAmount", UNSET)

        _fees = d.pop("fees", UNSET)
        fees: list[PreviewConversationSpecialOfferBodyFeesItem] | Unset = UNSET
        if _fees is not UNSET:
            fees = []
            for fees_item_data in _fees:
                fees_item = PreviewConversationSpecialOfferBodyFeesItem.from_dict(fees_item_data)



                fees.append(fees_item)


        def _parse_damage_deposit(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        damage_deposit = _parse_damage_deposit(d.pop("damageDeposit", UNSET))


        preview_conversation_special_offer_body = cls(
            check_in=check_in,
            check_out=check_out,
            guests=guests,
            rental_amount=rental_amount,
            fees=fees,
            damage_deposit=damage_deposit,
        )

        return preview_conversation_special_offer_body

