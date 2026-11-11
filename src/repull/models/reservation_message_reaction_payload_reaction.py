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





T = TypeVar("T", bound="ReservationMessageReactionPayloadReaction")



@_attrs_define
class ReservationMessageReactionPayloadReaction:
    """ 
        Attributes:
            id (str | Unset):  Example: 9e0b945a-b03d-4e28-ad48-5f7fc706a67f.
            emoji (str | Unset):  Example: ❤️.
            by (MessageActor | Unset): Who did something on a message.
            at (datetime.datetime | Unset): When it was added; for `removed`, when Repull saw it go.
     """

    id: str | Unset = UNSET
    emoji: str | Unset = UNSET
    by: MessageActor | Unset = UNSET
    at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.message_actor import MessageActor
        id = self.id

        emoji = self.emoji

        by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.by, Unset):
            by = self.by.to_dict()

        at: str | Unset = UNSET
        if not isinstance(self.at, Unset):
            at = self.at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if emoji is not UNSET:
            field_dict["emoji"] = emoji
        if by is not UNSET:
            field_dict["by"] = by
        if at is not UNSET:
            field_dict["at"] = at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message_actor import MessageActor
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        emoji = d.pop("emoji", UNSET)

        _by = d.pop("by", UNSET)
        by: MessageActor | Unset
        if isinstance(_by,  Unset):
            by = UNSET
        else:
            by = MessageActor.from_dict(_by)




        _at = d.pop("at", UNSET)
        at: datetime.datetime | Unset
        if isinstance(_at,  Unset):
            at = UNSET
        else:
            at = isoparse(_at)




        reservation_message_reaction_payload_reaction = cls(
            id=id,
            emoji=emoji,
            by=by,
            at=at,
        )


        reservation_message_reaction_payload_reaction.additional_properties = d
        return reservation_message_reaction_payload_reaction

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
