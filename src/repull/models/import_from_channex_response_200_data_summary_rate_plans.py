from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ImportFromChannexResponse200DataSummaryRatePlans")



@_attrs_define
class ImportFromChannexResponse200DataSummaryRatePlans:
    """ 
        Attributes:
            matched (int | Unset):
            created (int | Unset):
            needs_action (int | Unset):
     """

    matched: int | Unset = UNSET
    created: int | Unset = UNSET
    needs_action: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        matched = self.matched

        created = self.created

        needs_action = self.needs_action


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if matched is not UNSET:
            field_dict["matched"] = matched
        if created is not UNSET:
            field_dict["created"] = created
        if needs_action is not UNSET:
            field_dict["needsAction"] = needs_action

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        matched = d.pop("matched", UNSET)

        created = d.pop("created", UNSET)

        needs_action = d.pop("needsAction", UNSET)

        import_from_channex_response_200_data_summary_rate_plans = cls(
            matched=matched,
            created=created,
            needs_action=needs_action,
        )


        import_from_channex_response_200_data_summary_rate_plans.additional_properties = d
        return import_from_channex_response_200_data_summary_rate_plans

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
