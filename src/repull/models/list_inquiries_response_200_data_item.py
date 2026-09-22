from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.list_inquiries_response_200_data_item_status import ListInquiriesResponse200DataItemStatus
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.list_inquiries_response_200_data_item_expected_payout import ListInquiriesResponse200DataItemExpectedPayout
  from ..models.list_inquiries_response_200_data_item_guests import ListInquiriesResponse200DataItemGuests





T = TypeVar("T", bound="ListInquiriesResponse200DataItem")



@_attrs_define
class ListInquiriesResponse200DataItem:
    """ 
        Attributes:
            id (str): Repull inquiry id. Example: 25173.
            conversation_id (None | str): Repull conversation id — pass it to `POST /v1/conversations/{id}/pre-approval` or
                `/special-offers`. Example: 164743.
            listing_id (None | str):  Example: 23892.
            channel (str):  Example: airbnb.
            status (ListInquiriesResponse200DataItemStatus): `open` — nobody has answered and the stay is still ahead;
                `pre_approved`; `special_offer_sent` (from the API, Vanio, or Airbnb’s own app); `booked` — the guest booked
                (`reservationId`); `expired` — the stay has started or Airbnb expired it; `declined`; `not_possible` — Airbnb
                says the dates cannot be booked.
            check_in (datetime.date | None):  Example: 2026-09-23.
            check_out (datetime.date | None):  Example: 2026-10-11.
            guests (ListInquiriesResponse200DataItemGuests):
            expected_payout (ListInquiriesResponse200DataItemExpectedPayout): What Airbnb quoted the host for the stay the
                guest asked about.
            reservation_id (None | str): The reservation the inquiry became, once booked.
            relayed_by (None | str): A PMS (e.g. `hostaway`, `guesty`) this inquiry arrives through. When set, it cannot be
                pre-approved or offered from Repull — act on it in that PMS.
            respond_by (datetime.datetime | None): Airbnb’s response deadline for the host (it counts toward response rate).
            responded_at (datetime.datetime | None):
            created_at (datetime.datetime | None):
            updated_at (datetime.datetime | None):
     """

    id: str
    conversation_id: None | str
    listing_id: None | str
    channel: str
    status: ListInquiriesResponse200DataItemStatus
    check_in: datetime.date | None
    check_out: datetime.date | None
    guests: ListInquiriesResponse200DataItemGuests
    expected_payout: ListInquiriesResponse200DataItemExpectedPayout
    reservation_id: None | str
    relayed_by: None | str
    respond_by: datetime.datetime | None
    responded_at: datetime.datetime | None
    created_at: datetime.datetime | None
    updated_at: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.list_inquiries_response_200_data_item_expected_payout import ListInquiriesResponse200DataItemExpectedPayout
        from ..models.list_inquiries_response_200_data_item_guests import ListInquiriesResponse200DataItemGuests
        id = self.id

        conversation_id: None | str
        conversation_id = self.conversation_id

        listing_id: None | str
        listing_id = self.listing_id

        channel = self.channel

        status = self.status.value

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

        guests = self.guests.to_dict()

        expected_payout = self.expected_payout.to_dict()

        reservation_id: None | str
        reservation_id = self.reservation_id

        relayed_by: None | str
        relayed_by = self.relayed_by

        respond_by: None | str
        if isinstance(self.respond_by, datetime.datetime):
            respond_by = self.respond_by.isoformat()
        else:
            respond_by = self.respond_by

        responded_at: None | str
        if isinstance(self.responded_at, datetime.datetime):
            responded_at = self.responded_at.isoformat()
        else:
            responded_at = self.responded_at

        created_at: None | str
        if isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        updated_at: None | str
        if isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "conversationId": conversation_id,
            "listingId": listing_id,
            "channel": channel,
            "status": status,
            "checkIn": check_in,
            "checkOut": check_out,
            "guests": guests,
            "expectedPayout": expected_payout,
            "reservationId": reservation_id,
            "relayedBy": relayed_by,
            "respondBy": respond_by,
            "respondedAt": responded_at,
            "createdAt": created_at,
            "updatedAt": updated_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_inquiries_response_200_data_item_expected_payout import ListInquiriesResponse200DataItemExpectedPayout
        from ..models.list_inquiries_response_200_data_item_guests import ListInquiriesResponse200DataItemGuests
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_conversation_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        conversation_id = _parse_conversation_id(d.pop("conversationId"))


        def _parse_listing_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        listing_id = _parse_listing_id(d.pop("listingId"))


        channel = d.pop("channel")

        status = ListInquiriesResponse200DataItemStatus(d.pop("status"))




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


        guests = ListInquiriesResponse200DataItemGuests.from_dict(d.pop("guests"))




        expected_payout = ListInquiriesResponse200DataItemExpectedPayout.from_dict(d.pop("expectedPayout"))




        def _parse_reservation_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        reservation_id = _parse_reservation_id(d.pop("reservationId"))


        def _parse_relayed_by(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        relayed_by = _parse_relayed_by(d.pop("relayedBy"))


        def _parse_respond_by(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                respond_by_type_0 = isoparse(data)



                return respond_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        respond_by = _parse_respond_by(d.pop("respondBy"))


        def _parse_responded_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                responded_at_type_0 = isoparse(data)



                return responded_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        responded_at = _parse_responded_at(d.pop("respondedAt"))


        def _parse_created_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = isoparse(data)



                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        created_at = _parse_created_at(d.pop("createdAt"))


        def _parse_updated_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = isoparse(data)



                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        updated_at = _parse_updated_at(d.pop("updatedAt"))


        list_inquiries_response_200_data_item = cls(
            id=id,
            conversation_id=conversation_id,
            listing_id=listing_id,
            channel=channel,
            status=status,
            check_in=check_in,
            check_out=check_out,
            guests=guests,
            expected_payout=expected_payout,
            reservation_id=reservation_id,
            relayed_by=relayed_by,
            respond_by=respond_by,
            responded_at=responded_at,
            created_at=created_at,
            updated_at=updated_at,
        )


        list_inquiries_response_200_data_item.additional_properties = d
        return list_inquiries_response_200_data_item

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
