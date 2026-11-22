from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_vrbo_offer_body_type import CreateVrboOfferBodyType
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.create_vrbo_offer_body_fees_item import CreateVrboOfferBodyFeesItem
  from ..models.create_vrbo_offer_body_guest_details import CreateVrboOfferBodyGuestDetails





T = TypeVar("T", bound="CreateVrboOfferBody")



@_attrs_define
class CreateVrboOfferBody:
    """ 
        Attributes:
            type_ (CreateVrboOfferBodyType):
            thread_id (str): The Vrbo conversation (`vrbo:<uuid>`). `threadId` is accepted too.
            message (str | Unset): A note Vrbo shows the guest with the pre-approval or quote.
            start_date (datetime.date | Unset): Offer: first night. With `nights`.
            nights (int | Unset): Offer: number of nights. With `start_date`.
            guest_details (CreateVrboOfferBodyGuestDetails | Unset):
            rental_amount (float | Unset): Offer: the rent for the stay, before fees and taxes.
            fees (list[CreateVrboOfferBodyFeesItem] | Unset):
            damage_deposit (float | None | Unset): Offer: refundable damage deposit; `null` for none.
     """

    type_: CreateVrboOfferBodyType
    thread_id: str
    message: str | Unset = UNSET
    start_date: datetime.date | Unset = UNSET
    nights: int | Unset = UNSET
    guest_details: CreateVrboOfferBodyGuestDetails | Unset = UNSET
    rental_amount: float | Unset = UNSET
    fees: list[CreateVrboOfferBodyFeesItem] | Unset = UNSET
    damage_deposit: float | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.create_vrbo_offer_body_fees_item import CreateVrboOfferBodyFeesItem
        from ..models.create_vrbo_offer_body_guest_details import CreateVrboOfferBodyGuestDetails
        type_ = self.type_.value

        thread_id = self.thread_id

        message = self.message

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        nights = self.nights

        guest_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.guest_details, Unset):
            guest_details = self.guest_details.to_dict()

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
            "type": type_,
            "thread_id": thread_id,
        })
        if message is not UNSET:
            field_dict["message"] = message
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if nights is not UNSET:
            field_dict["nights"] = nights
        if guest_details is not UNSET:
            field_dict["guest_details"] = guest_details
        if rental_amount is not UNSET:
            field_dict["rental_amount"] = rental_amount
        if fees is not UNSET:
            field_dict["fees"] = fees
        if damage_deposit is not UNSET:
            field_dict["damage_deposit"] = damage_deposit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_vrbo_offer_body_fees_item import CreateVrboOfferBodyFeesItem
        from ..models.create_vrbo_offer_body_guest_details import CreateVrboOfferBodyGuestDetails
        d = dict(src_dict)
        type_ = CreateVrboOfferBodyType(d.pop("type"))




        thread_id = d.pop("thread_id")

        message = d.pop("message", UNSET)

        _start_date = d.pop("start_date", UNSET)
        start_date: datetime.date | Unset
        if isinstance(_start_date,  Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date).date()




        nights = d.pop("nights", UNSET)

        _guest_details = d.pop("guest_details", UNSET)
        guest_details: CreateVrboOfferBodyGuestDetails | Unset
        if isinstance(_guest_details,  Unset):
            guest_details = UNSET
        else:
            guest_details = CreateVrboOfferBodyGuestDetails.from_dict(_guest_details)




        rental_amount = d.pop("rental_amount", UNSET)

        _fees = d.pop("fees", UNSET)
        fees: list[CreateVrboOfferBodyFeesItem] | Unset = UNSET
        if _fees is not UNSET:
            fees = []
            for fees_item_data in _fees:
                fees_item = CreateVrboOfferBodyFeesItem.from_dict(fees_item_data)



                fees.append(fees_item)


        def _parse_damage_deposit(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        damage_deposit = _parse_damage_deposit(d.pop("damage_deposit", UNSET))


        create_vrbo_offer_body = cls(
            type_=type_,
            thread_id=thread_id,
            message=message,
            start_date=start_date,
            nights=nights,
            guest_details=guest_details,
            rental_amount=rental_amount,
            fees=fees,
            damage_deposit=damage_deposit,
        )

        return create_vrbo_offer_body

