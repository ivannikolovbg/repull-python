from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_vrbo_listing_response_200_data_item_content_sections import GetVrboListingResponse200DataItemContentSections
  from ..models.get_vrbo_listing_response_200_data_item_content_synced_at import GetVrboListingResponse200DataItemContentSyncedAt





T = TypeVar("T", bound="GetVrboListingResponse200DataItemContent")



@_attrs_define
class GetVrboListingResponse200DataItemContent:
    """ 
        Attributes:
            sections (GetVrboListingResponse200DataItemContentSections | Unset): With `include=content`: each section Repull
                holds, as `GET /v1/channels/vrbo/listings/{id}/{section}` returns its `data`.
            synced_at (GetVrboListingResponse200DataItemContentSyncedAt | Unset): When each section was read from Vrbo.
     """

    sections: GetVrboListingResponse200DataItemContentSections | Unset = UNSET
    synced_at: GetVrboListingResponse200DataItemContentSyncedAt | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_vrbo_listing_response_200_data_item_content_sections import GetVrboListingResponse200DataItemContentSections
        from ..models.get_vrbo_listing_response_200_data_item_content_synced_at import GetVrboListingResponse200DataItemContentSyncedAt
        sections: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sections, Unset):
            sections = self.sections.to_dict()

        synced_at: dict[str, Any] | Unset = UNSET
        if not isinstance(self.synced_at, Unset):
            synced_at = self.synced_at.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if sections is not UNSET:
            field_dict["sections"] = sections
        if synced_at is not UNSET:
            field_dict["syncedAt"] = synced_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_vrbo_listing_response_200_data_item_content_sections import GetVrboListingResponse200DataItemContentSections
        from ..models.get_vrbo_listing_response_200_data_item_content_synced_at import GetVrboListingResponse200DataItemContentSyncedAt
        d = dict(src_dict)
        _sections = d.pop("sections", UNSET)
        sections: GetVrboListingResponse200DataItemContentSections | Unset
        if isinstance(_sections,  Unset):
            sections = UNSET
        else:
            sections = GetVrboListingResponse200DataItemContentSections.from_dict(_sections)




        _synced_at = d.pop("syncedAt", UNSET)
        synced_at: GetVrboListingResponse200DataItemContentSyncedAt | Unset
        if isinstance(_synced_at,  Unset):
            synced_at = UNSET
        else:
            synced_at = GetVrboListingResponse200DataItemContentSyncedAt.from_dict(_synced_at)




        get_vrbo_listing_response_200_data_item_content = cls(
            sections=sections,
            synced_at=synced_at,
        )


        get_vrbo_listing_response_200_data_item_content.additional_properties = d
        return get_vrbo_listing_response_200_data_item_content

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
