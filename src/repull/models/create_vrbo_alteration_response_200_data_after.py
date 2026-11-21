from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CreateVrboAlterationResponse200DataAfter")



@_attrs_define
class CreateVrboAlterationResponse200DataAfter:
    """ 
        Attributes:
            check_in (str | Unset):
            check_out (str | Unset):
            check_in_time (str | Unset):
            check_out_time (str | Unset):
            adults (int | Unset):
            children (int | Unset):
            pets (bool | Unset):
     """

    check_in: str | Unset = UNSET
    check_out: str | Unset = UNSET
    check_in_time: str | Unset = UNSET
    check_out_time: str | Unset = UNSET
    adults: int | Unset = UNSET
    children: int | Unset = UNSET
    pets: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        check_in = self.check_in

        check_out = self.check_out

        check_in_time = self.check_in_time

        check_out_time = self.check_out_time

        adults = self.adults

        children = self.children

        pets = self.pets


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if check_in is not UNSET:
            field_dict["checkIn"] = check_in
        if check_out is not UNSET:
            field_dict["checkOut"] = check_out
        if check_in_time is not UNSET:
            field_dict["checkInTime"] = check_in_time
        if check_out_time is not UNSET:
            field_dict["checkOutTime"] = check_out_time
        if adults is not UNSET:
            field_dict["adults"] = adults
        if children is not UNSET:
            field_dict["children"] = children
        if pets is not UNSET:
            field_dict["pets"] = pets

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        check_in = d.pop("checkIn", UNSET)

        check_out = d.pop("checkOut", UNSET)

        check_in_time = d.pop("checkInTime", UNSET)

        check_out_time = d.pop("checkOutTime", UNSET)

        adults = d.pop("adults", UNSET)

        children = d.pop("children", UNSET)

        pets = d.pop("pets", UNSET)

        create_vrbo_alteration_response_200_data_after = cls(
            check_in=check_in,
            check_out=check_out,
            check_in_time=check_in_time,
            check_out_time=check_out_time,
            adults=adults,
            children=children,
            pets=pets,
        )


        create_vrbo_alteration_response_200_data_after.additional_properties = d
        return create_vrbo_alteration_response_200_data_after

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
