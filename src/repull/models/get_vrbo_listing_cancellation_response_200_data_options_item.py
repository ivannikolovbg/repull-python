from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_vrbo_listing_cancellation_response_200_data_options_item_tiers_item import GetVrboListingCancellationResponse200DataOptionsItemTiersItem





T = TypeVar("T", bound="GetVrboListingCancellationResponse200DataOptionsItem")



@_attrs_define
class GetVrboListingCancellationResponse200DataOptionsItem:
    """ 
        Attributes:
            policy_type (str | Unset):
            tiers (list[GetVrboListingCancellationResponse200DataOptionsItemTiersItem] | Unset):
     """

    policy_type: str | Unset = UNSET
    tiers: list[GetVrboListingCancellationResponse200DataOptionsItemTiersItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_vrbo_listing_cancellation_response_200_data_options_item_tiers_item import GetVrboListingCancellationResponse200DataOptionsItemTiersItem
        policy_type = self.policy_type

        tiers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tiers, Unset):
            tiers = []
            for tiers_item_data in self.tiers:
                tiers_item = tiers_item_data.to_dict()
                tiers.append(tiers_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if policy_type is not UNSET:
            field_dict["policyType"] = policy_type
        if tiers is not UNSET:
            field_dict["tiers"] = tiers

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_vrbo_listing_cancellation_response_200_data_options_item_tiers_item import GetVrboListingCancellationResponse200DataOptionsItemTiersItem
        d = dict(src_dict)
        policy_type = d.pop("policyType", UNSET)

        _tiers = d.pop("tiers", UNSET)
        tiers: list[GetVrboListingCancellationResponse200DataOptionsItemTiersItem] | Unset = UNSET
        if _tiers is not UNSET:
            tiers = []
            for tiers_item_data in _tiers:
                tiers_item = GetVrboListingCancellationResponse200DataOptionsItemTiersItem.from_dict(tiers_item_data)



                tiers.append(tiers_item)


        get_vrbo_listing_cancellation_response_200_data_options_item = cls(
            policy_type=policy_type,
            tiers=tiers,
        )


        get_vrbo_listing_cancellation_response_200_data_options_item.additional_properties = d
        return get_vrbo_listing_cancellation_response_200_data_options_item

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
