from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.update_vrbo_listing_registration_body_settings_item import UpdateVrboListingRegistrationBodySettingsItem





T = TypeVar("T", bound="UpdateVrboListingRegistrationBody")



@_attrs_define
class UpdateVrboListingRegistrationBody:
    """ 
        Attributes:
            settings (list[UpdateVrboListingRegistrationBodySettingsItem]):
     """

    settings: list[UpdateVrboListingRegistrationBodySettingsItem]





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_vrbo_listing_registration_body_settings_item import UpdateVrboListingRegistrationBodySettingsItem
        settings = []
        for settings_item_data in self.settings:
            settings_item = settings_item_data.to_dict()
            settings.append(settings_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "settings": settings,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_vrbo_listing_registration_body_settings_item import UpdateVrboListingRegistrationBodySettingsItem
        d = dict(src_dict)
        settings = []
        _settings = d.pop("settings")
        for settings_item_data in (_settings):
            settings_item = UpdateVrboListingRegistrationBodySettingsItem.from_dict(settings_item_data)



            settings.append(settings_item)


        update_vrbo_listing_registration_body = cls(
            settings=settings,
        )

        return update_vrbo_listing_registration_body

