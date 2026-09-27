from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.reservation_message_sent_payload_direction import ReservationMessageSentPayloadDirection
from ..models.reservation_message_sent_payload_source import ReservationMessageSentPayloadSource
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.conversation_message_attachment import ConversationMessageAttachment
  from ..models.reservation_message_sent_payload_from import ReservationMessageSentPayloadFrom





T = TypeVar("T", bound="ReservationMessageSentPayload")



@_attrs_define
class ReservationMessageSentPayload:
    """ Payload for `reservation.message.sent`: a host-side message was sent on a reservation thread. Same fields as
    `reservation.message.received`, plus `source`.

        Attributes:
            reservation_id (int | None | Unset):  Example: 235970.
            thread_id (str | Unset):  Example: 161347.
            message_id (str | Unset): Repull message id, as `GET /v1/conversations/{id}/messages` returns it. Example:
                1854462.
            external_message_id (None | str | Unset): The channel's own message id. Dedupe on it. Example: 32877308873.
            channel (str | Unset):  Example: airbnb.
            source (ReservationMessageSentPayloadSource | Unset): `channel`: sent in the channel's own app (e.g. the Airbnb
                app). `repull`: sent through Repull — the API, the dashboard, an automation or AI.
            from_ (ReservationMessageSentPayloadFrom | Unset):
            body (str | Unset):
            sent_at (datetime.datetime | Unset):
            direction (ReservationMessageSentPayloadDirection | Unset):
            is_automated (bool | Unset):
            ai_generated (bool | Unset):
            attachments (list[ConversationMessageAttachment] | Unset):
     """

    reservation_id: int | None | Unset = UNSET
    thread_id: str | Unset = UNSET
    message_id: str | Unset = UNSET
    external_message_id: None | str | Unset = UNSET
    channel: str | Unset = UNSET
    source: ReservationMessageSentPayloadSource | Unset = UNSET
    from_: ReservationMessageSentPayloadFrom | Unset = UNSET
    body: str | Unset = UNSET
    sent_at: datetime.datetime | Unset = UNSET
    direction: ReservationMessageSentPayloadDirection | Unset = UNSET
    is_automated: bool | Unset = UNSET
    ai_generated: bool | Unset = UNSET
    attachments: list[ConversationMessageAttachment] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.conversation_message_attachment import ConversationMessageAttachment
        from ..models.reservation_message_sent_payload_from import ReservationMessageSentPayloadFrom
        reservation_id: int | None | Unset
        if isinstance(self.reservation_id, Unset):
            reservation_id = UNSET
        else:
            reservation_id = self.reservation_id

        thread_id = self.thread_id

        message_id = self.message_id

        external_message_id: None | str | Unset
        if isinstance(self.external_message_id, Unset):
            external_message_id = UNSET
        else:
            external_message_id = self.external_message_id

        channel = self.channel

        source: str | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value


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


        is_automated = self.is_automated

        ai_generated = self.ai_generated

        attachments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if reservation_id is not UNSET:
            field_dict["reservationId"] = reservation_id
        if thread_id is not UNSET:
            field_dict["threadId"] = thread_id
        if message_id is not UNSET:
            field_dict["messageId"] = message_id
        if external_message_id is not UNSET:
            field_dict["externalMessageId"] = external_message_id
        if channel is not UNSET:
            field_dict["channel"] = channel
        if source is not UNSET:
            field_dict["source"] = source
        if from_ is not UNSET:
            field_dict["from"] = from_
        if body is not UNSET:
            field_dict["body"] = body
        if sent_at is not UNSET:
            field_dict["sentAt"] = sent_at
        if direction is not UNSET:
            field_dict["direction"] = direction
        if is_automated is not UNSET:
            field_dict["isAutomated"] = is_automated
        if ai_generated is not UNSET:
            field_dict["aiGenerated"] = ai_generated
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conversation_message_attachment import ConversationMessageAttachment
        from ..models.reservation_message_sent_payload_from import ReservationMessageSentPayloadFrom
        d = dict(src_dict)
        def _parse_reservation_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        reservation_id = _parse_reservation_id(d.pop("reservationId", UNSET))


        thread_id = d.pop("threadId", UNSET)

        message_id = d.pop("messageId", UNSET)

        def _parse_external_message_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_message_id = _parse_external_message_id(d.pop("externalMessageId", UNSET))


        channel = d.pop("channel", UNSET)

        _source = d.pop("source", UNSET)
        source: ReservationMessageSentPayloadSource | Unset
        if isinstance(_source,  Unset):
            source = UNSET
        else:
            source = ReservationMessageSentPayloadSource(_source)




        _from_ = d.pop("from", UNSET)
        from_: ReservationMessageSentPayloadFrom | Unset
        if isinstance(_from_,  Unset):
            from_ = UNSET
        else:
            from_ = ReservationMessageSentPayloadFrom.from_dict(_from_)




        body = d.pop("body", UNSET)

        _sent_at = d.pop("sentAt", UNSET)
        sent_at: datetime.datetime | Unset
        if isinstance(_sent_at,  Unset):
            sent_at = UNSET
        else:
            sent_at = isoparse(_sent_at)




        _direction = d.pop("direction", UNSET)
        direction: ReservationMessageSentPayloadDirection | Unset
        if isinstance(_direction,  Unset):
            direction = UNSET
        else:
            direction = ReservationMessageSentPayloadDirection(_direction)




        is_automated = d.pop("isAutomated", UNSET)

        ai_generated = d.pop("aiGenerated", UNSET)

        _attachments = d.pop("attachments", UNSET)
        attachments: list[ConversationMessageAttachment] | Unset = UNSET
        if _attachments is not UNSET:
            attachments = []
            for attachments_item_data in _attachments:
                attachments_item = ConversationMessageAttachment.from_dict(attachments_item_data)



                attachments.append(attachments_item)


        reservation_message_sent_payload = cls(
            reservation_id=reservation_id,
            thread_id=thread_id,
            message_id=message_id,
            external_message_id=external_message_id,
            channel=channel,
            source=source,
            from_=from_,
            body=body,
            sent_at=sent_at,
            direction=direction,
            is_automated=is_automated,
            ai_generated=ai_generated,
            attachments=attachments,
        )


        reservation_message_sent_payload.additional_properties = d
        return reservation_message_sent_payload

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
