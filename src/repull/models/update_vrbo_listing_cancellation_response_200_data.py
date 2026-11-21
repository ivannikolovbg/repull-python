from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_vrbo_listing_cancellation_response_200_data_options_item import UpdateVrboListingCancellationResponse200DataOptionsItem
  from ..models.update_vrbo_listing_cancellation_response_200_data_seasonal_item import UpdateVrboListingCancellationResponse200DataSeasonalItem
  from ..models.update_vrbo_listing_cancellation_response_200_data_tiers_item import UpdateVrboListingCancellationResponse200DataTiersItem





T = TypeVar("T", bound="UpdateVrboListingCancellationResponse200Data")



@_attrs_define
class UpdateVrboListingCancellationResponse200Data:
    """ What Vrbo has after the write, read back from Vrbo.

        Attributes:
            policy_type (None | str | Unset):
            tiers (list[UpdateVrboListingCancellationResponse200DataTiersItem] | Unset):
            seasonal (list[UpdateVrboListingCancellationResponse200DataSeasonalItem] | Unset):
            options (list[UpdateVrboListingCancellationResponse200DataOptionsItem] | Unset):
     """

    policy_type: None | str | Unset = UNSET
    tiers: list[UpdateVrboListingCancellationResponse200DataTiersItem] | Unset = UNSET
    seasonal: list[UpdateVrboListingCancellationResponse200DataSeasonalItem] | Unset = UNSET
    options: list[UpdateVrboListingCancellationResponse200DataOptionsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_vrbo_listing_cancellation_response_200_data_options_item import UpdateVrboListingCancellationResponse200DataOptionsItem
        from ..models.update_vrbo_listing_cancellation_response_200_data_seasonal_item import UpdateVrboListingCancellationResponse200DataSeasonalItem
        from ..models.update_vrbo_listing_cancellation_response_200_data_tiers_item import UpdateVrboListingCancellationResponse200DataTiersItem
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
        from ..models.update_vrbo_listing_cancellation_response_200_data_options_item import UpdateVrboListingCancellationResponse200DataOptionsItem
        from ..models.update_vrbo_listing_cancellation_response_200_data_seasonal_item import UpdateVrboListingCancellationResponse200DataSeasonalItem
        from ..models.update_vrbo_listing_cancellation_response_200_data_tiers_item import UpdateVrboListingCancellationResponse200DataTiersItem
        d = dict(src_dict)
        def _parse_policy_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        policy_type = _parse_policy_type(d.pop("policyType", UNSET))


        _tiers = d.pop("tiers", UNSET)
        tiers: list[UpdateVrboListingCancellationResponse200DataTiersItem] | Unset = UNSET
        if _tiers is not UNSET:
            tiers = []
            for tiers_item_data in _tiers:
                tiers_item = UpdateVrboListingCancellationResponse200DataTiersItem.from_dict(tiers_item_data)



                tiers.append(tiers_item)


        _seasonal = d.pop("seasonal", UNSET)
        seasonal: list[UpdateVrboListingCancellationResponse200DataSeasonalItem] | Unset = UNSET
        if _seasonal is not UNSET:
            seasonal = []
            for seasonal_item_data in _seasonal:
                seasonal_item = UpdateVrboListingCancellationResponse200DataSeasonalItem.from_dict(seasonal_item_data)



                seasonal.append(seasonal_item)


        _options = d.pop("options", UNSET)
        options: list[UpdateVrboListingCancellationResponse200DataOptionsItem] | Unset = UNSET
        if _options is not UNSET:
            options = []
            for options_item_data in _options:
                options_item = UpdateVrboListingCancellationResponse200DataOptionsItem.from_dict(options_item_data)



                options.append(options_item)


        update_vrbo_listing_cancellation_response_200_data = cls(
            policy_type=policy_type,
            tiers=tiers,
            seasonal=seasonal,
            options=options,
        )


        update_vrbo_listing_cancellation_response_200_data.additional_properties = d
        return update_vrbo_listing_cancellation_response_200_data

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
