from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.reservation_message_reaction_payload_action import ReservationMessageReactionPayloadAction
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.reservation_message_reaction_payload_reaction import ReservationMessageReactionPayloadReaction





T = TypeVar("T", bound="ReservationMessageReactionPayload")



@_attrs_define
class ReservationMessageReactionPayload:
    """ Payload for `reservation.message.reaction`: someone on the conversation added or removed a reaction. Airbnb reports
    reactions; other channels do not fire this event.

        Attributes:
            reservation_id (int | None | Unset):  Example: 235970.
            thread_id (str | Unset):  Example: 900301.
            external_thread_id (None | str | Unset):  Example: 2648057088.
            listing_id (int | None | Unset):  Example: 23893.
            channel (str | Unset):  Example: airbnb.
            message_id (str | Unset): The message reacted to. Example: 1854462.
            external_message_id (None | str | Unset):  Example: 33532605539.
            action (ReservationMessageReactionPayloadAction | Unset):
            reaction (ReservationMessageReactionPayloadReaction | Unset):
     """

    reservation_id: int | None | Unset = UNSET
    thread_id: str | Unset = UNSET
    external_thread_id: None | str | Unset = UNSET
    listing_id: int | None | Unset = UNSET
    channel: str | Unset = UNSET
    message_id: str | Unset = UNSET
    external_message_id: None | str | Unset = UNSET
    action: ReservationMessageReactionPayloadAction | Unset = UNSET
    reaction: ReservationMessageReactionPayloadReaction | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.reservation_message_reaction_payload_reaction import ReservationMessageReactionPayloadReaction
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

        action: str | Unset = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.value


        reaction: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reaction, Unset):
            reaction = self.reaction.to_dict()


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
        if action is not UNSET:
            field_dict["action"] = action
        if reaction is not UNSET:
            field_dict["reaction"] = reaction

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reservation_message_reaction_payload_reaction import ReservationMessageReactionPayloadReaction
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


        _action = d.pop("action", UNSET)
        action: ReservationMessageReactionPayloadAction | Unset
        if isinstance(_action,  Unset):
            action = UNSET
        else:
            action = ReservationMessageReactionPayloadAction(_action)




        _reaction = d.pop("reaction", UNSET)
        reaction: ReservationMessageReactionPayloadReaction | Unset
        if isinstance(_reaction,  Unset):
            reaction = UNSET
        else:
            reaction = ReservationMessageReactionPayloadReaction.from_dict(_reaction)




        reservation_message_reaction_payload = cls(
            reservation_id=reservation_id,
            thread_id=thread_id,
            external_thread_id=external_thread_id,
            listing_id=listing_id,
            channel=channel,
            message_id=message_id,
            external_message_id=external_message_id,
            action=action,
            reaction=reaction,
        )


        reservation_message_reaction_payload.additional_properties = d
        return reservation_message_reaction_payload

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
