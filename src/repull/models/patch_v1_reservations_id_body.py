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






T = TypeVar("T", bound="PatchV1ReservationsIdBody")



@_attrs_define
class PatchV1ReservationsIdBody:
    """ 
        Attributes:
            check_in (datetime.date | Unset):
            check_out (datetime.date | Unset):
            status (str | Unset):
            total_price (float | Unset):
     """

    check_in: datetime.date | Unset = UNSET
    check_out: datetime.date | Unset = UNSET
    status: str | Unset = UNSET
    total_price: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        check_in: str | Unset = UNSET
        if not isinstance(self.check_in, Unset):
            check_in = self.check_in.isoformat()

        check_out: str | Unset = UNSET
        if not isinstance(self.check_out, Unset):
            check_out = self.check_out.isoformat()

        status = self.status

        total_price = self.total_price


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if check_in is not UNSET:
            field_dict["checkIn"] = check_in
        if check_out is not UNSET:
            field_dict["checkOut"] = check_out
        if status is not UNSET:
            field_dict["status"] = status
        if total_price is not UNSET:
            field_dict["totalPrice"] = total_price

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _check_in = d.pop("checkIn", UNSET)
        check_in: datetime.date | Unset
        if isinstance(_check_in,  Unset):
            check_in = UNSET
        else:
            check_in = isoparse(_check_in).date()




        _check_out = d.pop("checkOut", UNSET)
        check_out: datetime.date | Unset
        if isinstance(_check_out,  Unset):
            check_out = UNSET
        else:
            check_out = isoparse(_check_out).date()




        status = d.pop("status", UNSET)

        total_price = d.pop("totalPrice", UNSET)

        patch_v1_reservations_id_body = cls(
            check_in=check_in,
            check_out=check_out,
            status=status,
            total_price=total_price,
        )


        patch_v1_reservations_id_body.additional_properties = d
        return patch_v1_reservations_id_body

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
