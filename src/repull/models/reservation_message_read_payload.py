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
  from ..models.message_actor import MessageActor





T = TypeVar("T", bound="ReservationMessageReadPayload")



@_attrs_define
class ReservationMessageReadPayload:
    """ Payload for `reservation.message.read`: the guest read the conversation up to and including `messageId`, a message
    from your side. Every earlier message in it was read by then too. Airbnb reports read receipts; other channels do
    not fire this event.

        Attributes:
            reservation_id (int | None | Unset):  Example: 235970.
            thread_id (str | Unset): The conversation id (`GET /v1/conversations/{id}`). Example: 900301.
            external_thread_id (None | str | Unset):  Example: 2648057088.
            listing_id (int | None | Unset):  Example: 23893.
            channel (str | Unset):  Example: airbnb.
            message_id (str | Unset): The newest message the guest has read. Its `readAt` is now set. Example: 1854462.
            external_message_id (None | str | Unset):  Example: 32877308873.
            read_at (datetime.datetime | Unset): When the guest read it, as the channel reports it.
            reader (MessageActor | Unset): Who did something on a message.
     """

    reservation_id: int | None | Unset = UNSET
    thread_id: str | Unset = UNSET
    external_thread_id: None | str | Unset = UNSET
    listing_id: int | None | Unset = UNSET
    channel: str | Unset = UNSET
    message_id: str | Unset = UNSET
    external_message_id: None | str | Unset = UNSET
    read_at: datetime.datetime | Unset = UNSET
    reader: MessageActor | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.message_actor import MessageActor
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

        read_at: str | Unset = UNSET
        if not isinstance(self.read_at, Unset):
            read_at = self.read_at.isoformat()

        reader: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reader, Unset):
            reader = self.reader.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
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
        if read_at is not UNSET:
            field_dict["readAt"] = read_at
        if reader is not UNSET:
            field_dict["reader"] = reader

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message_actor import MessageActor
        d = dict(src_dict)
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


        _read_at = d.pop("readAt", UNSET)
        read_at: datetime.datetime | Unset
        if isinstance(_read_at,  Unset):
            read_at = UNSET
        else:
            read_at = isoparse(_read_at)




        _reader = d.pop("reader", UNSET)
        reader: MessageActor | Unset
        if isinstance(_reader,  Unset):
            reader = UNSET
        else:
            reader = MessageActor.from_dict(_reader)




        reservation_message_read_payload = cls(
            reservation_id=reservation_id,
            thread_id=thread_id,
            external_thread_id=external_thread_id,
            listing_id=listing_id,
            channel=channel,
            message_id=message_id,
            external_message_id=external_message_id,
            read_at=read_at,
            reader=reader,
        )


        reservation_message_read_payload.additional_properties = d
        return reservation_message_read_payload

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
