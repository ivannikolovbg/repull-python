from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ListingAddressReadiness")



@_attrs_define
class ListingAddressReadiness:
    """ Whether one channel would accept this listing's postal address, answered WITHOUT attempting a publish.

        Attributes:
            ready (bool | Unset): True when the address satisfies this channel's create preflight. False means a publish
                would be refused for the address alone.
            missing (list[str] | Unset): The address parts still needed, named as the REQUEST fields you send — `street`,
                `city`, `state`, `postalCode` — so the value can be acted on directly. Empty when `ready` is true. Example:
                ['state', 'postalCode'].
            have (str | Unset): The address as currently resolved, for debugging. Example: street=123 Main St, city=Miami
                Beach, state=∅, postalCode=∅, country=US.
     """

    ready: bool | Unset = UNSET
    missing: list[str] | Unset = UNSET
    have: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        ready = self.ready

        missing: list[str] | Unset = UNSET
        if not isinstance(self.missing, Unset):
            missing = self.missing



        have = self.have


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if ready is not UNSET:
            field_dict["ready"] = ready
        if missing is not UNSET:
            field_dict["missing"] = missing
        if have is not UNSET:
            field_dict["have"] = have

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ready = d.pop("ready", UNSET)

        missing = cast(list[str], d.pop("missing", UNSET))


        have = d.pop("have", UNSET)

        listing_address_readiness = cls(
            ready=ready,
            missing=missing,
            have=have,
        )


        listing_address_readiness.additional_properties = d
        return listing_address_readiness

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
