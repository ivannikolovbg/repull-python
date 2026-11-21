from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="CreateVrboAlterationResponse200DataDueDate")



@_attrs_define
class CreateVrboAlterationResponse200DataDueDate:
    """ 
        Attributes:
            default (None | str | Unset):
            earliest (None | str | Unset):
            latest (None | str | Unset):
     """

    default: None | str | Unset = UNSET
    earliest: None | str | Unset = UNSET
    latest: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        default: None | str | Unset
        if isinstance(self.default, Unset):
            default = UNSET
        else:
            default = self.default

        earliest: None | str | Unset
        if isinstance(self.earliest, Unset):
            earliest = UNSET
        else:
            earliest = self.earliest

        latest: None | str | Unset
        if isinstance(self.latest, Unset):
            latest = UNSET
        else:
            latest = self.latest


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if default is not UNSET:
            field_dict["default"] = default
        if earliest is not UNSET:
            field_dict["earliest"] = earliest
        if latest is not UNSET:
            field_dict["latest"] = latest

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_default(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default = _parse_default(d.pop("default", UNSET))


        def _parse_earliest(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        earliest = _parse_earliest(d.pop("earliest", UNSET))


        def _parse_latest(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latest = _parse_latest(d.pop("latest", UNSET))


        create_vrbo_alteration_response_200_data_due_date = cls(
            default=default,
            earliest=earliest,
            latest=latest,
        )


        create_vrbo_alteration_response_200_data_due_date.additional_properties = d
        return create_vrbo_alteration_response_200_data_due_date

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
