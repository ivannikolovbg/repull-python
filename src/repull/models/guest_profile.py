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
  from ..models.guest_contact import GuestContact
  from ..models.guest_flag import GuestFlag
  from ..models.guest_note import GuestNote
  from ..models.guest_reservations_summary import GuestReservationsSummary





T = TypeVar("T", bound="GuestProfile")



@_attrs_define
class GuestProfile:
    """ Full guest profile returned by `GET /v1/guests/{id}`. Aggregates the base list-row fields plus contacts, flags,
    notes, risk metadata, and a reservations-summary rollup.

        Attributes:
            id (int | Unset):
            display_name (str | Unset):
            display_name_long (str | Unset):
            avatar_url (None | str | Unset):
            language (None | str | Unset):
            country (None | str | Unset):
            phone (None | str | Unset):
            email (None | str | Unset):
            total_reservations (int | Unset):
            total_revenue (str | Unset): Decimal as string.
            currency (None | str | Unset):
            is_blacklisted (bool | Unset):
            blacklisted_reason (None | str | Unset):
            risk_level (None | str | Unset): Main-vanio risk score (e.g. `low`, `medium`, `high`).
            verification_level (None | str | Unset):
            created_at (datetime.datetime | None | Unset):
            contacts (list[GuestContact] | Unset):
            flags (list[GuestFlag] | Unset):
            notes (list[GuestNote] | Unset):
            reservations_summary (GuestReservationsSummary | Unset): Aggregate counts of reservations attached to the guest.
                `future` is derived from `total - past - cancelled`.
     """

    id: int | Unset = UNSET
    display_name: str | Unset = UNSET
    display_name_long: str | Unset = UNSET
    avatar_url: None | str | Unset = UNSET
    language: None | str | Unset = UNSET
    country: None | str | Unset = UNSET
    phone: None | str | Unset = UNSET
    email: None | str | Unset = UNSET
    total_reservations: int | Unset = UNSET
    total_revenue: str | Unset = UNSET
    currency: None | str | Unset = UNSET
    is_blacklisted: bool | Unset = UNSET
    blacklisted_reason: None | str | Unset = UNSET
    risk_level: None | str | Unset = UNSET
    verification_level: None | str | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    contacts: list[GuestContact] | Unset = UNSET
    flags: list[GuestFlag] | Unset = UNSET
    notes: list[GuestNote] | Unset = UNSET
    reservations_summary: GuestReservationsSummary | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.guest_contact import GuestContact
        from ..models.guest_flag import GuestFlag
        from ..models.guest_note import GuestNote
        from ..models.guest_reservations_summary import GuestReservationsSummary
        id = self.id

        display_name = self.display_name

        display_name_long = self.display_name_long

        avatar_url: None | str | Unset
        if isinstance(self.avatar_url, Unset):
            avatar_url = UNSET
        else:
            avatar_url = self.avatar_url

        language: None | str | Unset
        if isinstance(self.language, Unset):
            language = UNSET
        else:
            language = self.language

        country: None | str | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

        phone: None | str | Unset
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        total_reservations = self.total_reservations

        total_revenue = self.total_revenue

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        is_blacklisted = self.is_blacklisted

        blacklisted_reason: None | str | Unset
        if isinstance(self.blacklisted_reason, Unset):
            blacklisted_reason = UNSET
        else:
            blacklisted_reason = self.blacklisted_reason

        risk_level: None | str | Unset
        if isinstance(self.risk_level, Unset):
            risk_level = UNSET
        else:
            risk_level = self.risk_level

        verification_level: None | str | Unset
        if isinstance(self.verification_level, Unset):
            verification_level = UNSET
        else:
            verification_level = self.verification_level

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        contacts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.contacts, Unset):
            contacts = []
            for contacts_item_data in self.contacts:
                contacts_item = contacts_item_data.to_dict()
                contacts.append(contacts_item)



        flags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.flags, Unset):
            flags = []
            for flags_item_data in self.flags:
                flags_item = flags_item_data.to_dict()
                flags.append(flags_item)



        notes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.notes, Unset):
            notes = []
            for notes_item_data in self.notes:
                notes_item = notes_item_data.to_dict()
                notes.append(notes_item)



        reservations_summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reservations_summary, Unset):
            reservations_summary = self.reservations_summary.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if display_name_long is not UNSET:
            field_dict["displayNameLong"] = display_name_long
        if avatar_url is not UNSET:
            field_dict["avatarUrl"] = avatar_url
        if language is not UNSET:
            field_dict["language"] = language
        if country is not UNSET:
            field_dict["country"] = country
        if phone is not UNSET:
            field_dict["phone"] = phone
        if email is not UNSET:
            field_dict["email"] = email
        if total_reservations is not UNSET:
            field_dict["totalReservations"] = total_reservations
        if total_revenue is not UNSET:
            field_dict["totalRevenue"] = total_revenue
        if currency is not UNSET:
            field_dict["currency"] = currency
        if is_blacklisted is not UNSET:
            field_dict["isBlacklisted"] = is_blacklisted
        if blacklisted_reason is not UNSET:
            field_dict["blacklistedReason"] = blacklisted_reason
        if risk_level is not UNSET:
            field_dict["riskLevel"] = risk_level
        if verification_level is not UNSET:
            field_dict["verificationLevel"] = verification_level
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if contacts is not UNSET:
            field_dict["contacts"] = contacts
        if flags is not UNSET:
            field_dict["flags"] = flags
        if notes is not UNSET:
            field_dict["notes"] = notes
        if reservations_summary is not UNSET:
            field_dict["reservations_summary"] = reservations_summary

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.guest_contact import GuestContact
        from ..models.guest_flag import GuestFlag
        from ..models.guest_note import GuestNote
        from ..models.guest_reservations_summary import GuestReservationsSummary
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        display_name = d.pop("displayName", UNSET)

        display_name_long = d.pop("displayNameLong", UNSET)

        def _parse_avatar_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar_url = _parse_avatar_url(d.pop("avatarUrl", UNSET))


        def _parse_language(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        language = _parse_language(d.pop("language", UNSET))


        def _parse_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country = _parse_country(d.pop("country", UNSET))


        def _parse_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone = _parse_phone(d.pop("phone", UNSET))


        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))


        total_reservations = d.pop("totalReservations", UNSET)

        total_revenue = d.pop("totalRevenue", UNSET)

        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))


        is_blacklisted = d.pop("isBlacklisted", UNSET)

        def _parse_blacklisted_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        blacklisted_reason = _parse_blacklisted_reason(d.pop("blacklistedReason", UNSET))


        def _parse_risk_level(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        risk_level = _parse_risk_level(d.pop("riskLevel", UNSET))


        def _parse_verification_level(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        verification_level = _parse_verification_level(d.pop("verificationLevel", UNSET))


        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = isoparse(data)



                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))


        _contacts = d.pop("contacts", UNSET)
        contacts: list[GuestContact] | Unset = UNSET
        if _contacts is not UNSET:
            contacts = []
            for contacts_item_data in _contacts:
                contacts_item = GuestContact.from_dict(contacts_item_data)



                contacts.append(contacts_item)


        _flags = d.pop("flags", UNSET)
        flags: list[GuestFlag] | Unset = UNSET
        if _flags is not UNSET:
            flags = []
            for flags_item_data in _flags:
                flags_item = GuestFlag.from_dict(flags_item_data)



                flags.append(flags_item)


        _notes = d.pop("notes", UNSET)
        notes: list[GuestNote] | Unset = UNSET
        if _notes is not UNSET:
            notes = []
            for notes_item_data in _notes:
                notes_item = GuestNote.from_dict(notes_item_data)



                notes.append(notes_item)


        _reservations_summary = d.pop("reservations_summary", UNSET)
        reservations_summary: GuestReservationsSummary | Unset
        if isinstance(_reservations_summary,  Unset):
            reservations_summary = UNSET
        else:
            reservations_summary = GuestReservationsSummary.from_dict(_reservations_summary)




        guest_profile = cls(
            id=id,
            display_name=display_name,
            display_name_long=display_name_long,
            avatar_url=avatar_url,
            language=language,
            country=country,
            phone=phone,
            email=email,
            total_reservations=total_reservations,
            total_revenue=total_revenue,
            currency=currency,
            is_blacklisted=is_blacklisted,
            blacklisted_reason=blacklisted_reason,
            risk_level=risk_level,
            verification_level=verification_level,
            created_at=created_at,
            contacts=contacts,
            flags=flags,
            notes=notes,
            reservations_summary=reservations_summary,
        )


        guest_profile.additional_properties = d
        return guest_profile

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
