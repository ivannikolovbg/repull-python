from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.property_availability_day import PropertyAvailabilityDay





T = TypeVar("T", bound="PropertyAvailability")



@_attrs_define
class PropertyAvailability:
    """ Channel-agnostic availability calendar for a property over the requested window. Every date in `[from, to]`
    (inclusive) is present in `days`; dates with no explicit calendar row fall back to available at the default price.

        Attributes:
            property_id (str): Repull property id (equal to `listings.id`), emitted as a string like every other id in the
                API. Example: 4118.
            currency (str): ISO 4217 currency code for the nightly prices in `days`. Example: USD.
            days (list[PropertyAvailabilityDay]): Dense per-date calendar for the requested window (capped at 366 days),
                ordered ascending by date.
     """

    property_id: str
    currency: str
    days: list[PropertyAvailabilityDay]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.property_availability_day import PropertyAvailabilityDay
        property_id = self.property_id

        currency = self.currency

        days = []
        for days_item_data in self.days:
            days_item = days_item_data.to_dict()
            days.append(days_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "propertyId": property_id,
            "currency": currency,
            "days": days,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.property_availability_day import PropertyAvailabilityDay
        d = dict(src_dict)
        property_id = d.pop("propertyId")

        currency = d.pop("currency")

        days = []
        _days = d.pop("days")
        for days_item_data in (_days):
            days_item = PropertyAvailabilityDay.from_dict(days_item_data)



            days.append(days_item)


        property_availability = cls(
            property_id=property_id,
            currency=currency,
            days=days,
        )


        property_availability.additional_properties = d
        return property_availability

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
