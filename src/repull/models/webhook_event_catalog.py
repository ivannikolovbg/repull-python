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





T = TypeVar("T", bound="WebhookEventCatalog")



@_attrs_define
class WebhookEventCatalog:
    """ 
        Attributes:
            domains (list[WebhookEventCatalogDomainsItem] | Unset):
     """

    domains: list[WebhookEventCatalogDomainsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.webhook_event_catalog_domains_item import WebhookEventCatalogDomainsItem
        domains: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.domains, Unset):
            domains = []
            for domains_item_data in self.domains:
                domains_item = domains_item_data.to_dict()
                domains.append(domains_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if domains is not UNSET:
            field_dict["domains"] = domains

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_event_catalog_domains_item import WebhookEventCatalogDomainsItem
        d = dict(src_dict)
        _domains = d.pop("domains", UNSET)
        domains: list[WebhookEventCatalogDomainsItem] | Unset = UNSET
        if _domains is not UNSET:
            domains = []
            for domains_item_data in _domains:
                domains_item = WebhookEventCatalogDomainsItem.from_dict(domains_item_data)



                domains.append(domains_item)


        webhook_event_catalog = cls(
            domains=domains,
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
