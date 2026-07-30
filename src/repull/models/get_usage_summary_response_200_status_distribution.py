from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetUsageSummaryResponse200StatusDistribution")



@_attrs_define
class GetUsageSummaryResponse200StatusDistribution:
    """ 
        Attributes:
            field_2xx (int | Unset):
            field_3xx (int | Unset):
            field_4xx (int | Unset):
            field_5xx (int | Unset):
     """

    field_2xx: int | Unset = UNSET
    field_3xx: int | Unset = UNSET
    field_4xx: int | Unset = UNSET
    field_5xx: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        field_2xx = self.field_2xx

        field_3xx = self.field_3xx

        field_4xx = self.field_4xx

        field_5xx = self.field_5xx


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if field_2xx is not UNSET:
            field_dict["2xx"] = field_2xx
        if field_3xx is not UNSET:
            field_dict["3xx"] = field_3xx
        if field_4xx is not UNSET:
            field_dict["4xx"] = field_4xx
        if field_5xx is not UNSET:
            field_dict["5xx"] = field_5xx

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_2xx = d.pop("2xx", UNSET)

        field_3xx = d.pop("3xx", UNSET)

        field_4xx = d.pop("4xx", UNSET)

        field_5xx = d.pop("5xx", UNSET)

        get_usage_summary_response_200_status_distribution = cls(
            field_2xx=field_2xx,
            field_3xx=field_3xx,
            field_4xx=field_4xx,
            field_5xx=field_5xx,
        )


        get_usage_summary_response_200_status_distribution.additional_properties = d
        return get_usage_summary_response_200_status_distribution

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
