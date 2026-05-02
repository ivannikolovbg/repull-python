from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.listing_pricing_apply_request_action import ListingPricingApplyRequestAction
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="ListingPricingApplyRequest")



@_attrs_define
class ListingPricingApplyRequest:
    """ 
        Attributes:
            dates (list[datetime.date]): Dates the action applies to. Must match dates that have a `pending` recommendation;
                others are silently skipped.
            action (ListingPricingApplyRequestAction):
     """

    dates: list[datetime.date]
    action: ListingPricingApplyRequestAction
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        dates = []
        for dates_item_data in self.dates:
            dates_item = dates_item_data.isoformat()
            dates.append(dates_item)



        action = self.action.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "dates": dates,
            "action": action,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dates = []
        _dates = d.pop("dates")
        for dates_item_data in (_dates):
            dates_item = isoparse(dates_item_data).date()



            dates.append(dates_item)


        action = ListingPricingApplyRequestAction(d.pop("action"))




        listing_pricing_apply_request = cls(
            dates=dates,
            action=action,
        )


        listing_pricing_apply_request.additional_properties = d
        return listing_pricing_apply_request

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
