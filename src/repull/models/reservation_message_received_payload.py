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
  from ..models.reservation_message_received_payload_from import ReservationMessageReceivedPayloadFrom





T = TypeVar("T", bound="ReservationMessageReceivedPayload")



@_attrs_define
class ReservationMessageReceivedPayload:
    """ Payload for `reservation.message.received`. A new inbound message arrived on a reservation thread.

        Attributes:
            reservation_id (int | Unset):  Example: 215906.
            thread_id (str | Unset):  Example: thr_01HX5XPQ2K.
            from_ (ReservationMessageReceivedPayloadFrom | Unset):
            body (str | Unset):  Example: Hi! What time can we check in?.
            sent_at (datetime.datetime | Unset):  Example: 2026-05-01T15:00:00.000Z.
     """

    reservation_id: int | Unset = UNSET
    thread_id: str | Unset = UNSET
    from_: ReservationMessageReceivedPayloadFrom | Unset = UNSET
    body: str | Unset = UNSET
    sent_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.reservation_message_received_payload_from import ReservationMessageReceivedPayloadFrom
        reservation_id = self.reservation_id

        thread_id = self.thread_id

        from_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.to_dict()

        body = self.body

        sent_at: str | Unset = UNSET
        if not isinstance(self.sent_at, Unset):
            sent_at = self.sent_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if reservation_id is not UNSET:
            field_dict["reservationId"] = reservation_id
        if thread_id is not UNSET:
            field_dict["threadId"] = thread_id
        if from_ is not UNSET:
            field_dict["from"] = from_
        if body is not UNSET:
            field_dict["body"] = body
        if sent_at is not UNSET:
            field_dict["sentAt"] = sent_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reservation_message_received_payload_from import ReservationMessageReceivedPayloadFrom
        d = dict(src_dict)
        reservation_id = d.pop("reservationId", UNSET)

        thread_id = d.pop("threadId", UNSET)

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




        reservation_message_received_payload = cls(
            reservation_id=reservation_id,
            thread_id=thread_id,
            from_=from_,
            body=body,
            sent_at=sent_at,
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
