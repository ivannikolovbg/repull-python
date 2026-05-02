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






T = TypeVar("T", bound="ListingCompNightly")



@_attrs_define
class ListingCompNightly:
    """ 
        Attributes:
            date (datetime.date | Unset):
            rate (float | None | Unset):
            available (bool | Unset):
     """

    date: datetime.date | Unset = UNSET
    rate: float | None | Unset = UNSET
    available: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        rate: float | None | Unset
        if isinstance(self.rate, Unset):
            rate = UNSET
        else:
            rate = self.rate

        available = self.available


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if date is not UNSET:
            field_dict["date"] = date
        if rate is not UNSET:
            field_dict["rate"] = rate
        if available is not UNSET:
            field_dict["available"] = available

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _date = d.pop("date", UNSET)
        date: datetime.date | Unset
        if isinstance(_date,  Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()




        def _parse_rate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        rate = _parse_rate(d.pop("rate", UNSET))


        available = d.pop("available", UNSET)

        listing_comp_nightly = cls(
            date=date,
            rate=rate,
            available=available,
        )


        listing_comp_nightly.additional_properties = d
        return listing_comp_nightly

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
