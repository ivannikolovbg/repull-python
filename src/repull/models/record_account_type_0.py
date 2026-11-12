from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="RecordAccountType0")



@_attrs_define
class RecordAccountType0:
    """ The connected account a record belongs to — keyed exactly like the webhook `account` block and
    `connect.session.completed`, so one `provider:externalAccountId` key routes reads and events to the same user.
    `null` when it cannot be resolved (never guessed). Until 2027-02-12 the `?account=` filter and connection handles
    also accept the old Extranet / Vrbo login ids (e.g. `booking_extranet:88`); they are never sent.

        Attributes:
            provider (str | Unset): airbnb, booking, booking_extranet, vrbo, or the PMS id (hostaway, cloudbeds, …).
                Example: airbnb.
            external_account_id (None | str | Unset): The platform's own account id: Airbnb host id; Booking.com hotel id
                (`booking`); the Booking.com account id behind the Extranet login (`booking_extranet`); Vrbo's account id
                (`vrbo`); the PMS's own account or company id. `null` when the platform id is not known yet (a Vrbo sign-in
                before its account id is captured, a PMS that does not expose one); never a Repull id. Example: 79730216.
            connection_id (None | str | Unset): Our connection record id: the `X-Account-Id` value, the same as
                `account.id`. `null` only when the account has no connection record (e.g. a Vrbo sign-in in a workspace with no
                Vrbo connection). A string, like every id in API responses. Example: 126.
            hotel_id (str | Unset): Booking.com only: the hotel (property) id the record belongs to. A `booking_extranet`
                account (a Booking.com account) can cover several hotels; this says which one. Example: 10433861.
     """

    provider: str | Unset = UNSET
    external_account_id: None | str | Unset = UNSET
    connection_id: None | str | Unset = UNSET
    hotel_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        provider = self.provider

        external_account_id: None | str | Unset
        if isinstance(self.external_account_id, Unset):
            external_account_id = UNSET
        else:
            external_account_id = self.external_account_id

        connection_id: None | str | Unset
        if isinstance(self.connection_id, Unset):
            connection_id = UNSET
        else:
            connection_id = self.connection_id

        hotel_id = self.hotel_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if provider is not UNSET:
            field_dict["provider"] = provider
        if external_account_id is not UNSET:
            field_dict["externalAccountId"] = external_account_id
        if connection_id is not UNSET:
            field_dict["connectionId"] = connection_id
        if hotel_id is not UNSET:
            field_dict["hotelId"] = hotel_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        provider = d.pop("provider", UNSET)

        def _parse_external_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_account_id = _parse_external_account_id(d.pop("externalAccountId", UNSET))


        def _parse_connection_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        connection_id = _parse_connection_id(d.pop("connectionId", UNSET))


        hotel_id = d.pop("hotelId", UNSET)

        record_account_type_0 = cls(
            provider=provider,
            external_account_id=external_account_id,
            connection_id=connection_id,
            hotel_id=hotel_id,
        )


        record_account_type_0.additional_properties = d
        return record_account_type_0

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
