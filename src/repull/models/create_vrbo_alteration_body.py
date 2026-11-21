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






T = TypeVar("T", bound="CreateVrboAlterationBody")



@_attrs_define
class CreateVrboAlterationBody:
    """ 
        Attributes:
            confirmation_code (str):  Example: HA-C3WBX1.
            check_in (datetime.date | Unset):
            check_out (datetime.date | Unset):
            check_in_time (str | Unset):  Example: 16:00.
            check_out_time (str | Unset):  Example: 11:00.
            number_of_adults (int | Unset):
            number_of_children (int | Unset):
            pets (bool | Unset):
            rent_amount (float | Unset): The new rent for the stay, in the booking's currency; Vrbo adds its fees and taxes.
            keep_original_price (bool | Unset): Change the stay without changing what the guest pays.
            payment_due_date (datetime.date | Unset): When the guest must pay any difference (Vrbo's default otherwise).
            preview (bool | Unset): Vrbo's dry run only: nothing is changed.
     """

    confirmation_code: str
    check_in: datetime.date | Unset = UNSET
    check_out: datetime.date | Unset = UNSET
    check_in_time: str | Unset = UNSET
    check_out_time: str | Unset = UNSET
    number_of_adults: int | Unset = UNSET
    number_of_children: int | Unset = UNSET
    pets: bool | Unset = UNSET
    rent_amount: float | Unset = UNSET
    keep_original_price: bool | Unset = UNSET
    payment_due_date: datetime.date | Unset = UNSET
    preview: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        confirmation_code = self.confirmation_code

        check_in: str | Unset = UNSET
        if not isinstance(self.check_in, Unset):
            check_in = self.check_in.isoformat()

        check_out: str | Unset = UNSET
        if not isinstance(self.check_out, Unset):
            check_out = self.check_out.isoformat()

        check_in_time = self.check_in_time

        check_out_time = self.check_out_time

        number_of_adults = self.number_of_adults

        number_of_children = self.number_of_children

        pets = self.pets

        rent_amount = self.rent_amount

        keep_original_price = self.keep_original_price

        payment_due_date: str | Unset = UNSET
        if not isinstance(self.payment_due_date, Unset):
            payment_due_date = self.payment_due_date.isoformat()

        preview = self.preview


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "confirmation_code": confirmation_code,
        })
        if check_in is not UNSET:
            field_dict["check_in"] = check_in
        if check_out is not UNSET:
            field_dict["check_out"] = check_out
        if check_in_time is not UNSET:
            field_dict["check_in_time"] = check_in_time
        if check_out_time is not UNSET:
            field_dict["check_out_time"] = check_out_time
        if number_of_adults is not UNSET:
            field_dict["number_of_adults"] = number_of_adults
        if number_of_children is not UNSET:
            field_dict["number_of_children"] = number_of_children
        if pets is not UNSET:
            field_dict["pets"] = pets
        if rent_amount is not UNSET:
            field_dict["rent_amount"] = rent_amount
        if keep_original_price is not UNSET:
            field_dict["keep_original_price"] = keep_original_price
        if payment_due_date is not UNSET:
            field_dict["payment_due_date"] = payment_due_date
        if preview is not UNSET:
            field_dict["preview"] = preview

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        confirmation_code = d.pop("confirmation_code")

        _check_in = d.pop("check_in", UNSET)
        check_in: datetime.date | Unset
        if isinstance(_check_in,  Unset):
            check_in = UNSET
        else:
            check_in = isoparse(_check_in).date()




        _check_out = d.pop("check_out", UNSET)
        check_out: datetime.date | Unset
        if isinstance(_check_out,  Unset):
            check_out = UNSET
        else:
            check_out = isoparse(_check_out).date()




        check_in_time = d.pop("check_in_time", UNSET)

        check_out_time = d.pop("check_out_time", UNSET)

        number_of_adults = d.pop("number_of_adults", UNSET)

        number_of_children = d.pop("number_of_children", UNSET)

        pets = d.pop("pets", UNSET)

        rent_amount = d.pop("rent_amount", UNSET)

        keep_original_price = d.pop("keep_original_price", UNSET)

        _payment_due_date = d.pop("payment_due_date", UNSET)
        payment_due_date: datetime.date | Unset
        if isinstance(_payment_due_date,  Unset):
            payment_due_date = UNSET
        else:
            payment_due_date = isoparse(_payment_due_date).date()




        preview = d.pop("preview", UNSET)

        create_vrbo_alteration_body = cls(
            confirmation_code=confirmation_code,
            check_in=check_in,
            check_out=check_out,
            check_in_time=check_in_time,
            check_out_time=check_out_time,
            number_of_adults=number_of_adults,
            number_of_children=number_of_children,
            pets=pets,
            rent_amount=rent_amount,
            keep_original_price=keep_original_price,
            payment_due_date=payment_due_date,
            preview=preview,
        )

        return create_vrbo_alteration_body

