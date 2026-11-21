from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PublishListingToVrboResponse202JobSkippedItem")



@_attrs_define
class PublishListingToVrboResponse202JobSkippedItem:
    """ 
        Attributes:
            section (str | Unset):
            reason (str | Unset):
     """

    section: str | Unset = UNSET
    reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        section = self.section

        reason = self.reason


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if section is not UNSET:
            field_dict["section"] = section
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        section = d.pop("section", UNSET)

        reason = d.pop("reason", UNSET)

        publish_listing_to_vrbo_response_202_job_skipped_item = cls(
            section=section,
            reason=reason,
        )


        publish_listing_to_vrbo_response_202_job_skipped_item.additional_properties = d
        return publish_listing_to_vrbo_response_202_job_skipped_item

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
