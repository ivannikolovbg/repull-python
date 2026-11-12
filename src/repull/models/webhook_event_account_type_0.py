from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="WebhookEventAccountType0")



@_attrs_define
class WebhookEventAccountType0:
    """ Which connected account produced this event. Null when it cannot be resolved — present-but-null rather than omitted,
    so a receiver can tell "unresolvable" from "an old event".

        Attributes:
            id (int | None | Unset): Our connection record id: the `X-Account-Id` value, the same as `account.id`. `null`
                only when the account has no connection record (e.g. a Vrbo sign-in in a workspace with no Vrbo connection).
                Example: 135.
            provider (None | str | Unset):  Example: airbnb.
            external_account_id (None | str | Unset): The platform's own account id: Airbnb host id; Booking.com hotel id
                (`booking`); the Booking.com account id behind the Extranet login (`booking_extranet`); Vrbo's account id
                (`vrbo`); the PMS's own account or company id. `null` when the platform id is not known yet (a Vrbo sign-in
                before its account id is captured, a PMS that does not expose one); never a Repull id. Example: 79730216.
     """

    id: int | None | Unset = UNSET
    provider: None | str | Unset = UNSET
    external_account_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id: int | None | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        provider: None | str | Unset
        if isinstance(self.provider, Unset):
            provider = UNSET
        else:
            provider = self.provider

        external_account_id: None | str | Unset
        if isinstance(self.external_account_id, Unset):
            external_account_id = UNSET
        else:
            external_account_id = self.external_account_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if provider is not UNSET:
            field_dict["provider"] = provider
        if external_account_id is not UNSET:
            field_dict["externalAccountId"] = external_account_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        id = _parse_id(d.pop("id", UNSET))


        def _parse_provider(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider = _parse_provider(d.pop("provider", UNSET))


        def _parse_external_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_account_id = _parse_external_account_id(d.pop("externalAccountId", UNSET))


        webhook_event_account_type_0 = cls(
            id=id,
            provider=provider,
            external_account_id=external_account_id,
        )


        webhook_event_account_type_0.additional_properties = d
        return webhook_event_account_type_0

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
