from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.booking_occupancy_rule import BookingOccupancyRule





T = TypeVar("T", bound="BookingDerivedPricingWriteResponseRatesItem")



@_attrs_define
class BookingDerivedPricingWriteResponseRatesItem:
    """ 
        Attributes:
            room_id (str | Unset):
            rate_id (str | Unset):
            leading_occupancy (int | Unset):
            occupancies (list[BookingOccupancyRule] | Unset):
     """

    room_id: str | Unset = UNSET
    rate_id: str | Unset = UNSET
    leading_occupancy: int | Unset = UNSET
    occupancies: list[BookingOccupancyRule] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.booking_occupancy_rule import BookingOccupancyRule
        room_id = self.room_id

        rate_id = self.rate_id

        leading_occupancy = self.leading_occupancy

        occupancies: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.occupancies, Unset):
            occupancies = []
            for occupancies_item_data in self.occupancies:
                occupancies_item = occupancies_item_data.to_dict()
                occupancies.append(occupancies_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if room_id is not UNSET:
            field_dict["roomId"] = room_id
        if rate_id is not UNSET:
            field_dict["rateId"] = rate_id
        if leading_occupancy is not UNSET:
            field_dict["leadingOccupancy"] = leading_occupancy
        if occupancies is not UNSET:
            field_dict["occupancies"] = occupancies

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.booking_occupancy_rule import BookingOccupancyRule
        d = dict(src_dict)
        room_id = d.pop("roomId", UNSET)

        rate_id = d.pop("rateId", UNSET)

        leading_occupancy = d.pop("leadingOccupancy", UNSET)

        _occupancies = d.pop("occupancies", UNSET)
        occupancies: list[BookingOccupancyRule] | Unset = UNSET
        if _occupancies is not UNSET:
            occupancies = []
            for occupancies_item_data in _occupancies:
                occupancies_item = BookingOccupancyRule.from_dict(occupancies_item_data)



                occupancies.append(occupancies_item)


        booking_derived_pricing_write_response_rates_item = cls(
            room_id=room_id,
            rate_id=rate_id,
            leading_occupancy=leading_occupancy,
            occupancies=occupancies,
        )


        booking_derived_pricing_write_response_rates_item.additional_properties = d
        return booking_derived_pricing_write_response_rates_item

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
