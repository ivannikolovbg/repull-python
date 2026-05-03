from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.bulk_pricing_failure_error_code import BulkPricingFailureErrorCode
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="BulkPricingFailure")



@_attrs_define
class BulkPricingFailure:
    """ Per-item failure entry. Per-item failures DO NOT fail the whole batch — partial-success is the norm at this scale.

        Attributes:
            listing_id (str | Unset):
            dates (list[datetime.date] | Unset):
            error_code (BulkPricingFailureErrorCode | Unset):  Example: not_owned.
            error (str | Unset):
     """

    listing_id: str | Unset = UNSET
    dates: list[datetime.date] | Unset = UNSET
    error_code: BulkPricingFailureErrorCode | Unset = UNSET
    error: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        listing_id = self.listing_id

        dates: list[str] | Unset = UNSET
        if not isinstance(self.dates, Unset):
            dates = []
            for dates_item_data in self.dates:
                dates_item = dates_item_data.isoformat()
                dates.append(dates_item)



        error_code: str | Unset = UNSET
        if not isinstance(self.error_code, Unset):
            error_code = self.error_code.value


        error = self.error


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if dates is not UNSET:
            field_dict["dates"] = dates
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        listing_id = d.pop("listingId", UNSET)

        _dates = d.pop("dates", UNSET)
        dates: list[datetime.date] | Unset = UNSET
        if _dates is not UNSET:
            dates = []
            for dates_item_data in _dates:
                dates_item = isoparse(dates_item_data).date()



                dates.append(dates_item)


        _error_code = d.pop("errorCode", UNSET)
        error_code: BulkPricingFailureErrorCode | Unset
        if isinstance(_error_code,  Unset):
            error_code = UNSET
        else:
            error_code = BulkPricingFailureErrorCode(_error_code)




        error = d.pop("error", UNSET)

        bulk_pricing_failure = cls(
            listing_id=listing_id,
            dates=dates,
            error_code=error_code,
            error=error,
        )


        bulk_pricing_failure.additional_properties = d
        return bulk_pricing_failure

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
