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
  from ..models.get_conversation_special_offer_response_200_guests_type_0 import GetConversationSpecialOfferResponse200GuestsType0





T = TypeVar("T", bound="GetConversationSpecialOfferResponse200")



@_attrs_define
class GetConversationSpecialOfferResponse200:
    """ 
        Attributes:
            id (None | str): Airbnb special-offer id. Use it to read or withdraw the offer. Example: 1459920384.
            conversation_id (str): Repull conversation id the offer was sent on. Example: 164743.
            status (None | str): Airbnb’s status for the offer: `active` (the guest can book it), `accepted`, `declined`,
                `expired` or `voided` (withdrawn). Example: active.
            check_in (datetime.date | None):  Example: 2026-10-01.
            check_out (datetime.date | None):  Example: 2026-10-05.
            nights (int | None):  Example: 4.
            total_price (float | None): Total for the stay, in the listing’s Airbnb currency. Example: 880.
            listing_id (None | str | Unset): Repull listing id, when known. Example: 23892.
            airbnb_listing_id (None | str | Unset): Airbnb listing id the offer is for (a string — it exceeds 2^53).
                Example: 955656266214757921.
            guests (GetConversationSpecialOfferResponse200GuestsType0 | None | Unset): Guests on the offer. Airbnb counts
                adults + children as guests; infants and pets are extra.
            created_at (datetime.datetime | None | Unset):
            expires_at (datetime.datetime | None | Unset): When the guest can no longer book the offer (Airbnb gives them 24
                hours).
     """

    id: None | str
    conversation_id: str
    status: None | str
    check_in: datetime.date | None
    check_out: datetime.date | None
    nights: int | None
    total_price: float | None
    listing_id: None | str | Unset = UNSET
    airbnb_listing_id: None | str | Unset = UNSET
    guests: GetConversationSpecialOfferResponse200GuestsType0 | None | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    expires_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_conversation_special_offer_response_200_guests_type_0 import GetConversationSpecialOfferResponse200GuestsType0
        id: None | str
        id = self.id

        conversation_id = self.conversation_id

        status: None | str
        status = self.status

        check_in: None | str
        if isinstance(self.check_in, datetime.date):
            check_in = self.check_in.isoformat()
        else:
            check_in = self.check_in

        check_out: None | str
        if isinstance(self.check_out, datetime.date):
            check_out = self.check_out.isoformat()
        else:
            check_out = self.check_out

        nights: int | None
        nights = self.nights

        total_price: float | None
        total_price = self.total_price

        listing_id: None | str | Unset
        if isinstance(self.listing_id, Unset):
            listing_id = UNSET
        else:
            listing_id = self.listing_id

        airbnb_listing_id: None | str | Unset
        if isinstance(self.airbnb_listing_id, Unset):
            airbnb_listing_id = UNSET
        else:
            airbnb_listing_id = self.airbnb_listing_id

        guests: dict[str, Any] | None | Unset
        if isinstance(self.guests, Unset):
            guests = UNSET
        elif isinstance(self.guests, GetConversationSpecialOfferResponse200GuestsType0):
            guests = self.guests.to_dict()
        else:
            guests = self.guests

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "conversationId": conversation_id,
            "status": status,
            "checkIn": check_in,
            "checkOut": check_out,
            "nights": nights,
            "totalPrice": total_price,
        })
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if airbnb_listing_id is not UNSET:
            field_dict["airbnbListingId"] = airbnb_listing_id
        if guests is not UNSET:
            field_dict["guests"] = guests
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_conversation_special_offer_response_200_guests_type_0 import GetConversationSpecialOfferResponse200GuestsType0
        d = dict(src_dict)
        def _parse_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        id = _parse_id(d.pop("id"))


        conversation_id = d.pop("conversationId")

        def _parse_status(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        status = _parse_status(d.pop("status"))


        def _parse_check_in(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                check_in_type_0 = isoparse(data).date()



                return check_in_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        check_in = _parse_check_in(d.pop("checkIn"))


        def _parse_check_out(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                check_out_type_0 = isoparse(data).date()



                return check_out_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        check_out = _parse_check_out(d.pop("checkOut"))


        def _parse_nights(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        nights = _parse_nights(d.pop("nights"))


        def _parse_total_price(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        total_price = _parse_total_price(d.pop("totalPrice"))


        def _parse_listing_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        listing_id = _parse_listing_id(d.pop("listingId", UNSET))


        def _parse_airbnb_listing_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        airbnb_listing_id = _parse_airbnb_listing_id(d.pop("airbnbListingId", UNSET))


        def _parse_guests(data: object) -> GetConversationSpecialOfferResponse200GuestsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                guests_type_0 = GetConversationSpecialOfferResponse200GuestsType0.from_dict(data)



                return guests_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetConversationSpecialOfferResponse200GuestsType0 | None | Unset, data)

        guests = _parse_guests(d.pop("guests", UNSET))


        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = isoparse(data)



                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("createdAt", UNSET))


        def _parse_expires_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = isoparse(data)



                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expires_at = _parse_expires_at(d.pop("expiresAt", UNSET))


        get_conversation_special_offer_response_200 = cls(
            id=id,
            conversation_id=conversation_id,
            status=status,
            check_in=check_in,
            check_out=check_out,
            nights=nights,
            total_price=total_price,
            listing_id=listing_id,
            airbnb_listing_id=airbnb_listing_id,
            guests=guests,
            created_at=created_at,
            expires_at=expires_at,
        )


        get_conversation_special_offer_response_200.additional_properties = d
        return get_conversation_special_offer_response_200

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
