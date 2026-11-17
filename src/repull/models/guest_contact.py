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






T = TypeVar("T", bound="GuestContact")



@_attrs_define
class GuestContact:
    """ One contact channel attached to a guest profile (phone, email, etc.).

        Attributes:
            type_ (str | Unset): Contact channel type (`phone`, `email`, etc.). Example: phone.
            value (str | Unset):  Example: +15551234567.
            verified (bool | Unset):
            is_primary (bool | Unset):
            last_used (datetime.datetime | None | Unset):
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
     """

    type_: str | Unset = UNSET
    value: str | Unset = UNSET
    verified: bool | Unset = UNSET
    is_primary: bool | Unset = UNSET
    last_used: datetime.datetime | None | Unset = UNSET
    phone_type: GuestPhoneType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        value = self.value

        verified = self.verified

        is_primary = self.is_primary

        last_used: None | str | Unset
        if isinstance(self.last_used, Unset):
            last_used = UNSET
        elif isinstance(self.last_used, datetime.datetime):
            last_used = self.last_used.isoformat()
        else:
            last_used = self.last_used

        phone_type: str | Unset = UNSET
        if not isinstance(self.phone_type, Unset):
            phone_type = self.phone_type.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if type_ is not UNSET:
            field_dict["type"] = type_
        if value is not UNSET:
            field_dict["value"] = value
        if verified is not UNSET:
            field_dict["verified"] = verified
        if is_primary is not UNSET:
            field_dict["isPrimary"] = is_primary
        if last_used is not UNSET:
            field_dict["lastUsed"] = last_used
        if phone_type is not UNSET:
            field_dict["phoneType"] = phone_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        value = d.pop("value", UNSET)

        verified = d.pop("verified", UNSET)

        is_primary = d.pop("isPrimary", UNSET)

        def _parse_last_used(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_used_type_0 = isoparse(data)



                return last_used_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_used = _parse_last_used(d.pop("lastUsed", UNSET))


        _phone_type = d.pop("phoneType", UNSET)
        phone_type: GuestPhoneType | Unset
        if isinstance(_phone_type,  Unset):
            phone_type = UNSET
        else:
            phone_type = GuestPhoneType(_phone_type)




        guest_contact = cls(
            type_=type_,
            value=value,
            verified=verified,
            is_primary=is_primary,
            last_used=last_used,
            phone_type=phone_type,
        )


        guest_contact.additional_properties = d
        return guest_contact

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
