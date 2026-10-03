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
  from ..models.guest_update_response_contacts_item import GuestUpdateResponseContactsItem
  from ..models.guest_update_response_pms_item import GuestUpdateResponsePmsItem





T = TypeVar("T", bound="GuestUpdateResponse")



@_attrs_define
class GuestUpdateResponse:
    """ 
        Attributes:
            id (int | Unset):
            first_name (str | Unset):
            last_name (None | str | Unset):
            language (None | str | Unset):
            contacts (list[GuestUpdateResponseContactsItem] | Unset):
            updated_at (datetime.datetime | None | Unset):
            pms (list[GuestUpdateResponsePmsItem] | Unset): Each PMS the change was written to first (the guest's linked
                PMSs), with the sections it applied.
     """

    id: int | Unset = UNSET
    first_name: str | Unset = UNSET
    last_name: None | str | Unset = UNSET
    language: None | str | Unset = UNSET
    contacts: list[GuestUpdateResponseContactsItem] | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    pms: list[GuestUpdateResponsePmsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.guest_update_response_contacts_item import GuestUpdateResponseContactsItem
        from ..models.guest_update_response_pms_item import GuestUpdateResponsePmsItem
        id = self.id

        first_name = self.first_name

        last_name: None | str | Unset
        if isinstance(self.last_name, Unset):
            last_name = UNSET
        else:
            last_name = self.last_name

        language: None | str | Unset
        if isinstance(self.language, Unset):
            language = UNSET
        else:
            language = self.language

        contacts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.contacts, Unset):
            contacts = []
            for contacts_item_data in self.contacts:
                contacts_item = contacts_item_data.to_dict()
                contacts.append(contacts_item)



        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        pms: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pms, Unset):
            pms = []
            for pms_item_data in self.pms:
                pms_item = pms_item_data.to_dict()
                pms.append(pms_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if language is not UNSET:
            field_dict["language"] = language
        if contacts is not UNSET:
            field_dict["contacts"] = contacts
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if pms is not UNSET:
            field_dict["pms"] = pms

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.guest_update_response_contacts_item import GuestUpdateResponseContactsItem
        from ..models.guest_update_response_pms_item import GuestUpdateResponsePmsItem
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        first_name = d.pop("firstName", UNSET)

        def _parse_last_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_name = _parse_last_name(d.pop("lastName", UNSET))


        def _parse_language(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        language = _parse_language(d.pop("language", UNSET))


        _contacts = d.pop("contacts", UNSET)
        contacts: list[GuestUpdateResponseContactsItem] | Unset = UNSET
        if _contacts is not UNSET:
            contacts = []
            for contacts_item_data in _contacts:
                contacts_item = GuestUpdateResponseContactsItem.from_dict(contacts_item_data)



                contacts.append(contacts_item)


        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = isoparse(data)



                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updatedAt", UNSET))


        _pms = d.pop("pms", UNSET)
        pms: list[GuestUpdateResponsePmsItem] | Unset = UNSET
        if _pms is not UNSET:
            pms = []
            for pms_item_data in _pms:
                pms_item = GuestUpdateResponsePmsItem.from_dict(pms_item_data)



                pms.append(pms_item)


        guest_update_response = cls(
            id=id,
            first_name=first_name,
            last_name=last_name,
            language=language,
            contacts=contacts,
            updated_at=updated_at,
            pms=pms,
        )


        guest_update_response.additional_properties = d
        return guest_update_response

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
