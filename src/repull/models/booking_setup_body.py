from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.booking_setup_body_action import BookingSetupBodyAction
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.booking_setup_body_contacts_item import BookingSetupBodyContactsItem





T = TypeVar("T", bound="BookingSetupBody")



@_attrs_define
class BookingSetupBody:
    """ 
        Attributes:
            action (BookingSetupBodyAction):
            property_id (str | Unset): Booking.com property id — required for readiness/open/contacts/policies actions.
            leid (int | Unset): Legal entity id — required for `check-legal-status`.
            contacts (list[BookingSetupBodyContactsItem] | Unset): Contacts payload for `set-contacts`.
     """

    action: BookingSetupBodyAction
    property_id: str | Unset = UNSET
    leid: int | Unset = UNSET
    contacts: list[BookingSetupBodyContactsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.booking_setup_body_contacts_item import BookingSetupBodyContactsItem
        action = self.action.value

        property_id = self.property_id

        leid = self.leid

        contacts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.contacts, Unset):
            contacts = []
            for contacts_item_data in self.contacts:
                contacts_item = contacts_item_data.to_dict()
                contacts.append(contacts_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "action": action,
        })
        if property_id is not UNSET:
            field_dict["property_id"] = property_id
        if leid is not UNSET:
            field_dict["leid"] = leid
        if contacts is not UNSET:
            field_dict["contacts"] = contacts

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.booking_setup_body_contacts_item import BookingSetupBodyContactsItem
        d = dict(src_dict)
        action = BookingSetupBodyAction(d.pop("action"))




        property_id = d.pop("property_id", UNSET)

        leid = d.pop("leid", UNSET)

        _contacts = d.pop("contacts", UNSET)
        contacts: list[BookingSetupBodyContactsItem] | Unset = UNSET
        if _contacts is not UNSET:
            contacts = []
            for contacts_item_data in _contacts:
                contacts_item = BookingSetupBodyContactsItem.from_dict(contacts_item_data)



                contacts.append(contacts_item)


        booking_setup_body = cls(
            action=action,
            property_id=property_id,
            leid=leid,
            contacts=contacts,
        )


        booking_setup_body.additional_properties = d
        return booking_setup_body

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
