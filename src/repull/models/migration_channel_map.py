from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.migration_channel_map_listings_item import MigrationChannelMapListingsItem
  from ..models.migration_channel_map_sources_item import MigrationChannelMapSourcesItem





T = TypeVar("T", bound="MigrationChannelMap")



@_attrs_define
class MigrationChannelMap:
    """ 
        Attributes:
            workspace_id (str | Unset):
            sources (list[MigrationChannelMapSourcesItem] | Unset):
            listings (list[MigrationChannelMapListingsItem] | Unset):
     """

    workspace_id: str | Unset = UNSET
    sources: list[MigrationChannelMapSourcesItem] | Unset = UNSET
    listings: list[MigrationChannelMapListingsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.migration_channel_map_listings_item import MigrationChannelMapListingsItem
        from ..models.migration_channel_map_sources_item import MigrationChannelMapSourcesItem
        workspace_id = self.workspace_id

        sources: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sources, Unset):
            sources = []
            for sources_item_data in self.sources:
                sources_item = sources_item_data.to_dict()
                sources.append(sources_item)



        listings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.listings, Unset):
            listings = []
            for listings_item_data in self.listings:
                listings_item = listings_item_data.to_dict()
                listings.append(listings_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id
        if sources is not UNSET:
            field_dict["sources"] = sources
        if listings is not UNSET:
            field_dict["listings"] = listings

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.migration_channel_map_listings_item import MigrationChannelMapListingsItem
        from ..models.migration_channel_map_sources_item import MigrationChannelMapSourcesItem
        d = dict(src_dict)
        workspace_id = d.pop("workspaceId", UNSET)

        _sources = d.pop("sources", UNSET)
        sources: list[MigrationChannelMapSourcesItem] | Unset = UNSET
        if _sources is not UNSET:
            sources = []
            for sources_item_data in _sources:
                sources_item = MigrationChannelMapSourcesItem.from_dict(sources_item_data)



                sources.append(sources_item)


        _listings = d.pop("listings", UNSET)
        listings: list[MigrationChannelMapListingsItem] | Unset = UNSET
        if _listings is not UNSET:
            listings = []
            for listings_item_data in _listings:
                listings_item = MigrationChannelMapListingsItem.from_dict(listings_item_data)



                listings.append(listings_item)


        migration_channel_map = cls(
            workspace_id=workspace_id,
            sources=sources,
            listings=listings,
        )


        migration_channel_map.additional_properties = d
        return migration_channel_map

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
