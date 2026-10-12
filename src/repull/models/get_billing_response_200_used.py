from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetBillingResponse200Used")



@_attrs_define
class GetBillingResponse200Used:
    """ 
        Attributes:
            monthly_requests (int | Unset):
            daily_requests (int | Unset):
     """

    monthly_requests: int | Unset = UNSET
    daily_requests: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        monthly_requests = self.monthly_requests

        daily_requests = self.daily_requests


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if monthly_requests is not UNSET:
            field_dict["monthlyRequests"] = monthly_requests
        if daily_requests is not UNSET:
            field_dict["dailyRequests"] = daily_requests

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        monthly_requests = d.pop("monthlyRequests", UNSET)

        daily_requests = d.pop("dailyRequests", UNSET)

        get_billing_response_200_used = cls(
            monthly_requests=monthly_requests,
            daily_requests=daily_requests,
        )


        get_billing_response_200_used.additional_properties = d
        return get_billing_response_200_used

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
