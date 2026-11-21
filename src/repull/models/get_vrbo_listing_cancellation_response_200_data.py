from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_vrbo_listing_cancellation_response_200_data_options_item import GetVrboListingCancellationResponse200DataOptionsItem
  from ..models.get_vrbo_listing_cancellation_response_200_data_seasonal_item import GetVrboListingCancellationResponse200DataSeasonalItem
  from ..models.get_vrbo_listing_cancellation_response_200_data_tiers_item import GetVrboListingCancellationResponse200DataTiersItem





T = TypeVar("T", bound="GetVrboListingCancellationResponse200Data")



@_attrs_define
class GetVrboListingCancellationResponse200Data:
    """ The section as Vrbo has it.

        Attributes:
            policy_type (None | str | Unset):
            tiers (list[GetVrboListingCancellationResponse200DataTiersItem] | Unset):
            seasonal (list[GetVrboListingCancellationResponse200DataSeasonalItem] | Unset):
            options (list[GetVrboListingCancellationResponse200DataOptionsItem] | Unset):
     """

    policy_type: None | str | Unset = UNSET
    tiers: list[GetVrboListingCancellationResponse200DataTiersItem] | Unset = UNSET
    seasonal: list[GetVrboListingCancellationResponse200DataSeasonalItem] | Unset = UNSET
    options: list[GetVrboListingCancellationResponse200DataOptionsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_vrbo_listing_cancellation_response_200_data_options_item import GetVrboListingCancellationResponse200DataOptionsItem
        from ..models.get_vrbo_listing_cancellation_response_200_data_seasonal_item import GetVrboListingCancellationResponse200DataSeasonalItem
        from ..models.get_vrbo_listing_cancellation_response_200_data_tiers_item import GetVrboListingCancellationResponse200DataTiersItem
        policy_type: None | str | Unset
        if isinstance(self.policy_type, Unset):
            policy_type = UNSET
        else:
            policy_type = self.policy_type

        tiers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tiers, Unset):
            tiers = []
            for tiers_item_data in self.tiers:
                tiers_item = tiers_item_data.to_dict()
                tiers.append(tiers_item)



        seasonal: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.seasonal, Unset):
            seasonal = []
            for seasonal_item_data in self.seasonal:
                seasonal_item = seasonal_item_data.to_dict()
                seasonal.append(seasonal_item)



        options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()
                options.append(options_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if policy_type is not UNSET:
            field_dict["policyType"] = policy_type
        if tiers is not UNSET:
            field_dict["tiers"] = tiers
        if seasonal is not UNSET:
            field_dict["seasonal"] = seasonal
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_vrbo_listing_cancellation_response_200_data_options_item import GetVrboListingCancellationResponse200DataOptionsItem
        from ..models.get_vrbo_listing_cancellation_response_200_data_seasonal_item import GetVrboListingCancellationResponse200DataSeasonalItem
        from ..models.get_vrbo_listing_cancellation_response_200_data_tiers_item import GetVrboListingCancellationResponse200DataTiersItem
        d = dict(src_dict)
        def _parse_policy_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        policy_type = _parse_policy_type(d.pop("policyType", UNSET))


        _tiers = d.pop("tiers", UNSET)
        tiers: list[GetVrboListingCancellationResponse200DataTiersItem] | Unset = UNSET
        if _tiers is not UNSET:
            tiers = []
            for tiers_item_data in _tiers:
                tiers_item = GetVrboListingCancellationResponse200DataTiersItem.from_dict(tiers_item_data)



                tiers.append(tiers_item)


        _seasonal = d.pop("seasonal", UNSET)
        seasonal: list[GetVrboListingCancellationResponse200DataSeasonalItem] | Unset = UNSET
        if _seasonal is not UNSET:
            seasonal = []
            for seasonal_item_data in _seasonal:
                seasonal_item = GetVrboListingCancellationResponse200DataSeasonalItem.from_dict(seasonal_item_data)



                seasonal.append(seasonal_item)


        _options = d.pop("options", UNSET)
        options: list[GetVrboListingCancellationResponse200DataOptionsItem] | Unset = UNSET
        if _options is not UNSET:
            options = []
            for options_item_data in _options:
                options_item = GetVrboListingCancellationResponse200DataOptionsItem.from_dict(options_item_data)



                options.append(options_item)


        get_vrbo_listing_cancellation_response_200_data = cls(
            policy_type=policy_type,
            tiers=tiers,
            seasonal=seasonal,
            options=options,
        )


        get_vrbo_listing_cancellation_response_200_data.additional_properties = d
        return get_vrbo_listing_cancellation_response_200_data

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
