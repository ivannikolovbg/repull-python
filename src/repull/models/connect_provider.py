from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.connect_provider_category import ConnectProviderCategory
from ..models.connect_provider_connect_pattern import ConnectProviderConnectPattern
from ..models.connect_provider_status import ConnectProviderStatus
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ConnectProvider")



@_attrs_define
class ConnectProvider:
    """ A channel the multi-channel Connect picker can show. Returned by `GET /v1/connect/providers` and consumed by SDKs
    that render their own picker UI.

        Attributes:
            id (str): Stable identifier passed back to /select-provider and used in /v1/connect/{provider} routes. Example:
                airbnb.
            display_name (str):  Example: Airbnb.
            category (ConnectProviderCategory): Channel category — OTAs are listing marketplaces; PMSes are property
                management systems.
            connect_pattern (ConnectProviderConnectPattern): How the host is connected. `oauth`: provider-side consent
                screen. `credentials`: hosted form collects API keys. `activation`: push-only handshake (Vrbo). `claim`:
                connectivity-provider designation in the channel's Extranet (Booking.com).
            status (ConnectProviderStatus): Pickers should hide / disable `coming-soon` cards. `beta` cards are clickable
                but show a Beta pill.
            logo_url (str): Logo URL — Clearbit stand-in until self-hosted SVGs land.
            description (str):  Example: OAuth consent — host approves access in one click..
            docs_url (str):  Example: https://repull.dev/docs/channels/airbnb.
            aliases (list[str] | None | Unset): Optional friendly aliases the picker's search box can match. Example:
                ['airbnb', 'abnb'].
     """

    id: str
    display_name: str
    category: ConnectProviderCategory
    connect_pattern: ConnectProviderConnectPattern
    status: ConnectProviderStatus
    logo_url: str
    description: str
    docs_url: str
    aliases: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        display_name = self.display_name

        category = self.category.value

        connect_pattern = self.connect_pattern.value

        status = self.status.value

        logo_url = self.logo_url

        description = self.description

        docs_url = self.docs_url

        aliases: list[str] | None | Unset
        if isinstance(self.aliases, Unset):
            aliases = UNSET
        elif isinstance(self.aliases, list):
            aliases = self.aliases


        else:
            aliases = self.aliases


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "displayName": display_name,
            "category": category,
            "connectPattern": connect_pattern,
            "status": status,
            "logoUrl": logo_url,
            "description": description,
            "docsUrl": docs_url,
        })
        if aliases is not UNSET:
            field_dict["aliases"] = aliases

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        display_name = d.pop("displayName")

        category = ConnectProviderCategory(d.pop("category"))




        connect_pattern = ConnectProviderConnectPattern(d.pop("connectPattern"))




        status = ConnectProviderStatus(d.pop("status"))




        logo_url = d.pop("logoUrl")

        description = d.pop("description")

        docs_url = d.pop("docsUrl")

        def _parse_aliases(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                aliases_type_0 = cast(list[str], data)

                return aliases_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        aliases = _parse_aliases(d.pop("aliases", UNSET))


        connect_provider = cls(
            id=id,
            display_name=display_name,
            category=category,
            connect_pattern=connect_pattern,
            status=status,
            logo_url=logo_url,
            description=description,
            docs_url=docs_url,
            aliases=aliases,
        )


        connect_provider.additional_properties = d
        return connect_provider

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
