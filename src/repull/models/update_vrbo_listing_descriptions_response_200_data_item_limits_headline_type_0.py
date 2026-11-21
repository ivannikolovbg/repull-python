from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="UpdateVrboListingDescriptionsResponse200DataItemLimitsHeadlineType0")



@_attrs_define
class UpdateVrboListingDescriptionsResponse200DataItemLimitsHeadlineType0:
    """ 
        Attributes:
            min_length (int | None | Unset):
            max_length (int | None | Unset):
     """

    min_length: int | None | Unset = UNSET
    max_length: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        min_length: int | None | Unset
        if isinstance(self.min_length, Unset):
            min_length = UNSET
        else:
            min_length = self.min_length

        max_length: int | None | Unset
        if isinstance(self.max_length, Unset):
            max_length = UNSET
        else:
            max_length = self.max_length


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if min_length is not UNSET:
            field_dict["minLength"] = min_length
        if max_length is not UNSET:
            field_dict["maxLength"] = max_length

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_min_length(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_length = _parse_min_length(d.pop("minLength", UNSET))


        def _parse_max_length(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_length = _parse_max_length(d.pop("maxLength", UNSET))


        update_vrbo_listing_descriptions_response_200_data_item_limits_headline_type_0 = cls(
            min_length=min_length,
            max_length=max_length,
        )


        update_vrbo_listing_descriptions_response_200_data_item_limits_headline_type_0.additional_properties = d
        return update_vrbo_listing_descriptions_response_200_data_item_limits_headline_type_0

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
