from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="CreateAirbnbAlterationBody")



@_attrs_define
class CreateAirbnbAlterationBody:
    """ 
        Attributes:
            confirmation_code (str): Airbnb confirmation code of the reservation to alter.
            check_in (datetime.date | Unset): New check-in date (YYYY-MM-DD).
            check_out (datetime.date | Unset): New check-out date (YYYY-MM-DD).
            number_of_guests (int | Unset): New guest count.
     """

    confirmation_code: str
    check_in: datetime.date | Unset = UNSET
    check_out: datetime.date | Unset = UNSET
    number_of_guests: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        confirmation_code = self.confirmation_code

        check_in: str | Unset = UNSET
        if not isinstance(self.check_in, Unset):
            check_in = self.check_in.isoformat()

        check_out: str | Unset = UNSET
        if not isinstance(self.check_out, Unset):
            check_out = self.check_out.isoformat()

        number_of_guests = self.number_of_guests


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "confirmation_code": confirmation_code,
        })
        if check_in is not UNSET:
            field_dict["check_in"] = check_in
        if check_out is not UNSET:
            field_dict["check_out"] = check_out
        if number_of_guests is not UNSET:
            field_dict["number_of_guests"] = number_of_guests

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        confirmation_code = d.pop("confirmation_code")

        _check_in = d.pop("check_in", UNSET)
        check_in: datetime.date | Unset
        if isinstance(_check_in,  Unset):
            check_in = UNSET
        else:
            check_in = isoparse(_check_in).date()




        _check_out = d.pop("check_out", UNSET)
        check_out: datetime.date | Unset
        if isinstance(_check_out,  Unset):
            check_out = UNSET
        else:
            check_out = isoparse(_check_out).date()




        number_of_guests = d.pop("number_of_guests", UNSET)

        create_airbnb_alteration_body = cls(
            confirmation_code=confirmation_code,
            check_in=check_in,
            check_out=check_out,
            number_of_guests=number_of_guests,
        )


        create_airbnb_alteration_body.additional_properties = d
        return create_airbnb_alteration_body

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
