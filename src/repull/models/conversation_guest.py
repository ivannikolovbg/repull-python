from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.conversation_guest_contact import ConversationGuestContact





T = TypeVar("T", bound="ConversationGuest")



@_attrs_define
class ConversationGuest:
    """ Linked guest metadata for a conversation thread. Resolved through the thread's `reservation_id` →
    `reservations.guest_id`. Up to 50 contacts are returned.

        Attributes:
            id (str | Unset):
            display_name (str | Unset):
            contacts (list[ConversationGuestContact] | Unset):
     """

    id: str | Unset = UNSET
    display_name: str | Unset = UNSET
    contacts: list[ConversationGuestContact] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.conversation_guest_contact import ConversationGuestContact
        id = self.id

        display_name = self.display_name

        contacts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.contacts, Unset):
            contacts = []
            for contacts_item_data in self.contacts:
                contacts_item = contacts_item_data.to_dict()
                contacts.append(contacts_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if contacts is not UNSET:
            field_dict["contacts"] = contacts

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conversation_guest_contact import ConversationGuestContact
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        display_name = d.pop("displayName", UNSET)

        _contacts = d.pop("contacts", UNSET)
        contacts: list[ConversationGuestContact] | Unset = UNSET
        if _contacts is not UNSET:
            contacts = []
            for contacts_item_data in _contacts:
                contacts_item = ConversationGuestContact.from_dict(contacts_item_data)



                contacts.append(contacts_item)


        conversation_guest = cls(
            id=id,
            display_name=display_name,
            contacts=contacts,
        )


        conversation_guest.additional_properties = d
        return conversation_guest

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
