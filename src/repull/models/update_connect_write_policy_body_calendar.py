from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UpdateConnectWritePolicyBodyCalendar")



@_attrs_define
class UpdateConnectWritePolicyBodyCalendar:
    """ 
        Attributes:
            availability (bool | Unset):
            rates (bool | Unset):
            restrictions (bool | Unset):
     """

    availability: bool | Unset = UNSET
    rates: bool | Unset = UNSET
    restrictions: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        availability = self.availability

        rates = self.rates

        restrictions = self.restrictions


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if availability is not UNSET:
            field_dict["availability"] = availability
        if rates is not UNSET:
            field_dict["rates"] = rates
        if restrictions is not UNSET:
            field_dict["restrictions"] = restrictions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        availability = d.pop("availability", UNSET)

        rates = d.pop("rates", UNSET)

        restrictions = d.pop("restrictions", UNSET)

        update_connect_write_policy_body_calendar = cls(
            availability=availability,
            rates=rates,
            restrictions=restrictions,
        )


        update_connect_write_policy_body_calendar.additional_properties = d
        return update_connect_write_policy_body_calendar

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
