from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="VrboListingActionResponse200UnitsItem")



@_attrs_define
class VrboListingActionResponse200UnitsItem:
    """ 
        Attributes:
            vrbo_listing_number (str | Unset):
            live (bool | Unset):
            ok (bool | Unset):
            verified (bool | Unset):
            code (str | Unset):
            message (str | Unset):
     """

    vrbo_listing_number: str | Unset = UNSET
    live: bool | Unset = UNSET
    ok: bool | Unset = UNSET
    verified: bool | Unset = UNSET
    code: str | Unset = UNSET
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        vrbo_listing_number = self.vrbo_listing_number

        live = self.live

        ok = self.ok

        verified = self.verified

        code = self.code

        message = self.message


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if vrbo_listing_number is not UNSET:
            field_dict["vrboListingNumber"] = vrbo_listing_number
        if live is not UNSET:
            field_dict["live"] = live
        if ok is not UNSET:
            field_dict["ok"] = ok
        if verified is not UNSET:
            field_dict["verified"] = verified
        if code is not UNSET:
            field_dict["code"] = code
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        vrbo_listing_number = d.pop("vrboListingNumber", UNSET)

        live = d.pop("live", UNSET)

        ok = d.pop("ok", UNSET)

        verified = d.pop("verified", UNSET)

        code = d.pop("code", UNSET)

        message = d.pop("message", UNSET)

        vrbo_listing_action_response_200_units_item = cls(
            vrbo_listing_number=vrbo_listing_number,
            live=live,
            ok=ok,
            verified=verified,
            code=code,
            message=message,
        )


        vrbo_listing_action_response_200_units_item.additional_properties = d
        return vrbo_listing_action_response_200_units_item

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
