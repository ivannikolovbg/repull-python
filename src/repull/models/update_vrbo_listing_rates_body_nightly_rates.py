from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UpdateVrboListingRatesBodyNightlyRates")



@_attrs_define
class UpdateVrboListingRatesBodyNightlyRates:
    """ A price per weekday; every weekday in the range needs one.

        Attributes:
            sunday (float | Unset):
            monday (float | Unset):
            tuesday (float | Unset):
            wednesday (float | Unset):
            thursday (float | Unset):
            friday (float | Unset):
            saturday (float | Unset):
     """

    sunday: float | Unset = UNSET
    monday: float | Unset = UNSET
    tuesday: float | Unset = UNSET
    wednesday: float | Unset = UNSET
    thursday: float | Unset = UNSET
    friday: float | Unset = UNSET
    saturday: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        sunday = self.sunday

        monday = self.monday

        tuesday = self.tuesday

        wednesday = self.wednesday

        thursday = self.thursday

        friday = self.friday

        saturday = self.saturday


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if sunday is not UNSET:
            field_dict["sunday"] = sunday
        if monday is not UNSET:
            field_dict["monday"] = monday
        if tuesday is not UNSET:
            field_dict["tuesday"] = tuesday
        if wednesday is not UNSET:
            field_dict["wednesday"] = wednesday
        if thursday is not UNSET:
            field_dict["thursday"] = thursday
        if friday is not UNSET:
            field_dict["friday"] = friday
        if saturday is not UNSET:
            field_dict["saturday"] = saturday

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sunday = d.pop("sunday", UNSET)

        monday = d.pop("monday", UNSET)

        tuesday = d.pop("tuesday", UNSET)

        wednesday = d.pop("wednesday", UNSET)

        thursday = d.pop("thursday", UNSET)

        friday = d.pop("friday", UNSET)

        saturday = d.pop("saturday", UNSET)

        update_vrbo_listing_rates_body_nightly_rates = cls(
            sunday=sunday,
            monday=monday,
            tuesday=tuesday,
            wednesday=wednesday,
            thursday=thursday,
            friday=friday,
            saturday=saturday,
        )

        return update_vrbo_listing_rates_body_nightly_rates

