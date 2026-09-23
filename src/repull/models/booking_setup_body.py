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
  from ..models.booking_setup_body_legal_entity import BookingSetupBodyLegalEntity





T = TypeVar("T", bound="BookingSetupBody")



@_attrs_define
class BookingSetupBody:
    """ 
        Attributes:
            action (BookingSetupBodyAction):
            listing_id (int | Unset): Repull listing id — required for `create-property`, `add-room` and `add-unit`. NOT a
                Booking.com Hotel ID. `listingId` is accepted as an alias.
            property_id (str | Unset): Booking.com Hotel ID — required for `add-room`, `add-unit`, `advance`, and the
                readiness/open/contacts/policies actions.
            room_id (int | Unset): Booking.com room id — required for `add-unit`. `GET
                /v1/channels/booking/properties/{listingId}/rooms` lists them. `roomId` is accepted as an alias.
            legal_entity_id (int | Unset): Optional override for `create-property`. Omit it: the legal entity this workspace
                already uses is resolved automatically. An id that carries another workspace's properties is refused with `403
                legal_entity_not_yours`. `legalEntityId` is accepted as an alias.
            legal_entity (BookingSetupBodyLegalEntity | Unset): Used by `create-property` ONLY when this workspace has no
                legal entity yet — one is registered with Booking.com from these details and used for the property. Ignored when
                the workspace already has one, so a second is never registered.
            leid (int | Unset): Legal entity id — required for `check-legal-status`, which always answers 404.
            contacts (list[BookingSetupBodyContactsItem] | Unset): Contacts payload for `set-contacts`.
     """

    action: BookingSetupBodyAction
    listing_id: int | Unset = UNSET
    property_id: str | Unset = UNSET
    room_id: int | Unset = UNSET
    legal_entity_id: int | Unset = UNSET
    legal_entity: BookingSetupBodyLegalEntity | Unset = UNSET
    leid: int | Unset = UNSET
    contacts: list[BookingSetupBodyContactsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.booking_setup_body_contacts_item import BookingSetupBodyContactsItem
        from ..models.booking_setup_body_legal_entity import BookingSetupBodyLegalEntity
        action = self.action.value

        listing_id = self.listing_id

        property_id = self.property_id

        room_id = self.room_id

        legal_entity_id = self.legal_entity_id

        legal_entity: dict[str, Any] | Unset = UNSET
        if not isinstance(self.legal_entity, Unset):
            legal_entity = self.legal_entity.to_dict()

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
        if listing_id is not UNSET:
            field_dict["listing_id"] = listing_id
        if property_id is not UNSET:
            field_dict["property_id"] = property_id
        if room_id is not UNSET:
            field_dict["room_id"] = room_id
        if legal_entity_id is not UNSET:
            field_dict["legal_entity_id"] = legal_entity_id
        if legal_entity is not UNSET:
            field_dict["legal_entity"] = legal_entity
        if leid is not UNSET:
            field_dict["leid"] = leid
        if contacts is not UNSET:
            field_dict["contacts"] = contacts

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.booking_setup_body_contacts_item import BookingSetupBodyContactsItem
        from ..models.booking_setup_body_legal_entity import BookingSetupBodyLegalEntity
        d = dict(src_dict)
        action = BookingSetupBodyAction(d.pop("action"))




        listing_id = d.pop("listing_id", UNSET)

        property_id = d.pop("property_id", UNSET)

        room_id = d.pop("room_id", UNSET)

        legal_entity_id = d.pop("legal_entity_id", UNSET)

        _legal_entity = d.pop("legal_entity", UNSET)
        legal_entity: BookingSetupBodyLegalEntity | Unset
        if isinstance(_legal_entity,  Unset):
            legal_entity = UNSET
        else:
            legal_entity = BookingSetupBodyLegalEntity.from_dict(_legal_entity)




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
            listing_id=listing_id,
            property_id=property_id,
            room_id=room_id,
            legal_entity_id=legal_entity_id,
            legal_entity=legal_entity,
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
