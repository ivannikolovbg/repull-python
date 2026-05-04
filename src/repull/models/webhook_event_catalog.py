from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.webhook_event_catalog_domains_item import WebhookEventCatalogDomainsItem
  from ..models.webhook_event_catalog_entry import WebhookEventCatalogEntry





T = TypeVar("T", bound="WebhookEventCatalog")



@_attrs_define
class WebhookEventCatalog:
    """ Canonical catalog of every event the API can deliver, grouped by domain. Each entry includes a realistic
    `samplePayload` matching the discriminated `WebhookEvent` union — so SDKs can render docs and dashboards from this
    single source of truth.

        Attributes:
            domains (list[WebhookEventCatalogDomainsItem] | Unset):
            flat (list[WebhookEventCatalogEntry] | Unset): All events in a flat list (same entries as `domains[].events`,
                ungrouped).
     """

    domains: list[WebhookEventCatalogDomainsItem] | Unset = UNSET
    flat: list[WebhookEventCatalogEntry] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.webhook_event_catalog_domains_item import WebhookEventCatalogDomainsItem
        from ..models.webhook_event_catalog_entry import WebhookEventCatalogEntry
        domains: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.domains, Unset):
            domains = []
            for domains_item_data in self.domains:
                domains_item = domains_item_data.to_dict()
                domains.append(domains_item)



        flat: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.flat, Unset):
            flat = []
            for flat_item_data in self.flat:
                flat_item = flat_item_data.to_dict()
                flat.append(flat_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if domains is not UNSET:
            field_dict["domains"] = domains
        if flat is not UNSET:
            field_dict["flat"] = flat

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_event_catalog_domains_item import WebhookEventCatalogDomainsItem
        from ..models.webhook_event_catalog_entry import WebhookEventCatalogEntry
        d = dict(src_dict)
        _domains = d.pop("domains", UNSET)
        domains: list[WebhookEventCatalogDomainsItem] | Unset = UNSET
        if _domains is not UNSET:
            domains = []
            for domains_item_data in _domains:
                domains_item = WebhookEventCatalogDomainsItem.from_dict(domains_item_data)



                domains.append(domains_item)


        _flat = d.pop("flat", UNSET)
        flat: list[WebhookEventCatalogEntry] | Unset = UNSET
        if _flat is not UNSET:
            flat = []
            for flat_item_data in _flat:
                flat_item = WebhookEventCatalogEntry.from_dict(flat_item_data)



                flat.append(flat_item)


        webhook_event_catalog = cls(
            domains=domains,
            flat=flat,
        )


        webhook_event_catalog.additional_properties = d
        return webhook_event_catalog

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
