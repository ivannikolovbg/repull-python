from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="PmsWritePolicyCalendar")



@_attrs_define
class PmsWritePolicyCalendar:
    """ 
        Attributes:
            availability (bool): Open and close nights. Off also means the PMS's bookings never block the calendar on other
                channels.
            rates (bool): Nightly prices.
            restrictions (bool): Minimum stay and other stay restrictions.
     """

    availability: bool
    rates: bool
    restrictions: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        availability = self.availability

        rates = self.rates

        restrictions = self.restrictions


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "availability": availability,
            "rates": rates,
            "restrictions": restrictions,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        availability = d.pop("availability")

        rates = d.pop("rates")

        restrictions = d.pop("restrictions")

        pms_write_policy_calendar = cls(
            availability=availability,
            rates=rates,
            restrictions=restrictions,
        )


        pms_write_policy_calendar.additional_properties = d
        return pms_write_policy_calendar

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
