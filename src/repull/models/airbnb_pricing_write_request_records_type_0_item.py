from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="AirbnbPricingWriteRequestRecordsType0Item")



@_attrs_define
class AirbnbPricingWriteRequestRecordsType0Item:
    """ 
        Attributes:
            check_in_date (datetime.date):
            guest_count (int):
            los_data (list[list[float]]):
     """

    check_in_date: datetime.date
    guest_count: int
    los_data: list[list[float]]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        check_in_date = self.check_in_date.isoformat()

        guest_count = self.guest_count

        los_data = []
        for los_data_item_data in self.los_data:
            los_data_item = los_data_item_data


            los_data.append(los_data_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "check_in_date": check_in_date,
            "guest_count": guest_count,
            "los_data": los_data,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        check_in_date = isoparse(d.pop("check_in_date")).date()




        guest_count = d.pop("guest_count")

        los_data = []
        _los_data = d.pop("los_data")
        for los_data_item_data in (_los_data):
            los_data_item = cast(list[float], los_data_item_data)

            los_data.append(los_data_item)


        airbnb_pricing_write_request_records_type_0_item = cls(
            check_in_date=check_in_date,
            guest_count=guest_count,
            los_data=los_data,
        )


        airbnb_pricing_write_request_records_type_0_item.additional_properties = d
        return airbnb_pricing_write_request_records_type_0_item

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
