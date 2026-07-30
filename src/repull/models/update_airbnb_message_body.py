from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.update_airbnb_message_body_action import UpdateAirbnbMessageBodyAction
from ..types import UNSET, Unset






T = TypeVar("T", bound="UpdateAirbnbMessageBody")



@_attrs_define
class UpdateAirbnbMessageBody:
    """ 
        Attributes:
            action (UpdateAirbnbMessageBodyAction): Operation to perform on the message.
            message (str | Unset): New message text. Required when `action` is `edit`.
            reaction (str | Unset): Reaction to add. Required when `action` is `react`.
     """

    action: UpdateAirbnbMessageBodyAction
    message: str | Unset = UNSET
    reaction: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        action = self.action.value

        message = self.message

        reaction = self.reaction


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "action": action,
        })
        if message is not UNSET:
            field_dict["message"] = message
        if reaction is not UNSET:
            field_dict["reaction"] = reaction

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = UpdateAirbnbMessageBodyAction(d.pop("action"))




        message = d.pop("message", UNSET)

        reaction = d.pop("reaction", UNSET)

        update_airbnb_message_body = cls(
            action=action,
            message=message,
            reaction=reaction,
        )


        update_airbnb_message_body.additional_properties = d
        return update_airbnb_message_body

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
