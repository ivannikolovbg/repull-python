from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.airbnb_availability_write_request_type import AirbnbAvailabilityWriteRequestType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.airbnb_availability_write_request_rules import AirbnbAvailabilityWriteRequestRules
  from ..models.airbnb_calendar_operation import AirbnbCalendarOperation





T = TypeVar("T", bound="AirbnbAvailabilityWriteRequest")



@_attrs_define
class AirbnbAvailabilityWriteRequest:
    """ Body for `PUT /v1/channels/airbnb/listings/{id}/availability`. `type: "calendar"` carries per-date restrictions
    (min/max nights, closed-to-arrival/departure, stop-sell); `type: "rules"` carries listing-level availability rules
    (default min/max nights, booking lead time, turnover days).

        Attributes:
            type_ (AirbnbAvailabilityWriteRequestType):
            operations (list[AirbnbCalendarOperation] | Unset): Required when `type: "calendar"`. Batch of per-date
                restriction operations.
            rules (AirbnbAvailabilityWriteRequestRules | Unset): Required when `type: "rules"`. Airbnb availability-rules
                object — `default_min_nights`, `default_max_nights`, `booking_lead_time`, `turnover_days`,
                `day_of_week_min_nights`, `seasonal_min_nights`, etc.
     """

    type_: AirbnbAvailabilityWriteRequestType
    operations: list[AirbnbCalendarOperation] | Unset = UNSET
    rules: AirbnbAvailabilityWriteRequestRules | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.airbnb_availability_write_request_rules import AirbnbAvailabilityWriteRequestRules
        from ..models.airbnb_calendar_operation import AirbnbCalendarOperation
        type_ = self.type_.value

        operations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.operations, Unset):
            operations = []
            for operations_item_data in self.operations:
                operations_item = operations_item_data.to_dict()
                operations.append(operations_item)



        rules: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rules, Unset):
            rules = self.rules.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
        })
        if operations is not UNSET:
            field_dict["operations"] = operations
        if rules is not UNSET:
            field_dict["rules"] = rules

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.airbnb_availability_write_request_rules import AirbnbAvailabilityWriteRequestRules
        from ..models.airbnb_calendar_operation import AirbnbCalendarOperation
        d = dict(src_dict)
        type_ = AirbnbAvailabilityWriteRequestType(d.pop("type"))




        _operations = d.pop("operations", UNSET)
        operations: list[AirbnbCalendarOperation] | Unset = UNSET
        if _operations is not UNSET:
            operations = []
            for operations_item_data in _operations:
                operations_item = AirbnbCalendarOperation.from_dict(operations_item_data)



                operations.append(operations_item)


        _rules = d.pop("rules", UNSET)
        rules: AirbnbAvailabilityWriteRequestRules | Unset
        if isinstance(_rules,  Unset):
            rules = UNSET
        else:
            rules = AirbnbAvailabilityWriteRequestRules.from_dict(_rules)




        airbnb_availability_write_request = cls(
            type_=type_,
            operations=operations,
            rules=rules,
        )


        airbnb_availability_write_request.additional_properties = d
        return airbnb_availability_write_request

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
