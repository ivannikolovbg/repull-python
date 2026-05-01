from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.post_v1_billing_body_plan import PostV1BillingBodyPlan
from ..types import UNSET, Unset






T = TypeVar("T", bound="PostV1BillingBody")



@_attrs_define
class PostV1BillingBody:
    """ 
        Attributes:
            plan (PostV1BillingBodyPlan | Unset):
     """

    plan: PostV1BillingBodyPlan | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        plan: str | Unset = UNSET
        if not isinstance(self.plan, Unset):
            plan = self.plan.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if plan is not UNSET:
            field_dict["plan"] = plan

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _plan = d.pop("plan", UNSET)
        plan: PostV1BillingBodyPlan | Unset
        if isinstance(_plan,  Unset):
            plan = UNSET
        else:
            plan = PostV1BillingBodyPlan(_plan)




        post_v1_billing_body = cls(
            plan=plan,
        )


        post_v1_billing_body.additional_properties = d
        return post_v1_billing_body

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
