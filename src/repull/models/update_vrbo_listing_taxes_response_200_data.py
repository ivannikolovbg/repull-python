from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_vrbo_listing_taxes_response_200_data_rules_item import UpdateVrboListingTaxesResponse200DataRulesItem





T = TypeVar("T", bound="UpdateVrboListingTaxesResponse200Data")



@_attrs_define
class UpdateVrboListingTaxesResponse200Data:
    """ What Vrbo has after the write, read back from Vrbo.

        Attributes:
            tax_source (None | str | Unset):
            vrbo_collects (bool | Unset):
            rules (list[UpdateVrboListingTaxesResponse200DataRulesItem] | Unset):
            raw (Any | Unset): Vrbo's tax settings as Vrbo returns them — the shape a write takes.
     """

    tax_source: None | str | Unset = UNSET
    vrbo_collects: bool | Unset = UNSET
    rules: list[UpdateVrboListingTaxesResponse200DataRulesItem] | Unset = UNSET
    raw: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_vrbo_listing_taxes_response_200_data_rules_item import UpdateVrboListingTaxesResponse200DataRulesItem
        tax_source: None | str | Unset
        if isinstance(self.tax_source, Unset):
            tax_source = UNSET
        else:
            tax_source = self.tax_source

        vrbo_collects = self.vrbo_collects

        rules: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rules, Unset):
            rules = []
            for rules_item_data in self.rules:
                rules_item = rules_item_data.to_dict()
                rules.append(rules_item)



        raw = self.raw


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if tax_source is not UNSET:
            field_dict["taxSource"] = tax_source
        if vrbo_collects is not UNSET:
            field_dict["vrboCollects"] = vrbo_collects
        if rules is not UNSET:
            field_dict["rules"] = rules
        if raw is not UNSET:
            field_dict["raw"] = raw

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_vrbo_listing_taxes_response_200_data_rules_item import UpdateVrboListingTaxesResponse200DataRulesItem
        d = dict(src_dict)
        def _parse_tax_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tax_source = _parse_tax_source(d.pop("taxSource", UNSET))


        vrbo_collects = d.pop("vrboCollects", UNSET)

        _rules = d.pop("rules", UNSET)
        rules: list[UpdateVrboListingTaxesResponse200DataRulesItem] | Unset = UNSET
        if _rules is not UNSET:
            rules = []
            for rules_item_data in _rules:
                rules_item = UpdateVrboListingTaxesResponse200DataRulesItem.from_dict(rules_item_data)



                rules.append(rules_item)


        raw = d.pop("raw", UNSET)

        update_vrbo_listing_taxes_response_200_data = cls(
            tax_source=tax_source,
            vrbo_collects=vrbo_collects,
            rules=rules,
            raw=raw,
        )


        update_vrbo_listing_taxes_response_200_data.additional_properties = d
        return update_vrbo_listing_taxes_response_200_data

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
