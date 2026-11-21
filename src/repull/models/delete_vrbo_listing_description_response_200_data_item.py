from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.delete_vrbo_listing_description_response_200_data_item_limits import DeleteVrboListingDescriptionResponse200DataItemLimits





T = TypeVar("T", bound="DeleteVrboListingDescriptionResponse200DataItem")



@_attrs_define
class DeleteVrboListingDescriptionResponse200DataItem:
    """ 
        Attributes:
            locale (None | str | Unset): `null` for the listing's own language; a language code for a hand-written
                translation. Example: fr-FR.
            primary (bool | Unset): `true` for the listing's own language.
            headline (None | str | Unset):
            description (None | str | Unset):
            limits (DeleteVrboListingDescriptionResponse200DataItemLimits | Unset): On the primary item: the lengths Vrbo
                allows.
     """

    locale: None | str | Unset = UNSET
    primary: bool | Unset = UNSET
    headline: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    limits: DeleteVrboListingDescriptionResponse200DataItemLimits | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.delete_vrbo_listing_description_response_200_data_item_limits import DeleteVrboListingDescriptionResponse200DataItemLimits
        locale: None | str | Unset
        if isinstance(self.locale, Unset):
            locale = UNSET
        else:
            locale = self.locale

        primary = self.primary

        headline: None | str | Unset
        if isinstance(self.headline, Unset):
            headline = UNSET
        else:
            headline = self.headline

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        limits: dict[str, Any] | Unset = UNSET
        if not isinstance(self.limits, Unset):
            limits = self.limits.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if locale is not UNSET:
            field_dict["locale"] = locale
        if primary is not UNSET:
            field_dict["primary"] = primary
        if headline is not UNSET:
            field_dict["headline"] = headline
        if description is not UNSET:
            field_dict["description"] = description
        if limits is not UNSET:
            field_dict["limits"] = limits

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.delete_vrbo_listing_description_response_200_data_item_limits import DeleteVrboListingDescriptionResponse200DataItemLimits
        d = dict(src_dict)
        def _parse_locale(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        locale = _parse_locale(d.pop("locale", UNSET))


        primary = d.pop("primary", UNSET)

        def _parse_headline(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        headline = _parse_headline(d.pop("headline", UNSET))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        _limits = d.pop("limits", UNSET)
        limits: DeleteVrboListingDescriptionResponse200DataItemLimits | Unset
        if isinstance(_limits,  Unset):
            limits = UNSET
        else:
            limits = DeleteVrboListingDescriptionResponse200DataItemLimits.from_dict(_limits)




        delete_vrbo_listing_description_response_200_data_item = cls(
            locale=locale,
            primary=primary,
            headline=headline,
            description=description,
            limits=limits,
        )


        delete_vrbo_listing_description_response_200_data_item.additional_properties = d
        return delete_vrbo_listing_description_response_200_data_item

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
