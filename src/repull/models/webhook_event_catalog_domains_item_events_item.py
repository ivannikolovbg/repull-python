from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.webhook_event_catalog_domains_item_events_item_sample_payload import WebhookEventCatalogDomainsItemEventsItemSamplePayload





T = TypeVar("T", bound="WebhookEventCatalogDomainsItemEventsItem")



@_attrs_define
class WebhookEventCatalogDomainsItemEventsItem:
    """ 
        Attributes:
            type_ (str | Unset):
            domain (str | Unset):
            title (str | Unset):
            description (str | Unset):
            sample_payload (WebhookEventCatalogDomainsItemEventsItemSamplePayload | Unset):
     """

    type_: str | Unset = UNSET
    domain: str | Unset = UNSET
    title: str | Unset = UNSET
    description: str | Unset = UNSET
    sample_payload: WebhookEventCatalogDomainsItemEventsItemSamplePayload | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.webhook_event_catalog_domains_item_events_item_sample_payload import WebhookEventCatalogDomainsItemEventsItemSamplePayload
        type_ = self.type_

        domain = self.domain

        title = self.title

        description = self.description

        sample_payload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sample_payload, Unset):
            sample_payload = self.sample_payload.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if type_ is not UNSET:
            field_dict["type"] = type_
        if domain is not UNSET:
            field_dict["domain"] = domain
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if sample_payload is not UNSET:
            field_dict["samplePayload"] = sample_payload

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_event_catalog_domains_item_events_item_sample_payload import WebhookEventCatalogDomainsItemEventsItemSamplePayload
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        domain = d.pop("domain", UNSET)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        _sample_payload = d.pop("samplePayload", UNSET)
        sample_payload: WebhookEventCatalogDomainsItemEventsItemSamplePayload | Unset
        if isinstance(_sample_payload,  Unset):
            sample_payload = UNSET
        else:
            sample_payload = WebhookEventCatalogDomainsItemEventsItemSamplePayload.from_dict(_sample_payload)




        webhook_event_catalog_domains_item_events_item = cls(
            type_=type_,
            domain=domain,
            title=title,
            description=description,
            sample_payload=sample_payload,
        )


        webhook_event_catalog_domains_item_events_item.additional_properties = d
        return webhook_event_catalog_domains_item_events_item

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
