from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UpdateVrboListingCheckinGuideBodyWifi")



@_attrs_define
class UpdateVrboListingCheckinGuideBodyWifi:
    """ 
        Attributes:
            network_name (str | Unset):
            password (str | Unset):
            instructions (str | Unset):
     """

    network_name: str | Unset = UNSET
    password: str | Unset = UNSET
    instructions: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        network_name = self.network_name

        password = self.password

        instructions = self.instructions


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if network_name is not UNSET:
            field_dict["networkName"] = network_name
        if password is not UNSET:
            field_dict["password"] = password
        if instructions is not UNSET:
            field_dict["instructions"] = instructions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        network_name = d.pop("networkName", UNSET)

        password = d.pop("password", UNSET)

        instructions = d.pop("instructions", UNSET)

        update_vrbo_listing_checkin_guide_body_wifi = cls(
            network_name=network_name,
            password=password,
            instructions=instructions,
        )

        return update_vrbo_listing_checkin_guide_body_wifi

