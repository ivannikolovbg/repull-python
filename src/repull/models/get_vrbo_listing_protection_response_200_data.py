from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_vrbo_listing_protection_response_200_data_options_item import GetVrboListingProtectionResponse200DataOptionsItem





T = TypeVar("T", bound="GetVrboListingProtectionResponse200Data")



@_attrs_define
class GetVrboListingProtectionResponse200Data:
    """ The section as Vrbo has it.

        Attributes:
            currency (None | str | Unset):
            damage_coverage_enabled (bool | None | Unset):
            damage_deposit (Any | Unset):
            damage_protection (Any | Unset):
            options (list[GetVrboListingProtectionResponse200DataOptionsItem] | Unset):
     """

    currency: None | str | Unset = UNSET
    damage_coverage_enabled: bool | None | Unset = UNSET
    damage_deposit: Any | Unset = UNSET
    damage_protection: Any | Unset = UNSET
    options: list[GetVrboListingProtectionResponse200DataOptionsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_vrbo_listing_protection_response_200_data_options_item import GetVrboListingProtectionResponse200DataOptionsItem
        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        damage_coverage_enabled: bool | None | Unset
        if isinstance(self.damage_coverage_enabled, Unset):
            damage_coverage_enabled = UNSET
        else:
            damage_coverage_enabled = self.damage_coverage_enabled

        damage_deposit = self.damage_deposit

        damage_protection = self.damage_protection

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
        if currency is not UNSET:
            field_dict["currency"] = currency
        if damage_coverage_enabled is not UNSET:
            field_dict["damageCoverageEnabled"] = damage_coverage_enabled
        if damage_deposit is not UNSET:
            field_dict["damageDeposit"] = damage_deposit
        if damage_protection is not UNSET:
            field_dict["damageProtection"] = damage_protection
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_vrbo_listing_protection_response_200_data_options_item import GetVrboListingProtectionResponse200DataOptionsItem
        d = dict(src_dict)
        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))


        def _parse_damage_coverage_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        damage_coverage_enabled = _parse_damage_coverage_enabled(d.pop("damageCoverageEnabled", UNSET))


        damage_deposit = d.pop("damageDeposit", UNSET)

        damage_protection = d.pop("damageProtection", UNSET)

        _options = d.pop("options", UNSET)
        options: list[GetVrboListingProtectionResponse200DataOptionsItem] | Unset = UNSET
        if _options is not UNSET:
            options = []
            for options_item_data in _options:
                options_item = GetVrboListingProtectionResponse200DataOptionsItem.from_dict(options_item_data)



                options.append(options_item)


        get_vrbo_listing_protection_response_200_data = cls(
            currency=currency,
            damage_coverage_enabled=damage_coverage_enabled,
            damage_deposit=damage_deposit,
            damage_protection=damage_protection,
            options=options,
        )


        get_vrbo_listing_protection_response_200_data.additional_properties = d
        return get_vrbo_listing_protection_response_200_data

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
