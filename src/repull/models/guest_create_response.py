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
  from ..models.guest_create_response_contacts_item import GuestCreateResponseContactsItem





T = TypeVar("T", bound="GuestCreateResponse")



@_attrs_define
class GuestCreateResponse:
    """ 
        Attributes:
            id (int | Unset): Pass to `GET /v1/guests/{id}` for the full profile. Example: 91234.
            created (bool | Unset): `true` when a new guest was written, `false` when an existing guest matched on
                email/phone plus name. Read this rather than assuming a 2xx means a new record.
            first_name (str | Unset):
            last_name (None | str | Unset):
            language (None | str | Unset):
            currency (None | str | Unset):
            is_business_traveler (bool | Unset):
            contacts (list[GuestCreateResponseContactsItem] | Unset): One entry per stored contact. Email and phone are
                separate records.
            created_at (datetime.datetime | Unset):
     """

    id: int | Unset = UNSET
    created: bool | Unset = UNSET
    first_name: str | Unset = UNSET
    last_name: None | str | Unset = UNSET
    language: None | str | Unset = UNSET
    currency: None | str | Unset = UNSET
    is_business_traveler: bool | Unset = UNSET
    contacts: list[GuestCreateResponseContactsItem] | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.guest_create_response_contacts_item import GuestCreateResponseContactsItem
        id = self.id

        created = self.created

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

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        is_business_traveler = self.is_business_traveler

        contacts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.contacts, Unset):
            contacts = []
            for contacts_item_data in self.contacts:
                contacts_item = contacts_item_data.to_dict()
                contacts.append(contacts_item)



        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if created is not UNSET:
            field_dict["created"] = created
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if language is not UNSET:
            field_dict["language"] = language
        if currency is not UNSET:
            field_dict["currency"] = currency
        if is_business_traveler is not UNSET:
            field_dict["isBusinessTraveler"] = is_business_traveler
        if contacts is not UNSET:
            field_dict["contacts"] = contacts
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.guest_create_response_contacts_item import GuestCreateResponseContactsItem
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        created = d.pop("created", UNSET)

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


        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))


        is_business_traveler = d.pop("isBusinessTraveler", UNSET)

        _contacts = d.pop("contacts", UNSET)
        contacts: list[GuestCreateResponseContactsItem] | Unset = UNSET
        if _contacts is not UNSET:
            contacts = []
            for contacts_item_data in _contacts:
                contacts_item = GuestCreateResponseContactsItem.from_dict(contacts_item_data)



                contacts.append(contacts_item)


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        guest_create_response = cls(
            id=id,
            created=created,
            first_name=first_name,
            last_name=last_name,
            language=language,
            currency=currency,
            is_business_traveler=is_business_traveler,
            contacts=contacts,
            created_at=created_at,
        )


        guest_create_response.additional_properties = d
        return guest_create_response

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
