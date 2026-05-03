from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="BulkPricingItem")



@_attrs_define
class BulkPricingItem:
    """ A single (listingId, dates) pair in a bulk pricing request. The action in the parent request body applies to every
    date in `dates` for this listing.

        Attributes:
            listing_id (str):  Example: 4118.
            dates (list[datetime.date]):  Example: ['2026-05-14', '2026-05-15'].
     """

    listing_id: str
    dates: list[datetime.date]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        listing_id = self.listing_id

        dates = []
        for dates_item_data in self.dates:
            dates_item = dates_item_data.isoformat()
            dates.append(dates_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "listingId": listing_id,
            "dates": dates,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        listing_id = d.pop("listingId")

        dates = []
        _dates = d.pop("dates")
        for dates_item_data in (_dates):
            dates_item = isoparse(dates_item_data).date()



            dates.append(dates_item)


        bulk_pricing_item = cls(
            listing_id=listing_id,
            dates=dates,
        )


        bulk_pricing_item.additional_properties = d
        return bulk_pricing_item

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
