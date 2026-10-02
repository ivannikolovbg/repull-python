from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.reservation_capabilities_managed_by import ReservationCapabilitiesManagedBy
from ..models.reservation_capabilities_verified_against import ReservationCapabilitiesVerifiedAgainst
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ReservationCapabilities")



@_attrs_define
class ReservationCapabilities:
    """ Which reservation writes the API performs for this listing (or, on `GET /v1/connect/{provider}`, for any listing of
    that connection). Derived from the PMS connector, the connection, and its write policy — a flag is true only when
    all three allow it.

        Attributes:
            managed_by (ReservationCapabilitiesManagedBy | Unset): `pms` — booked in the connected PMS; `repull` — a direct
                booking made in Repull.
            provider (None | str | Unset):  Example: hostaway.
            create (bool | Unset): `POST /v1/reservations`.
            modify (bool | Unset): `PATCH /v1/reservations/{id}`.
            cancel (bool | Unset): `POST /v1/reservations/{id}/cancel`.
            quote (bool | Unset): `POST /v1/reservations/quote`.
            custom_price (bool | Unset): `totalPrice` on create is honoured; otherwise the PMS (or the rate engine) prices
                the stay.
            notes (str | Unset): What the flags do not say: limits, required access, and why something is off.
            verified_against (ReservationCapabilitiesVerifiedAgainst | Unset): `sandbox` — run end to end on the vendor
                sandbox (Mews, Cloudbeds); `vendor_docs` — verified against the vendor's API documentation only. Null for direct
                bookings.
     """

    managed_by: ReservationCapabilitiesManagedBy | Unset = UNSET
    provider: None | str | Unset = UNSET
    create: bool | Unset = UNSET
    modify: bool | Unset = UNSET
    cancel: bool | Unset = UNSET
    quote: bool | Unset = UNSET
    custom_price: bool | Unset = UNSET
    notes: str | Unset = UNSET
    verified_against: ReservationCapabilitiesVerifiedAgainst | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        managed_by: str | Unset = UNSET
        if not isinstance(self.managed_by, Unset):
            managed_by = self.managed_by.value


        provider: None | str | Unset
        if isinstance(self.provider, Unset):
            provider = UNSET
        else:
            provider = self.provider

        create = self.create

        modify = self.modify

        cancel = self.cancel

        quote = self.quote

        custom_price = self.custom_price

        notes = self.notes

        verified_against: str | Unset = UNSET
        if not isinstance(self.verified_against, Unset):
            verified_against = self.verified_against.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if managed_by is not UNSET:
            field_dict["managedBy"] = managed_by
        if provider is not UNSET:
            field_dict["provider"] = provider
        if create is not UNSET:
            field_dict["create"] = create
        if modify is not UNSET:
            field_dict["modify"] = modify
        if cancel is not UNSET:
            field_dict["cancel"] = cancel
        if quote is not UNSET:
            field_dict["quote"] = quote
        if custom_price is not UNSET:
            field_dict["customPrice"] = custom_price
        if notes is not UNSET:
            field_dict["notes"] = notes
        if verified_against is not UNSET:
            field_dict["verifiedAgainst"] = verified_against

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _managed_by = d.pop("managedBy", UNSET)
        managed_by: ReservationCapabilitiesManagedBy | Unset
        if isinstance(_managed_by,  Unset):
            managed_by = UNSET
        else:
            managed_by = ReservationCapabilitiesManagedBy(_managed_by)




        def _parse_provider(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider = _parse_provider(d.pop("provider", UNSET))


        create = d.pop("create", UNSET)

        modify = d.pop("modify", UNSET)

        cancel = d.pop("cancel", UNSET)

        quote = d.pop("quote", UNSET)

        custom_price = d.pop("customPrice", UNSET)

        notes = d.pop("notes", UNSET)

        _verified_against = d.pop("verifiedAgainst", UNSET)
        verified_against: ReservationCapabilitiesVerifiedAgainst | Unset
        if isinstance(_verified_against,  Unset):
            verified_against = UNSET
        else:
            verified_against = ReservationCapabilitiesVerifiedAgainst(_verified_against)




        reservation_capabilities = cls(
            managed_by=managed_by,
            provider=provider,
            create=create,
            modify=modify,
            cancel=cancel,
            quote=quote,
            custom_price=custom_price,
            notes=notes,
            verified_against=verified_against,
        )


        reservation_capabilities.additional_properties = d
        return reservation_capabilities

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
