from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.update_vrbo_listing_permits_body_settings_item import UpdateVrboListingPermitsBodySettingsItem





T = TypeVar("T", bound="UpdateVrboListingPermitsBody")



@_attrs_define
class UpdateVrboListingPermitsBody:
    """ 
        Attributes:
            settings (list[UpdateVrboListingPermitsBodySettingsItem]):
     """

    settings: list[UpdateVrboListingPermitsBodySettingsItem]





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_vrbo_listing_permits_body_settings_item import UpdateVrboListingPermitsBodySettingsItem
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
        from ..models.update_vrbo_listing_permits_body_settings_item import UpdateVrboListingPermitsBodySettingsItem
        d = dict(src_dict)
        settings = []
        _settings = d.pop("settings")
        for settings_item_data in (_settings):
            settings_item = UpdateVrboListingPermitsBodySettingsItem.from_dict(settings_item_data)



            settings.append(settings_item)


        update_vrbo_listing_permits_body = cls(
            settings=settings,
        )

        return update_vrbo_listing_permits_body

