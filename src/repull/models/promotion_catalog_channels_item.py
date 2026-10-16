from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.promotion_catalog_channels_item_channel import PromotionCatalogChannelsItemChannel
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.promotion_catalog_entry import PromotionCatalogEntry





T = TypeVar("T", bound="PromotionCatalogChannelsItem")



@_attrs_define
class PromotionCatalogChannelsItem:
    """ 
        Attributes:
            channel (PromotionCatalogChannelsItemChannel | Unset):
            connected (bool | Unset):
            reason (str | Unset):
            properties (list[str] | Unset): Booking.com properties the listing has a room on.
            entries (list[PromotionCatalogEntry] | Unset):
     """

    channel: PromotionCatalogChannelsItemChannel | Unset = UNSET
    connected: bool | Unset = UNSET
    reason: str | Unset = UNSET
    properties: list[str] | Unset = UNSET
    entries: list[PromotionCatalogEntry] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.promotion_catalog_entry import PromotionCatalogEntry
        channel: str | Unset = UNSET
        if not isinstance(self.channel, Unset):
            channel = self.channel.value


        connected = self.connected

        reason = self.reason

        properties: list[str] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties



        entries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.entries, Unset):
            entries = []
            for entries_item_data in self.entries:
                entries_item = entries_item_data.to_dict()
                entries.append(entries_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if channel is not UNSET:
            field_dict["channel"] = channel
        if connected is not UNSET:
            field_dict["connected"] = connected
        if reason is not UNSET:
            field_dict["reason"] = reason
        if properties is not UNSET:
            field_dict["properties"] = properties
        if entries is not UNSET:
            field_dict["entries"] = entries

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.promotion_catalog_entry import PromotionCatalogEntry
        d = dict(src_dict)
        _channel = d.pop("channel", UNSET)
        channel: PromotionCatalogChannelsItemChannel | Unset
        if isinstance(_channel,  Unset):
            channel = UNSET
        else:
            channel = PromotionCatalogChannelsItemChannel(_channel)




        connected = d.pop("connected", UNSET)

        reason = d.pop("reason", UNSET)

        properties = cast(list[str], d.pop("properties", UNSET))


        _entries = d.pop("entries", UNSET)
        entries: list[PromotionCatalogEntry] | Unset = UNSET
        if _entries is not UNSET:
            entries = []
            for entries_item_data in _entries:
                entries_item = PromotionCatalogEntry.from_dict(entries_item_data)



                entries.append(entries_item)


        promotion_catalog_channels_item = cls(
            channel=channel,
            connected=connected,
            reason=reason,
            properties=properties,
            entries=entries,
        )


        promotion_catalog_channels_item.additional_properties = d
        return promotion_catalog_channels_item

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
