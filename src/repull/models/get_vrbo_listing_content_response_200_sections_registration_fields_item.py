from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_vrbo_listing_content_response_200_sections_registration_fields_item_options_item import GetVrboListingContentResponse200SectionsRegistrationFieldsItemOptionsItem





T = TypeVar("T", bound="GetVrboListingContentResponse200SectionsRegistrationFieldsItem")



@_attrs_define
class GetVrboListingContentResponse200SectionsRegistrationFieldsItem:
    """ 
        Attributes:
            name (str | Unset):
            label (None | str | Unset):
            value (Any | Unset):
            options (list[GetVrboListingContentResponse200SectionsRegistrationFieldsItemOptionsItem] | Unset):
     """

    name: str | Unset = UNSET
    label: None | str | Unset = UNSET
    value: Any | Unset = UNSET
    options: list[GetVrboListingContentResponse200SectionsRegistrationFieldsItemOptionsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_vrbo_listing_content_response_200_sections_registration_fields_item_options_item import GetVrboListingContentResponse200SectionsRegistrationFieldsItemOptionsItem
        name = self.name

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        value = self.value

        options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()
                options.append(options_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if label is not UNSET:
            field_dict["label"] = label
        if value is not UNSET:
            field_dict["value"] = value
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_vrbo_listing_content_response_200_sections_registration_fields_item_options_item import GetVrboListingContentResponse200SectionsRegistrationFieldsItemOptionsItem
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))


        value = d.pop("value", UNSET)

        _options = d.pop("options", UNSET)
        options: list[GetVrboListingContentResponse200SectionsRegistrationFieldsItemOptionsItem] | Unset = UNSET
        if _options is not UNSET:
            options = []
            for options_item_data in _options:
                options_item = GetVrboListingContentResponse200SectionsRegistrationFieldsItemOptionsItem.from_dict(options_item_data)



                options.append(options_item)


        get_vrbo_listing_content_response_200_sections_registration_fields_item = cls(
            name=name,
            label=label,
            value=value,
            options=options,
        )


        get_vrbo_listing_content_response_200_sections_registration_fields_item.additional_properties = d
        return get_vrbo_listing_content_response_200_sections_registration_fields_item

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
