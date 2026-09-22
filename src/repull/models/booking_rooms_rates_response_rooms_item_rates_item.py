from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="BookingRoomsRatesResponseRoomsItemRatesItem")



@_attrs_define
class BookingRoomsRatesResponseRoomsItemRatesItem:
    """ 
        Attributes:
            rate_id (None | str | Unset): Booking.com rate-plan id — use as `rateId` in an ARI update.
            rate_name (None | str | Unset):
            policy (None | str | Unset): Cancellation policy name.
            policy_id (None | str | Unset):
            max_persons (int | None | Unset): The party size this rate plan prices. A rate amount must be written at this
                number: above it Booking.com declines the price in silence, below it answers 400. Null when `source` is
                `mirror`.
            pricing_type (None | str | Unset): Pricing model: `Standard`, `RLO`, `OBP`, or `LOS`.
            is_child_rate (bool | None | Unset): Whether this rate plan is a derived child rate.
     """

    rate_id: None | str | Unset = UNSET
    rate_name: None | str | Unset = UNSET
    policy: None | str | Unset = UNSET
    policy_id: None | str | Unset = UNSET
    max_persons: int | None | Unset = UNSET
    pricing_type: None | str | Unset = UNSET
    is_child_rate: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        rate_id: None | str | Unset
        if isinstance(self.rate_id, Unset):
            rate_id = UNSET
        else:
            rate_id = self.rate_id

        rate_name: None | str | Unset
        if isinstance(self.rate_name, Unset):
            rate_name = UNSET
        else:
            rate_name = self.rate_name

        policy: None | str | Unset
        if isinstance(self.policy, Unset):
            policy = UNSET
        else:
            policy = self.policy

        policy_id: None | str | Unset
        if isinstance(self.policy_id, Unset):
            policy_id = UNSET
        else:
            policy_id = self.policy_id

        max_persons: int | None | Unset
        if isinstance(self.max_persons, Unset):
            max_persons = UNSET
        else:
            max_persons = self.max_persons

        pricing_type: None | str | Unset
        if isinstance(self.pricing_type, Unset):
            pricing_type = UNSET
        else:
            pricing_type = self.pricing_type

        is_child_rate: bool | None | Unset
        if isinstance(self.is_child_rate, Unset):
            is_child_rate = UNSET
        else:
            is_child_rate = self.is_child_rate


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if rate_id is not UNSET:
            field_dict["rateId"] = rate_id
        if rate_name is not UNSET:
            field_dict["rateName"] = rate_name
        if policy is not UNSET:
            field_dict["policy"] = policy
        if policy_id is not UNSET:
            field_dict["policyId"] = policy_id
        if max_persons is not UNSET:
            field_dict["maxPersons"] = max_persons
        if pricing_type is not UNSET:
            field_dict["pricingType"] = pricing_type
        if is_child_rate is not UNSET:
            field_dict["isChildRate"] = is_child_rate

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_rate_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rate_id = _parse_rate_id(d.pop("rateId", UNSET))


        def _parse_rate_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rate_name = _parse_rate_name(d.pop("rateName", UNSET))


        def _parse_policy(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        policy = _parse_policy(d.pop("policy", UNSET))


        def _parse_policy_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        policy_id = _parse_policy_id(d.pop("policyId", UNSET))


        def _parse_max_persons(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_persons = _parse_max_persons(d.pop("maxPersons", UNSET))


        def _parse_pricing_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pricing_type = _parse_pricing_type(d.pop("pricingType", UNSET))


        def _parse_is_child_rate(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_child_rate = _parse_is_child_rate(d.pop("isChildRate", UNSET))


        booking_rooms_rates_response_rooms_item_rates_item = cls(
            rate_id=rate_id,
            rate_name=rate_name,
            policy=policy,
            policy_id=policy_id,
            max_persons=max_persons,
            pricing_type=pricing_type,
            is_child_rate=is_child_rate,
        )


        booking_rooms_rates_response_rooms_item_rates_item.additional_properties = d
        return booking_rooms_rates_response_rooms_item_rates_item

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
