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






T = TypeVar("T", bound="Guest")



@_attrs_define
class Guest:
    """ Guest list-row shape returned by `GET /v1/guests`. Pre-resolved primary phone/email + display name + cumulative stay
    aggregates so list UIs can render without a per-row round-trip.

        Attributes:
            id (int | Unset):
            display_name (str | Unset): Short display name (first name). Example: Jane.
            display_name_long (str | Unset): Long display name (first + last). Falls back to displayName when last name is
                missing. Example: Jane Doe.
            avatar_url (None | str | Unset):
            language (None | str | Unset): Guest's preferred language (ISO 639-1).
            country (None | str | Unset): Guest country (from profile metadata or address).
            phone (None | str | Unset): Primary phone contact (or first non-primary if no primary set).
            email (None | str | Unset): Primary email contact.
            total_reservations (int | Unset): Lifetime reservation count.
            total_revenue (str | Unset): Decimal-as-string to preserve precision across mixed-currency totals. Example:
                14250.00.
            last_stayed_at (datetime.datetime | None | Unset):
            first_stayed_at (datetime.datetime | None | Unset):
            created_at (datetime.datetime | Unset):
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
    last_stayed_at: datetime.datetime | None | Unset = UNSET
    first_stayed_at: datetime.datetime | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
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

        last_stayed_at: None | str | Unset
        if isinstance(self.last_stayed_at, Unset):
            last_stayed_at = UNSET
        elif isinstance(self.last_stayed_at, datetime.datetime):
            last_stayed_at = self.last_stayed_at.isoformat()
        else:
            last_stayed_at = self.last_stayed_at

        first_stayed_at: None | str | Unset
        if isinstance(self.first_stayed_at, Unset):
            first_stayed_at = UNSET
        elif isinstance(self.first_stayed_at, datetime.datetime):
            first_stayed_at = self.first_stayed_at.isoformat()
        else:
            first_stayed_at = self.first_stayed_at

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()


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
        if last_stayed_at is not UNSET:
            field_dict["lastStayedAt"] = last_stayed_at
        if first_stayed_at is not UNSET:
            field_dict["firstStayedAt"] = first_stayed_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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

        def _parse_last_stayed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_stayed_at_type_0 = isoparse(data)



                return last_stayed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_stayed_at = _parse_last_stayed_at(d.pop("lastStayedAt", UNSET))


        def _parse_first_stayed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                first_stayed_at_type_0 = isoparse(data)



                return first_stayed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        first_stayed_at = _parse_first_stayed_at(d.pop("firstStayedAt", UNSET))


        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        guest = cls(
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
            last_stayed_at=last_stayed_at,
            first_stayed_at=first_stayed_at,
            created_at=created_at,
        )


        guest.additional_properties = d
        return guest

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
