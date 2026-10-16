from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.promotion_catalog_channels_item import PromotionCatalogChannelsItem





T = TypeVar("T", bound="PromotionCatalog")



@_attrs_define
class PromotionCatalog:
    """ 
        Attributes:
            listing_id (str | Unset):
            channels (list[PromotionCatalogChannelsItem] | Unset):
     """

    listing_id: str | Unset = UNSET
    channels: list[PromotionCatalogChannelsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.promotion_catalog_channels_item import PromotionCatalogChannelsItem
        listing_id = self.listing_id

        channels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.channels, Unset):
            channels = []
            for channels_item_data in self.channels:
                channels_item = channels_item_data.to_dict()
                channels.append(channels_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if channels is not UNSET:
            field_dict["channels"] = channels

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.promotion_catalog_channels_item import PromotionCatalogChannelsItem
        d = dict(src_dict)
        listing_id = d.pop("listingId", UNSET)

        _channels = d.pop("channels", UNSET)
        channels: list[PromotionCatalogChannelsItem] | Unset = UNSET
        if _channels is not UNSET:
            channels = []
            for channels_item_data in _channels:
                channels_item = PromotionCatalogChannelsItem.from_dict(channels_item_data)



                channels.append(channels_item)


        promotion_catalog = cls(
            listing_id=listing_id,
            channels=channels,
        )


        promotion_catalog.additional_properties = d
        return promotion_catalog

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
