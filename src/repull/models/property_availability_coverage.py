from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="PropertyAvailabilityCoverage")



@_attrs_define
class PropertyAvailabilityCoverage:
    """ How much of the requested window we actually hold calendar data for. Read this before treating an absent date as
    bookable — absence means "no data", not "available".

        Attributes:
            requested_days (int): Number of dates in the requested `[from, to]` window, after the 366-day cap. Example: 30.
            covered_days (int): Number of those dates present in `days`. Example: 30.
            missing_dates (list[datetime.date]): Requested dates with no calendar row, ascending. Availability for these
                dates is UNKNOWN — do not treat them as bookable.
     """

    requested_days: int
    covered_days: int
    missing_dates: list[datetime.date]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        requested_days = self.requested_days

        covered_days = self.covered_days

        missing_dates = []
        for missing_dates_item_data in self.missing_dates:
            missing_dates_item = missing_dates_item_data.isoformat()
            missing_dates.append(missing_dates_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "requestedDays": requested_days,
            "coveredDays": covered_days,
            "missingDates": missing_dates,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        requested_days = d.pop("requestedDays")

        covered_days = d.pop("coveredDays")

        missing_dates = []
        _missing_dates = d.pop("missingDates")
        for missing_dates_item_data in (_missing_dates):
            missing_dates_item = isoparse(missing_dates_item_data).date()



            missing_dates.append(missing_dates_item)


        property_availability_coverage = cls(
            requested_days=requested_days,
            covered_days=covered_days,
            missing_dates=missing_dates,
        )


        property_availability_coverage.additional_properties = d
        return property_availability_coverage

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
