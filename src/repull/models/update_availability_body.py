from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.calendar_day import CalendarDay





T = TypeVar("T", bound="UpdateAvailabilityBody")



@_attrs_define
class UpdateAvailabilityBody:
    """ 
        Attributes:
            dates (list[CalendarDay] | Unset):
     """

    dates: list[CalendarDay] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.calendar_day import CalendarDay
        dates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.dates, Unset):
            dates = []
            for dates_item_data in self.dates:
                dates_item = dates_item_data.to_dict()
                dates.append(dates_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if dates is not UNSET:
            field_dict["dates"] = dates

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.calendar_day import CalendarDay
        d = dict(src_dict)
        _dates = d.pop("dates", UNSET)
        dates: list[CalendarDay] | Unset = UNSET
        if _dates is not UNSET:
            dates = []
            for dates_item_data in _dates:
                dates_item = CalendarDay.from_dict(dates_item_data)



                dates.append(dates_item)


        update_availability_body = cls(
            dates=dates,
        )


        update_availability_body.additional_properties = d
        return update_availability_body

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
