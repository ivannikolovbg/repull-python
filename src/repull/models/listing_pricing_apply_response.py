from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ListingPricingApplyResponse")



@_attrs_define
class ListingPricingApplyResponse:
    """ 
        Attributes:
            ok (bool | Unset):
            applied (int | None | Unset): Number of recommendations applied (apply action only).
            declined (int | None | Unset): Number of dates declined (decline action only).
     """

    ok: bool | Unset = UNSET
    applied: int | None | Unset = UNSET
    declined: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        ok = self.ok

        applied: int | None | Unset
        if isinstance(self.applied, Unset):
            applied = UNSET
        else:
            applied = self.applied

        declined: int | None | Unset
        if isinstance(self.declined, Unset):
            declined = UNSET
        else:
            declined = self.declined


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if ok is not UNSET:
            field_dict["ok"] = ok
        if applied is not UNSET:
            field_dict["applied"] = applied
        if declined is not UNSET:
            field_dict["declined"] = declined

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ok = d.pop("ok", UNSET)

        def _parse_applied(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        applied = _parse_applied(d.pop("applied", UNSET))


        def _parse_declined(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        declined = _parse_declined(d.pop("declined", UNSET))


        listing_pricing_apply_response = cls(
            ok=ok,
            applied=applied,
            declined=declined,
        )


        listing_pricing_apply_response.additional_properties = d
        return listing_pricing_apply_response

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
