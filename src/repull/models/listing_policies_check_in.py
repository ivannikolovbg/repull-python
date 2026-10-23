from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ListingPoliciesCheckIn")



@_attrs_define
class ListingPoliciesCheckIn:
    """ 
        Attributes:
            method (None | str | Unset): `lockbox`, `smartlock`, `keypad`, `doorman`, `host_greets`, `building_staff`,
                `other`. Example: lockbox.
            instructions (None | str | Unset):
            from_ (None | str | Unset):  Example: 15:00.
            until (None | str | Unset):  Example: 22:00.
     """

    method: None | str | Unset = UNSET
    instructions: None | str | Unset = UNSET
    from_: None | str | Unset = UNSET
    until: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        method: None | str | Unset
        if isinstance(self.method, Unset):
            method = UNSET
        else:
            method = self.method

        instructions: None | str | Unset
        if isinstance(self.instructions, Unset):
            instructions = UNSET
        else:
            instructions = self.instructions

        from_: None | str | Unset
        if isinstance(self.from_, Unset):
            from_ = UNSET
        else:
            from_ = self.from_

        until: None | str | Unset
        if isinstance(self.until, Unset):
            until = UNSET
        else:
            until = self.until


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if method is not UNSET:
            field_dict["method"] = method
        if instructions is not UNSET:
            field_dict["instructions"] = instructions
        if from_ is not UNSET:
            field_dict["from"] = from_
        if until is not UNSET:
            field_dict["until"] = until

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_method(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        method = _parse_method(d.pop("method", UNSET))


        def _parse_instructions(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        instructions = _parse_instructions(d.pop("instructions", UNSET))


        def _parse_from_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        from_ = _parse_from_(d.pop("from", UNSET))


        def _parse_until(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        until = _parse_until(d.pop("until", UNSET))


        listing_policies_check_in = cls(
            method=method,
            instructions=instructions,
            from_=from_,
            until=until,
        )


        listing_policies_check_in.additional_properties = d
        return listing_policies_check_in

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
