from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.guest_phone_type import GuestPhoneType
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="ReservationPrimaryGuest")



@_attrs_define
class ReservationPrimaryGuest:
    """ Inline guest summary resolved by JOIN-ing the `guests` table. Populated for every reservation that has a linked
    guest row; OMITTED entirely (not null) for owner-blocks / pre-arrival rows / partial-sync gaps. Always optional-
    chain in SDK consumers.

        Attributes:
            id (str | Unset): Internal Repull guest ID. Use `GET /v1/guests/{id}` for the full profile.
            first_name (None | str | Unset):
            last_name (None | str | Unset):
            email (None | str | Unset): Primary email contact (or first non-primary if no primary set).
            phone (None | str | Unset): Primary phone contact (or first non-primary if no primary set). For an Airbnb stay
                this may be an Airbnb relay number — check `phoneType`.
            phone_type (GuestPhoneType | Unset): Whether `phone` is the guest's own number or an Airbnb relay number. Since
                late October 2026 Airbnb never shares a guest's real phone number. For an Airbnb stay where the listing, host
                and guest are all in the same country and that country is the US or Canada, Airbnb gives a temporary relay
                number instead (`airbnb_relay`); every other Airbnb stay has no phone at all. A relay number forwards SMS only
                (no MMS, RCS or images; about 1,000 characters including Airbnb's prefix, not split). It stops working 48 hours
                after checkout or when the reservation is cancelled, and it can change during the stay without a reservation
                webhook (re-read the reservation for the current one). The same relay number is used for other guests of other
                hosts, so never use it to identify or match a guest. Texting from a number Airbnb does not know: the first
                message must be the reservation's confirmation code (for example `HM12345678`); text from the host's Airbnb
                contact number for automatic delivery. `guest` means the number as the channel or the host recorded it. Example:
                airbnb_relay.
            phone_expires_at (datetime.datetime | None | Unset): Only next to an Airbnb relay number: when it stops working
                (checkout + 48 hours). `null` when Airbnb did not give the checkout time with its offset. A cancelled
                reservation's relay number stops working at cancellation, whatever this says. Example: 2026-11-22T16:00:00.000Z.
            language (None | str | Unset): Guest's preferred language (BCP-47 / ISO 639-1).
     """

    id: str | Unset = UNSET
    first_name: None | str | Unset = UNSET
    last_name: None | str | Unset = UNSET
    email: None | str | Unset = UNSET
    phone: None | str | Unset = UNSET
    phone_type: GuestPhoneType | Unset = UNSET
    phone_expires_at: datetime.datetime | None | Unset = UNSET
    language: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        first_name: None | str | Unset
        if isinstance(self.first_name, Unset):
            first_name = UNSET
        else:
            first_name = self.first_name

        last_name: None | str | Unset
        if isinstance(self.last_name, Unset):
            last_name = UNSET
        else:
            last_name = self.last_name

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        phone: None | str | Unset
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        phone_type: str | Unset = UNSET
        if not isinstance(self.phone_type, Unset):
            phone_type = self.phone_type.value


        phone_expires_at: None | str | Unset
        if isinstance(self.phone_expires_at, Unset):
            phone_expires_at = UNSET
        elif isinstance(self.phone_expires_at, datetime.datetime):
            phone_expires_at = self.phone_expires_at.isoformat()
        else:
            phone_expires_at = self.phone_expires_at

        language: None | str | Unset
        if isinstance(self.language, Unset):
            language = UNSET
        else:
            language = self.language


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
        if email is not UNSET:
            field_dict["email"] = email
        if phone is not UNSET:
            field_dict["phone"] = phone
        if phone_type is not UNSET:
            field_dict["phoneType"] = phone_type
        if phone_expires_at is not UNSET:
            field_dict["phoneExpiresAt"] = phone_expires_at
        if language is not UNSET:
            field_dict["language"] = language

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_first_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        first_name = _parse_first_name(d.pop("firstName", UNSET))


        def _parse_last_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_name = _parse_last_name(d.pop("lastName", UNSET))


        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))


        def _parse_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone = _parse_phone(d.pop("phone", UNSET))


        _phone_type = d.pop("phoneType", UNSET)
        phone_type: GuestPhoneType | Unset
        if isinstance(_phone_type,  Unset):
            phone_type = UNSET
        else:
            phone_type = GuestPhoneType(_phone_type)




        def _parse_phone_expires_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                phone_expires_at_type_0 = isoparse(data)



                return phone_expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        phone_expires_at = _parse_phone_expires_at(d.pop("phoneExpiresAt", UNSET))


        def _parse_language(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        language = _parse_language(d.pop("language", UNSET))


        reservation_primary_guest = cls(
            id=id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            phone_type=phone_type,
            phone_expires_at=phone_expires_at,
            language=language,
        )


        reservation_primary_guest.additional_properties = d
        return reservation_primary_guest

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
