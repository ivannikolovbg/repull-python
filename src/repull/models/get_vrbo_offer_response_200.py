from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_vrbo_offer_response_200_fees_item import GetVrboOfferResponse200FeesItem
  from ..models.get_vrbo_offer_response_200_guests_type_0 import GetVrboOfferResponse200GuestsType0
  from ..models.get_vrbo_offer_response_200_lines_item import GetVrboOfferResponse200LinesItem





T = TypeVar("T", bound="GetVrboOfferResponse200")



@_attrs_define
class GetVrboOfferResponse200:
    """ 
        Attributes:
            id (str | Unset): Vrbo keeps one live quote per conversation: always `current`. Example: current.
            conversation_id (str | Unset):
            channel (str | Unset):  Example: vrbo.
            status (str | Unset):  Example: sent.
            check_in (None | str | Unset):
            check_out (None | str | Unset):
            nights (int | None | Unset):
            guests (GetVrboOfferResponse200GuestsType0 | None | Unset):
            total_price (float | None | Unset): Vrbo's guest total (with its taxes and service fee).
            currency (None | str | Unset):
            rental_amount (float | None | Unset):
            fees (list[GetVrboOfferResponse200FeesItem] | Unset):
            damage_deposit (float | None | Unset):
            lines (list[GetVrboOfferResponse200LinesItem] | Unset):
            message (None | str | Unset):
     """

    id: str | Unset = UNSET
    conversation_id: str | Unset = UNSET
    channel: str | Unset = UNSET
    status: str | Unset = UNSET
    check_in: None | str | Unset = UNSET
    check_out: None | str | Unset = UNSET
    nights: int | None | Unset = UNSET
    guests: GetVrboOfferResponse200GuestsType0 | None | Unset = UNSET
    total_price: float | None | Unset = UNSET
    currency: None | str | Unset = UNSET
    rental_amount: float | None | Unset = UNSET
    fees: list[GetVrboOfferResponse200FeesItem] | Unset = UNSET
    damage_deposit: float | None | Unset = UNSET
    lines: list[GetVrboOfferResponse200LinesItem] | Unset = UNSET
    message: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_vrbo_offer_response_200_fees_item import GetVrboOfferResponse200FeesItem
        from ..models.get_vrbo_offer_response_200_guests_type_0 import GetVrboOfferResponse200GuestsType0
        from ..models.get_vrbo_offer_response_200_lines_item import GetVrboOfferResponse200LinesItem
        id = self.id

        conversation_id = self.conversation_id

        channel = self.channel

        status = self.status

        check_in: None | str | Unset
        if isinstance(self.check_in, Unset):
            check_in = UNSET
        else:
            check_in = self.check_in

        check_out: None | str | Unset
        if isinstance(self.check_out, Unset):
            check_out = UNSET
        else:
            check_out = self.check_out

        nights: int | None | Unset
        if isinstance(self.nights, Unset):
            nights = UNSET
        else:
            nights = self.nights

        guests: dict[str, Any] | None | Unset
        if isinstance(self.guests, Unset):
            guests = UNSET
        elif isinstance(self.guests, GetVrboOfferResponse200GuestsType0):
            guests = self.guests.to_dict()
        else:
            guests = self.guests

        total_price: float | None | Unset
        if isinstance(self.total_price, Unset):
            total_price = UNSET
        else:
            total_price = self.total_price

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        rental_amount: float | None | Unset
        if isinstance(self.rental_amount, Unset):
            rental_amount = UNSET
        else:
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

        lines: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.lines, Unset):
            lines = []
            for lines_item_data in self.lines:
                lines_item = lines_item_data.to_dict()
                lines.append(lines_item)



        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if conversation_id is not UNSET:
            field_dict["conversationId"] = conversation_id
        if channel is not UNSET:
            field_dict["channel"] = channel
        if status is not UNSET:
            field_dict["status"] = status
        if check_in is not UNSET:
            field_dict["checkIn"] = check_in
        if check_out is not UNSET:
            field_dict["checkOut"] = check_out
        if nights is not UNSET:
            field_dict["nights"] = nights
        if guests is not UNSET:
            field_dict["guests"] = guests
        if total_price is not UNSET:
            field_dict["totalPrice"] = total_price
        if currency is not UNSET:
            field_dict["currency"] = currency
        if rental_amount is not UNSET:
            field_dict["rentalAmount"] = rental_amount
        if fees is not UNSET:
            field_dict["fees"] = fees
        if damage_deposit is not UNSET:
            field_dict["damageDeposit"] = damage_deposit
        if lines is not UNSET:
            field_dict["lines"] = lines
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_vrbo_offer_response_200_fees_item import GetVrboOfferResponse200FeesItem
        from ..models.get_vrbo_offer_response_200_guests_type_0 import GetVrboOfferResponse200GuestsType0
        from ..models.get_vrbo_offer_response_200_lines_item import GetVrboOfferResponse200LinesItem
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        conversation_id = d.pop("conversationId", UNSET)

        channel = d.pop("channel", UNSET)

        status = d.pop("status", UNSET)

        def _parse_check_in(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        check_in = _parse_check_in(d.pop("checkIn", UNSET))


        def _parse_check_out(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        check_out = _parse_check_out(d.pop("checkOut", UNSET))


        def _parse_nights(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        nights = _parse_nights(d.pop("nights", UNSET))


        def _parse_guests(data: object) -> GetVrboOfferResponse200GuestsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                guests_type_0 = GetVrboOfferResponse200GuestsType0.from_dict(data)



                return guests_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetVrboOfferResponse200GuestsType0 | None | Unset, data)

        guests = _parse_guests(d.pop("guests", UNSET))


        def _parse_total_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        total_price = _parse_total_price(d.pop("totalPrice", UNSET))


        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))


        def _parse_rental_amount(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        rental_amount = _parse_rental_amount(d.pop("rentalAmount", UNSET))


        _fees = d.pop("fees", UNSET)
        fees: list[GetVrboOfferResponse200FeesItem] | Unset = UNSET
        if _fees is not UNSET:
            fees = []
            for fees_item_data in _fees:
                fees_item = GetVrboOfferResponse200FeesItem.from_dict(fees_item_data)



                fees.append(fees_item)


        def _parse_damage_deposit(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        damage_deposit = _parse_damage_deposit(d.pop("damageDeposit", UNSET))


        _lines = d.pop("lines", UNSET)
        lines: list[GetVrboOfferResponse200LinesItem] | Unset = UNSET
        if _lines is not UNSET:
            lines = []
            for lines_item_data in _lines:
                lines_item = GetVrboOfferResponse200LinesItem.from_dict(lines_item_data)



                lines.append(lines_item)


        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))


        get_vrbo_offer_response_200 = cls(
            id=id,
            conversation_id=conversation_id,
            channel=channel,
            status=status,
            check_in=check_in,
            check_out=check_out,
            nights=nights,
            guests=guests,
            total_price=total_price,
            currency=currency,
            rental_amount=rental_amount,
            fees=fees,
            damage_deposit=damage_deposit,
            lines=lines,
            message=message,
        )


        get_vrbo_offer_response_200.additional_properties = d
        return get_vrbo_offer_response_200

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
