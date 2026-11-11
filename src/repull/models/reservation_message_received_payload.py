from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.reservation_message_received_payload_direction import ReservationMessageReceivedPayloadDirection
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.conversation_message_attachment import ConversationMessageAttachment
  from ..models.reservation_message_received_payload_from import ReservationMessageReceivedPayloadFrom





T = TypeVar("T", bound="ReservationMessageReceivedPayload")



@_attrs_define
class ReservationMessageReceivedPayload:
    """ Payload for `reservation.message.received`. A new inbound message arrived on a reservation thread: from the guest, a
    co-traveler, the booker, or Airbnb Support (`from.type: "airbnb"`). The whole message, the same as `GET
    /v1/conversations/{threadId}/messages` returns it, plus where it belongs. Dedupe on `externalMessageId` (or
    `messageId`).

        Attributes:
            hotel_id (None | str | Unset): Booking.com only: the hotel (property) id of the conversation's listing. Absent
                on other channels. A Booking.com Extranet login can cover several hotels, so use this to route the message.
                Example: 10433861.
            reservation_id (int | None | Unset): The reservation the conversation belongs to. `null` for an inquiry, or a
                message that arrived before its booking was imported (`reservation.thread.assigned` fires when it is attached).
                Example: 215906.
            thread_id (str | Unset): The Repull conversation id: the numeric id, as a string. Pass it as `{id}` to `GET
                /v1/conversations/{id}` and `GET /v1/conversations/{id}/messages`. Example: 532457.
            external_thread_id (None | str | Unset): The channel's own thread id (Airbnb thread id, Booking.com conversation
                id). Same as `externalThreadId` on `GET /v1/conversations/{id}`. Example: 2603530383.
            listing_id (int | None | Unset): The Repull listing the conversation is about. Example: 5668.
            channel (str | Unset): The channel the message came through: `airbnb`, `booking`, `vrbo`, … Example: airbnb.
            message_id (str | Unset): Repull message id, as `GET /v1/conversations/{id}/messages` returns it (`id`).
                Example: 1847801.
            external_message_id (None | str | Unset): The channel's own message id. Stable across retries and backfill:
                dedupe on it. Example: 32837172376.
            confirmation_code (None | str | Unset): The reservation's confirmation code on the channel. `null` when there is
                no reservation. Example: HMEXAMPLE1.
            from_ (ReservationMessageReceivedPayloadFrom | Unset):
            body (str | Unset): Empty when the guest sent only a file. Example: Hi! What time can we check in?.
            sent_at (datetime.datetime | Unset): When the message was sent on the channel. Example:
                2026-05-01T15:00:00.000Z.
            direction (ReservationMessageReceivedPayloadDirection | Unset): Always `inbound` on this event.
            sender_type (None | str | Unset): Sender role as stored, the same as `senderType` on `GET
                /v1/conversations/{id}/messages`. Example: guest.
            sender_name (None | str | Unset):  Example: Alex Morgan.
            sender_avatar (None | str | Unset):
            translated_body (None | str | Unset): English translation, when one has been computed.
            attachments (list[ConversationMessageAttachment] | Unset): Files the guest sent (photos, videos, documents),
                same shape as `GET /v1/conversations/{id}/messages`. Empty array when there are none.
            is_automated (bool | Unset):
            ai_generated (bool | Unset):
            status (None | str | Unset): Stored delivery state. Usually `null` on inbound messages (`GET
                /v1/conversations/{id}/messages` shows them as `received`).
            revision (datetime.datetime | None | Unset): Orders two deliveries about the same message without parsing the
                body. Example: 2026-05-01T15:00:00.000Z.
     """

    hotel_id: None | str | Unset = UNSET
    reservation_id: int | None | Unset = UNSET
    thread_id: str | Unset = UNSET
    external_thread_id: None | str | Unset = UNSET
    listing_id: int | None | Unset = UNSET
    channel: str | Unset = UNSET
    message_id: str | Unset = UNSET
    external_message_id: None | str | Unset = UNSET
    confirmation_code: None | str | Unset = UNSET
    from_: ReservationMessageReceivedPayloadFrom | Unset = UNSET
    body: str | Unset = UNSET
    sent_at: datetime.datetime | Unset = UNSET
    direction: ReservationMessageReceivedPayloadDirection | Unset = UNSET
    sender_type: None | str | Unset = UNSET
    sender_name: None | str | Unset = UNSET
    sender_avatar: None | str | Unset = UNSET
    translated_body: None | str | Unset = UNSET
    attachments: list[ConversationMessageAttachment] | Unset = UNSET
    is_automated: bool | Unset = UNSET
    ai_generated: bool | Unset = UNSET
    status: None | str | Unset = UNSET
    revision: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.conversation_message_attachment import ConversationMessageAttachment
        from ..models.reservation_message_received_payload_from import ReservationMessageReceivedPayloadFrom
        hotel_id: None | str | Unset
        if isinstance(self.hotel_id, Unset):
            hotel_id = UNSET
        else:
            hotel_id = self.hotel_id

        reservation_id: int | None | Unset
        if isinstance(self.reservation_id, Unset):
            reservation_id = UNSET
        else:
            reservation_id = self.reservation_id

        thread_id = self.thread_id

        external_thread_id: None | str | Unset
        if isinstance(self.external_thread_id, Unset):
            external_thread_id = UNSET
        else:
            external_thread_id = self.external_thread_id

        listing_id: int | None | Unset
        if isinstance(self.listing_id, Unset):
            listing_id = UNSET
        else:
            listing_id = self.listing_id

        channel = self.channel

        message_id = self.message_id

        external_message_id: None | str | Unset
        if isinstance(self.external_message_id, Unset):
            external_message_id = UNSET
        else:
            external_message_id = self.external_message_id

        confirmation_code: None | str | Unset
        if isinstance(self.confirmation_code, Unset):
            confirmation_code = UNSET
        else:
            confirmation_code = self.confirmation_code

        from_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.to_dict()

        body = self.body

        sent_at: str | Unset = UNSET
        if not isinstance(self.sent_at, Unset):
            sent_at = self.sent_at.isoformat()

        direction: str | Unset = UNSET
        if not isinstance(self.direction, Unset):
            direction = self.direction.value


        sender_type: None | str | Unset
        if isinstance(self.sender_type, Unset):
            sender_type = UNSET
        else:
            sender_type = self.sender_type

        sender_name: None | str | Unset
        if isinstance(self.sender_name, Unset):
            sender_name = UNSET
        else:
            sender_name = self.sender_name

        sender_avatar: None | str | Unset
        if isinstance(self.sender_avatar, Unset):
            sender_avatar = UNSET
        else:
            sender_avatar = self.sender_avatar

        translated_body: None | str | Unset
        if isinstance(self.translated_body, Unset):
            translated_body = UNSET
        else:
            translated_body = self.translated_body

        attachments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)



        is_automated = self.is_automated

        ai_generated = self.ai_generated

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        revision: None | str | Unset
        if isinstance(self.revision, Unset):
            revision = UNSET
        elif isinstance(self.revision, datetime.datetime):
            revision = self.revision.isoformat()
        else:
            revision = self.revision


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if hotel_id is not UNSET:
            field_dict["hotelId"] = hotel_id
        if reservation_id is not UNSET:
            field_dict["reservationId"] = reservation_id
        if thread_id is not UNSET:
            field_dict["threadId"] = thread_id
        if external_thread_id is not UNSET:
            field_dict["externalThreadId"] = external_thread_id
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if channel is not UNSET:
            field_dict["channel"] = channel
        if message_id is not UNSET:
            field_dict["messageId"] = message_id
        if external_message_id is not UNSET:
            field_dict["externalMessageId"] = external_message_id
        if confirmation_code is not UNSET:
            field_dict["confirmationCode"] = confirmation_code
        if from_ is not UNSET:
            field_dict["from"] = from_
        if body is not UNSET:
            field_dict["body"] = body
        if sent_at is not UNSET:
            field_dict["sentAt"] = sent_at
        if direction is not UNSET:
            field_dict["direction"] = direction
        if sender_type is not UNSET:
            field_dict["senderType"] = sender_type
        if sender_name is not UNSET:
            field_dict["senderName"] = sender_name
        if sender_avatar is not UNSET:
            field_dict["senderAvatar"] = sender_avatar
        if translated_body is not UNSET:
            field_dict["translatedBody"] = translated_body
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if is_automated is not UNSET:
            field_dict["isAutomated"] = is_automated
        if ai_generated is not UNSET:
            field_dict["aiGenerated"] = ai_generated
        if status is not UNSET:
            field_dict["status"] = status
        if revision is not UNSET:
            field_dict["revision"] = revision

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conversation_message_attachment import ConversationMessageAttachment
        from ..models.reservation_message_received_payload_from import ReservationMessageReceivedPayloadFrom
        d = dict(src_dict)
        def _parse_hotel_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hotel_id = _parse_hotel_id(d.pop("hotelId", UNSET))


        def _parse_reservation_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        reservation_id = _parse_reservation_id(d.pop("reservationId", UNSET))


        thread_id = d.pop("threadId", UNSET)

        def _parse_external_thread_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_thread_id = _parse_external_thread_id(d.pop("externalThreadId", UNSET))


        def _parse_listing_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        listing_id = _parse_listing_id(d.pop("listingId", UNSET))


        channel = d.pop("channel", UNSET)

        message_id = d.pop("messageId", UNSET)

        def _parse_external_message_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_message_id = _parse_external_message_id(d.pop("externalMessageId", UNSET))


        def _parse_confirmation_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        confirmation_code = _parse_confirmation_code(d.pop("confirmationCode", UNSET))


        _from_ = d.pop("from", UNSET)
        from_: ReservationMessageReceivedPayloadFrom | Unset
        if isinstance(_from_,  Unset):
            from_ = UNSET
        else:
            from_ = ReservationMessageReceivedPayloadFrom.from_dict(_from_)




        body = d.pop("body", UNSET)

        _sent_at = d.pop("sentAt", UNSET)
        sent_at: datetime.datetime | Unset
        if isinstance(_sent_at,  Unset):
            sent_at = UNSET
        else:
            sent_at = isoparse(_sent_at)




        _direction = d.pop("direction", UNSET)
        direction: ReservationMessageReceivedPayloadDirection | Unset
        if isinstance(_direction,  Unset):
            direction = UNSET
        else:
            direction = ReservationMessageReceivedPayloadDirection(_direction)




        def _parse_sender_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sender_type = _parse_sender_type(d.pop("senderType", UNSET))


        def _parse_sender_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sender_name = _parse_sender_name(d.pop("senderName", UNSET))


        def _parse_sender_avatar(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sender_avatar = _parse_sender_avatar(d.pop("senderAvatar", UNSET))


        def _parse_translated_body(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        translated_body = _parse_translated_body(d.pop("translatedBody", UNSET))


        _attachments = d.pop("attachments", UNSET)
        attachments: list[ConversationMessageAttachment] | Unset = UNSET
        if _attachments is not UNSET:
            attachments = []
            for attachments_item_data in _attachments:
                attachments_item = ConversationMessageAttachment.from_dict(attachments_item_data)



                attachments.append(attachments_item)


        is_automated = d.pop("isAutomated", UNSET)

        ai_generated = d.pop("aiGenerated", UNSET)

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_revision(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                revision_type_0 = isoparse(data)



                return revision_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        revision = _parse_revision(d.pop("revision", UNSET))


        reservation_message_received_payload = cls(
            hotel_id=hotel_id,
            reservation_id=reservation_id,
            thread_id=thread_id,
            external_thread_id=external_thread_id,
            listing_id=listing_id,
            channel=channel,
            message_id=message_id,
            external_message_id=external_message_id,
            confirmation_code=confirmation_code,
            from_=from_,
            body=body,
            sent_at=sent_at,
            direction=direction,
            sender_type=sender_type,
            sender_name=sender_name,
            sender_avatar=sender_avatar,
            translated_body=translated_body,
            attachments=attachments,
            is_automated=is_automated,
            ai_generated=ai_generated,
            status=status,
            revision=revision,
        )


        reservation_message_received_payload.additional_properties = d
        return reservation_message_received_payload

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
