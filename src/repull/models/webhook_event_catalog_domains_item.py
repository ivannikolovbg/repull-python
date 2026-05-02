from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.webhook_event_catalog_domains_item_events_item import WebhookEventCatalogDomainsItemEventsItem





T = TypeVar("T", bound="WebhookEventCatalogDomainsItem")



@_attrs_define
class WebhookEventCatalogDomainsItem:
    """ 
        Attributes:
            id (str | Unset):
            title (str | Unset):
            events (list[WebhookEventCatalogDomainsItemEventsItem] | Unset):
     """

    id: str | Unset = UNSET
    title: str | Unset = UNSET
    events: list[WebhookEventCatalogDomainsItemEventsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.webhook_event_catalog_domains_item_events_item import WebhookEventCatalogDomainsItemEventsItem
        id = self.id

        title = self.title

        events: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.to_dict()
                events.append(events_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_event_catalog_domains_item_events_item import WebhookEventCatalogDomainsItemEventsItem
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        _events = d.pop("events", UNSET)
        events: list[WebhookEventCatalogDomainsItemEventsItem] | Unset = UNSET
        if _events is not UNSET:
            events = []
            for events_item_data in _events:
                events_item = WebhookEventCatalogDomainsItemEventsItem.from_dict(events_item_data)



                events.append(events_item)


        webhook_event_catalog_domains_item = cls(
            id=id,
            title=title,
            events=events,
        )


        webhook_event_catalog_domains_item.additional_properties = d
        return webhook_event_catalog_domains_item

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
