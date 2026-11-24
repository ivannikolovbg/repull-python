from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="TiketRatePlan")



@_attrs_define
class TiketRatePlan:
    """ 
        Attributes:
            rate_plan_id (str | Unset): Repull id of the rate plan (used by `set-push-rate-plans`).
            rate_plan_code (str | Unset): tiket.com rate plan id.
            name (None | str | Unset):
            push_target (bool | Unset): Prices and restrictions from the mapped listing's calendar are sent to this rate
                plan.
     """

    rate_plan_id: str | Unset = UNSET
    rate_plan_code: str | Unset = UNSET
    name: None | str | Unset = UNSET
    push_target: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        rate_plan_id = self.rate_plan_id

        rate_plan_code = self.rate_plan_code

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        push_target = self.push_target


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if rate_plan_id is not UNSET:
            field_dict["ratePlanId"] = rate_plan_id
        if rate_plan_code is not UNSET:
            field_dict["ratePlanCode"] = rate_plan_code
        if name is not UNSET:
            field_dict["name"] = name
        if push_target is not UNSET:
            field_dict["pushTarget"] = push_target

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rate_plan_id = d.pop("ratePlanId", UNSET)

        rate_plan_code = d.pop("ratePlanCode", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        push_target = d.pop("pushTarget", UNSET)

        tiket_rate_plan = cls(
            rate_plan_id=rate_plan_id,
            rate_plan_code=rate_plan_code,
            name=name,
            push_target=push_target,
        )


        tiket_rate_plan.additional_properties = d
        return tiket_rate_plan

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
