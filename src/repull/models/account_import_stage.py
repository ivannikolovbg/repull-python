from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AccountImportStage")



@_attrs_define
class AccountImportStage:
    """ One stage of an account import (e.g. `reservations`). The stage is done when `done + failed` reaches `expected`.

        Attributes:
            name (str | Unset):  Example: reservations.
            expected (int | None | Unset): Units of work in this stage (one per page, chunk, listing or thread, depending on
                the channel). `null` until the stage knows its size.
            done (int | Unset):
            failed (int | Unset):
     """

    name: str | Unset = UNSET
    expected: int | None | Unset = UNSET
    done: int | Unset = UNSET
    failed: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        expected: int | None | Unset
        if isinstance(self.expected, Unset):
            expected = UNSET
        else:
            expected = self.expected

        done = self.done

        failed = self.failed


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if expected is not UNSET:
            field_dict["expected"] = expected
        if done is not UNSET:
            field_dict["done"] = done
        if failed is not UNSET:
            field_dict["failed"] = failed

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_expected(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        expected = _parse_expected(d.pop("expected", UNSET))


        done = d.pop("done", UNSET)

        failed = d.pop("failed", UNSET)

        account_import_stage = cls(
            name=name,
            expected=expected,
            done=done,
            failed=failed,
        )


        account_import_stage.additional_properties = d
        return account_import_stage

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
