from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.bulk_pricing_request_action import BulkPricingRequestAction
from typing import cast

if TYPE_CHECKING:
  from ..models.bulk_pricing_item import BulkPricingItem





T = TypeVar("T", bound="BulkPricingRequest")



@_attrs_define
class BulkPricingRequest:
    """ Body for `POST /v1/listings/pricing/bulk`. Apply or decline pending Atlas pricing recommendations across many
    listings in one call. Capped at 500 items per request — exceeding returns 422.

        Attributes:
            action (BulkPricingRequestAction): `apply` writes the recommended price to each listing's calendar and fans out
                to channels (Airbnb/Booking/VRBO). `decline` marks the recommendations as `declined` so they stop surfacing.
            items (list[BulkPricingItem]):
     """

    action: BulkPricingRequestAction
    items: list[BulkPricingItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.bulk_pricing_item import BulkPricingItem
        action = self.action.value

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "action": action,
            "items": items,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_pricing_item import BulkPricingItem
        d = dict(src_dict)
        action = BulkPricingRequestAction(d.pop("action"))




        items = []
        _items = d.pop("items")
        for items_item_data in (_items):
            items_item = BulkPricingItem.from_dict(items_item_data)



            items.append(items_item)


        bulk_pricing_request = cls(
            action=action,
            items=items,
        )


        bulk_pricing_request.additional_properties = d
        return bulk_pricing_request

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
