from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.inquiry_webhook_object_status import InquiryWebhookObjectStatus
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.inquiry_webhook_object_expected_payout import InquiryWebhookObjectExpectedPayout
  from ..models.inquiry_webhook_object_guests import InquiryWebhookObjectGuests





T = TypeVar("T", bound="InquiryWebhookObject")



@_attrs_define
class InquiryWebhookObject:
    """ An inquiry — a guest asking about dates before booking — exactly as `GET /v1/inquiries` returns it. Delivered as
    `data.object` on `inquiry.*` events.

        Attributes:
            id (str): Repull inquiry id. Example: 25173.
            status (InquiryWebhookObjectStatus): Same vocabulary as `GET /v1/inquiries`: `open` needs an answer; `booked`
                means the guest booked (`reservationId`). Example: open.
            conversation_id (None | str | Unset): Pass to `POST /v1/conversations/{id}/pre-approval` or `/special-offers`.
                Example: 164743.
            listing_id (None | str | Unset):  Example: 23892.
            channel (str | Unset):  Example: airbnb.
            check_in (datetime.date | None | Unset):  Example: 2026-10-23.
            check_out (datetime.date | None | Unset):  Example: 2026-11-11.
            guests (InquiryWebhookObjectGuests | Unset):
            expected_payout (InquiryWebhookObjectExpectedPayout | Unset):
            reservation_id (None | str | Unset): The reservation the inquiry became, once booked.
            relayed_by (None | str | Unset): A PMS that relays this inquiry; when set, answer it in that PMS.
            respond_by (datetime.datetime | None | Unset):
            responded_at (datetime.datetime | None | Unset):
            created_at (datetime.datetime | None | Unset):
            updated_at (datetime.datetime | None | Unset):
     """

    id: str
    status: InquiryWebhookObjectStatus
    conversation_id: None | str | Unset = UNSET
    listing_id: None | str | Unset = UNSET
    channel: str | Unset = UNSET
    check_in: datetime.date | None | Unset = UNSET
    check_out: datetime.date | None | Unset = UNSET
    guests: InquiryWebhookObjectGuests | Unset = UNSET
    expected_payout: InquiryWebhookObjectExpectedPayout | Unset = UNSET
    reservation_id: None | str | Unset = UNSET
    relayed_by: None | str | Unset = UNSET
    respond_by: datetime.datetime | None | Unset = UNSET
    responded_at: datetime.datetime | None | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.inquiry_webhook_object_expected_payout import InquiryWebhookObjectExpectedPayout
        from ..models.inquiry_webhook_object_guests import InquiryWebhookObjectGuests
        id = self.id

        status = self.status.value

        conversation_id: None | str | Unset
        if isinstance(self.conversation_id, Unset):
            conversation_id = UNSET
        else:
            conversation_id = self.conversation_id

        listing_id: None | str | Unset
        if isinstance(self.listing_id, Unset):
            listing_id = UNSET
        else:
            listing_id = self.listing_id

        channel = self.channel

        check_in: None | str | Unset
        if isinstance(self.check_in, Unset):
            check_in = UNSET
        elif isinstance(self.check_in, datetime.date):
            check_in = self.check_in.isoformat()
        else:
            check_in = self.check_in

        check_out: None | str | Unset
        if isinstance(self.check_out, Unset):
            check_out = UNSET
        elif isinstance(self.check_out, datetime.date):
            check_out = self.check_out.isoformat()
        else:
            check_out = self.check_out

        guests: dict[str, Any] | Unset = UNSET
        if not isinstance(self.guests, Unset):
            guests = self.guests.to_dict()

        expected_payout: dict[str, Any] | Unset = UNSET
        if not isinstance(self.expected_payout, Unset):
            expected_payout = self.expected_payout.to_dict()

        reservation_id: None | str | Unset
        if isinstance(self.reservation_id, Unset):
            reservation_id = UNSET
        else:
            reservation_id = self.reservation_id

        relayed_by: None | str | Unset
        if isinstance(self.relayed_by, Unset):
            relayed_by = UNSET
        else:
            relayed_by = self.relayed_by

        respond_by: None | str | Unset
        if isinstance(self.respond_by, Unset):
            respond_by = UNSET
        elif isinstance(self.respond_by, datetime.datetime):
            respond_by = self.respond_by.isoformat()
        else:
            respond_by = self.respond_by

        responded_at: None | str | Unset
        if isinstance(self.responded_at, Unset):
            responded_at = UNSET
        elif isinstance(self.responded_at, datetime.datetime):
            responded_at = self.responded_at.isoformat()
        else:
            responded_at = self.responded_at

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "status": status,
        })
        if conversation_id is not UNSET:
            field_dict["conversationId"] = conversation_id
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if channel is not UNSET:
            field_dict["channel"] = channel
        if check_in is not UNSET:
            field_dict["checkIn"] = check_in
        if check_out is not UNSET:
            field_dict["checkOut"] = check_out
        if guests is not UNSET:
            field_dict["guests"] = guests
        if expected_payout is not UNSET:
            field_dict["expectedPayout"] = expected_payout
        if reservation_id is not UNSET:
            field_dict["reservationId"] = reservation_id
        if relayed_by is not UNSET:
            field_dict["relayedBy"] = relayed_by
        if respond_by is not UNSET:
            field_dict["respondBy"] = respond_by
        if responded_at is not UNSET:
            field_dict["respondedAt"] = responded_at
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.inquiry_webhook_object_expected_payout import InquiryWebhookObjectExpectedPayout
        from ..models.inquiry_webhook_object_guests import InquiryWebhookObjectGuests
        d = dict(src_dict)
        id = d.pop("id")

        status = InquiryWebhookObjectStatus(d.pop("status"))




        def _parse_conversation_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        conversation_id = _parse_conversation_id(d.pop("conversationId", UNSET))


        def _parse_listing_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        listing_id = _parse_listing_id(d.pop("listingId", UNSET))


        channel = d.pop("channel", UNSET)

        def _parse_check_in(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                check_in_type_0 = isoparse(data).date()



                return check_in_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        check_in = _parse_check_in(d.pop("checkIn", UNSET))


        def _parse_check_out(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                check_out_type_0 = isoparse(data).date()



                return check_out_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        check_out = _parse_check_out(d.pop("checkOut", UNSET))


        _guests = d.pop("guests", UNSET)
        guests: InquiryWebhookObjectGuests | Unset
        if isinstance(_guests,  Unset):
            guests = UNSET
        else:
            guests = InquiryWebhookObjectGuests.from_dict(_guests)




        _expected_payout = d.pop("expectedPayout", UNSET)
        expected_payout: InquiryWebhookObjectExpectedPayout | Unset
        if isinstance(_expected_payout,  Unset):
            expected_payout = UNSET
        else:
            expected_payout = InquiryWebhookObjectExpectedPayout.from_dict(_expected_payout)




        def _parse_reservation_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reservation_id = _parse_reservation_id(d.pop("reservationId", UNSET))


        def _parse_relayed_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        relayed_by = _parse_relayed_by(d.pop("relayedBy", UNSET))


        def _parse_respond_by(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                respond_by_type_0 = isoparse(data)



                return respond_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        respond_by = _parse_respond_by(d.pop("respondBy", UNSET))


        def _parse_responded_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                responded_at_type_0 = isoparse(data)



                return responded_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        responded_at = _parse_responded_at(d.pop("respondedAt", UNSET))


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


        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = isoparse(data)



                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updatedAt", UNSET))


        inquiry_webhook_object = cls(
            id=id,
            status=status,
            conversation_id=conversation_id,
            listing_id=listing_id,
            channel=channel,
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


        inquiry_webhook_object.additional_properties = d
        return inquiry_webhook_object

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
