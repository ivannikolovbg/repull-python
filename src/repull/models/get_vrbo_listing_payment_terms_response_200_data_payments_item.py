from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetVrboListingPaymentTermsResponse200DataPaymentsItem")



@_attrs_define
class GetVrboListingPaymentTermsResponse200DataPaymentsItem:
    """ 
        Attributes:
            percent (float | Unset):
            days_before_arrival (int | Unset):
     """

    percent: float | Unset = UNSET
    days_before_arrival: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        percent = self.percent

        days_before_arrival = self.days_before_arrival


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if percent is not UNSET:
            field_dict["percent"] = percent
        if days_before_arrival is not UNSET:
            field_dict["daysBeforeArrival"] = days_before_arrival

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        percent = d.pop("percent", UNSET)

        days_before_arrival = d.pop("daysBeforeArrival", UNSET)

        get_vrbo_listing_payment_terms_response_200_data_payments_item = cls(
            percent=percent,
            days_before_arrival=days_before_arrival,
        )


        get_vrbo_listing_payment_terms_response_200_data_payments_item.additional_properties = d
        return get_vrbo_listing_payment_terms_response_200_data_payments_item

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
