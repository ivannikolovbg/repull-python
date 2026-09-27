from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.reservation_message_updated_payload_direction import ReservationMessageUpdatedPayloadDirection
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.reservation_message_updated_payload_from import ReservationMessageUpdatedPayloadFrom





T = TypeVar("T", bound="ReservationMessageUpdatedPayload")



@_attrs_define
class ReservationMessageUpdatedPayload:
    """ Payload for `reservation.message.updated`: a message was edited on the channel. `body` is the new text;
    `previousBody` what it replaced. Read receipts and reactions do not fire it.

        Attributes:
            reservation_id (int | None | Unset):  Example: 235970.
            thread_id (str | Unset):  Example: 161347.
            message_id (str | Unset):  Example: 1854462.
            external_message_id (None | str | Unset):  Example: 32877308873.
            channel (str | Unset):  Example: airbnb.
            from_ (ReservationMessageUpdatedPayloadFrom | Unset):
            body (str | Unset): The text after the edit.
            previous_body (str | Unset): The text before the edit.
            edited_at (datetime.datetime | Unset): When the edit was made, as the channel reports it. Also the event's
                `revision`.
            sent_at (datetime.datetime | Unset): When the message was first sent.
            direction (ReservationMessageUpdatedPayloadDirection | Unset):
     """

    reservation_id: int | None | Unset = UNSET
    thread_id: str | Unset = UNSET
    message_id: str | Unset = UNSET
    external_message_id: None | str | Unset = UNSET
    channel: str | Unset = UNSET
    from_: ReservationMessageUpdatedPayloadFrom | Unset = UNSET
    body: str | Unset = UNSET
    previous_body: str | Unset = UNSET
    edited_at: datetime.datetime | Unset = UNSET
    sent_at: datetime.datetime | Unset = UNSET
    direction: ReservationMessageUpdatedPayloadDirection | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.reservation_message_updated_payload_from import ReservationMessageUpdatedPayloadFrom
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

        from_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.to_dict()

        body = self.body

        previous_body = self.previous_body

        edited_at: str | Unset = UNSET
        if not isinstance(self.edited_at, Unset):
            edited_at = self.edited_at.isoformat()

        sent_at: str | Unset = UNSET
        if not isinstance(self.sent_at, Unset):
            sent_at = self.sent_at.isoformat()

        direction: str | Unset = UNSET
        if not isinstance(self.direction, Unset):
            direction = self.direction.value



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
        if from_ is not UNSET:
            field_dict["from"] = from_
        if body is not UNSET:
            field_dict["body"] = body
        if previous_body is not UNSET:
            field_dict["previousBody"] = previous_body
        if edited_at is not UNSET:
            field_dict["editedAt"] = edited_at
        if sent_at is not UNSET:
            field_dict["sentAt"] = sent_at
        if direction is not UNSET:
            field_dict["direction"] = direction

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reservation_message_updated_payload_from import ReservationMessageUpdatedPayloadFrom
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

        _from_ = d.pop("from", UNSET)
        from_: ReservationMessageUpdatedPayloadFrom | Unset
        if isinstance(_from_,  Unset):
            from_ = UNSET
        else:
            from_ = ReservationMessageUpdatedPayloadFrom.from_dict(_from_)




        body = d.pop("body", UNSET)

        previous_body = d.pop("previousBody", UNSET)

        _edited_at = d.pop("editedAt", UNSET)
        edited_at: datetime.datetime | Unset
        if isinstance(_edited_at,  Unset):
            edited_at = UNSET
        else:
            edited_at = isoparse(_edited_at)




        _sent_at = d.pop("sentAt", UNSET)
        sent_at: datetime.datetime | Unset
        if isinstance(_sent_at,  Unset):
            sent_at = UNSET
        else:
            sent_at = isoparse(_sent_at)




        _direction = d.pop("direction", UNSET)
        direction: ReservationMessageUpdatedPayloadDirection | Unset
        if isinstance(_direction,  Unset):
            direction = UNSET
        else:
            direction = ReservationMessageUpdatedPayloadDirection(_direction)




        reservation_message_updated_payload = cls(
            reservation_id=reservation_id,
            thread_id=thread_id,
            message_id=message_id,
            external_message_id=external_message_id,
            channel=channel,
            from_=from_,
            body=body,
            previous_body=previous_body,
            edited_at=edited_at,
            sent_at=sent_at,
            direction=direction,
        )


        reservation_message_updated_payload.additional_properties = d
        return reservation_message_updated_payload

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
