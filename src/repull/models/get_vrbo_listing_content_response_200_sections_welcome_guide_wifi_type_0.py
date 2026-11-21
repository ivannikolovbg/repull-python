from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GetVrboListingContentResponse200SectionsWelcomeGuideWifiType0")



@_attrs_define
class GetVrboListingContentResponse200SectionsWelcomeGuideWifiType0:
    """ 
        Attributes:
            network_name (None | str | Unset):
            password (None | str | Unset):
            instructions (None | str | Unset):
            available (bool | None | Unset):
     """

    network_name: None | str | Unset = UNSET
    password: None | str | Unset = UNSET
    instructions: None | str | Unset = UNSET
    available: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        network_name: None | str | Unset
        if isinstance(self.network_name, Unset):
            network_name = UNSET
        else:
            network_name = self.network_name

        password: None | str | Unset
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password

        instructions: None | str | Unset
        if isinstance(self.instructions, Unset):
            instructions = UNSET
        else:
            instructions = self.instructions

        available: bool | None | Unset
        if isinstance(self.available, Unset):
            available = UNSET
        else:
            available = self.available


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if network_name is not UNSET:
            field_dict["networkName"] = network_name
        if password is not UNSET:
            field_dict["password"] = password
        if instructions is not UNSET:
            field_dict["instructions"] = instructions
        if available is not UNSET:
            field_dict["available"] = available

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_network_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        network_name = _parse_network_name(d.pop("networkName", UNSET))


        def _parse_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        password = _parse_password(d.pop("password", UNSET))


        def _parse_instructions(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        instructions = _parse_instructions(d.pop("instructions", UNSET))


        def _parse_available(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        available = _parse_available(d.pop("available", UNSET))


        get_vrbo_listing_content_response_200_sections_welcome_guide_wifi_type_0 = cls(
            network_name=network_name,
            password=password,
            instructions=instructions,
            available=available,
        )


        get_vrbo_listing_content_response_200_sections_welcome_guide_wifi_type_0.additional_properties = d
        return get_vrbo_listing_content_response_200_sections_welcome_guide_wifi_type_0

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
