from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.withdraw_airbnb_offer_response_200_offer_type import WithdrawAirbnbOfferResponse200OfferType
from ..models.withdraw_airbnb_offer_response_200_status import WithdrawAirbnbOfferResponse200Status
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.withdraw_airbnb_offer_response_200_guest_details import WithdrawAirbnbOfferResponse200GuestDetails





T = TypeVar("T", bound="WithdrawAirbnbOfferResponse200")



@_attrs_define
class WithdrawAirbnbOfferResponse200:
    """ Airbnb’s special-offer object as Airbnb returns it (keys camelCased). Fields vary by `offerType`; a pre-approval
    carries only the thread, status and expiry.

        Attributes:
            id (str | Unset): Airbnb special-offer id.
            thread_id (str | Unset): Airbnb thread id the offer was sent on.
            offer_type (WithdrawAirbnbOfferResponse200OfferType | Unset):
            status (WithdrawAirbnbOfferResponse200Status | Unset):
            listing_id (str | Unset): Airbnb listing id (special offers only).
            start_date (datetime.date | Unset):
            nights (int | Unset):
            total_price (float | Unset):
            guest_details (WithdrawAirbnbOfferResponse200GuestDetails | Unset):
            created_at (datetime.datetime | Unset):
            expires_at (datetime.datetime | Unset):
     """

    id: str | Unset = UNSET
    thread_id: str | Unset = UNSET
    offer_type: WithdrawAirbnbOfferResponse200OfferType | Unset = UNSET
    status: WithdrawAirbnbOfferResponse200Status | Unset = UNSET
    listing_id: str | Unset = UNSET
    start_date: datetime.date | Unset = UNSET
    nights: int | Unset = UNSET
    total_price: float | Unset = UNSET
    guest_details: WithdrawAirbnbOfferResponse200GuestDetails | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    expires_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.withdraw_airbnb_offer_response_200_guest_details import WithdrawAirbnbOfferResponse200GuestDetails
        id = self.id

        thread_id = self.thread_id

        offer_type: str | Unset = UNSET
        if not isinstance(self.offer_type, Unset):
            offer_type = self.offer_type.value


        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        listing_id = self.listing_id

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        nights = self.nights

        total_price = self.total_price

        guest_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.guest_details, Unset):
            guest_details = self.guest_details.to_dict()

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        expires_at: str | Unset = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if thread_id is not UNSET:
            field_dict["threadId"] = thread_id
        if offer_type is not UNSET:
            field_dict["offerType"] = offer_type
        if status is not UNSET:
            field_dict["status"] = status
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if nights is not UNSET:
            field_dict["nights"] = nights
        if total_price is not UNSET:
            field_dict["totalPrice"] = total_price
        if guest_details is not UNSET:
            field_dict["guestDetails"] = guest_details
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.withdraw_airbnb_offer_response_200_guest_details import WithdrawAirbnbOfferResponse200GuestDetails
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        thread_id = d.pop("threadId", UNSET)

        _offer_type = d.pop("offerType", UNSET)
        offer_type: WithdrawAirbnbOfferResponse200OfferType | Unset
        if isinstance(_offer_type,  Unset):
            offer_type = UNSET
        else:
            offer_type = WithdrawAirbnbOfferResponse200OfferType(_offer_type)




        _status = d.pop("status", UNSET)
        status: WithdrawAirbnbOfferResponse200Status | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = WithdrawAirbnbOfferResponse200Status(_status)




        listing_id = d.pop("listingId", UNSET)

        _start_date = d.pop("startDate", UNSET)
        start_date: datetime.date | Unset
        if isinstance(_start_date,  Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date).date()




        nights = d.pop("nights", UNSET)

        total_price = d.pop("totalPrice", UNSET)

        _guest_details = d.pop("guestDetails", UNSET)
        guest_details: WithdrawAirbnbOfferResponse200GuestDetails | Unset
        if isinstance(_guest_details,  Unset):
            guest_details = UNSET
        else:
            guest_details = WithdrawAirbnbOfferResponse200GuestDetails.from_dict(_guest_details)




        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        _expires_at = d.pop("expiresAt", UNSET)
        expires_at: datetime.datetime | Unset
        if isinstance(_expires_at,  Unset):
            expires_at = UNSET
        else:
            expires_at = isoparse(_expires_at)




        withdraw_airbnb_offer_response_200 = cls(
            id=id,
            thread_id=thread_id,
            offer_type=offer_type,
            status=status,
            listing_id=listing_id,
            start_date=start_date,
            nights=nights,
            total_price=total_price,
            guest_details=guest_details,
            created_at=created_at,
            expires_at=expires_at,
        )


        withdraw_airbnb_offer_response_200.additional_properties = d
        return withdraw_airbnb_offer_response_200

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
