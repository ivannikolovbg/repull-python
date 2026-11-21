from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.update_vrbo_listing_amenities_response_200_data_groups_additional_property_fields_item_type import UpdateVrboListingAmenitiesResponse200DataGroupsAdditionalPropertyFieldsItemType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_vrbo_listing_amenities_response_200_data_groups_additional_property_fields_item_options_item import UpdateVrboListingAmenitiesResponse200DataGroupsAdditionalPropertyFieldsItemOptionsItem
  from ..models.update_vrbo_listing_amenities_response_200_data_groups_additional_property_fields_item_shown_when_type_0 import UpdateVrboListingAmenitiesResponse200DataGroupsAdditionalPropertyFieldsItemShownWhenType0





T = TypeVar("T", bound="UpdateVrboListingAmenitiesResponse200DataGroupsAdditionalPropertyFieldsItem")



@_attrs_define
class UpdateVrboListingAmenitiesResponse200DataGroupsAdditionalPropertyFieldsItem:
    """ 
        Attributes:
            id (str | Unset): The field id to write in `values`. Example: haveInternet:yes:haveWifi.
            type_ (UpdateVrboListingAmenitiesResponse200DataGroupsAdditionalPropertyFieldsItemType | Unset):
            title (None | str | Unset):
            section (None | str | Unset):
            value (bool | float | None | str | Unset): Checkbox: true/false. Choice: one of `options[].value`. Text / number
                as such.
            options (list[UpdateVrboListingAmenitiesResponse200DataGroupsAdditionalPropertyFieldsItemOptionsItem] | Unset):
            min_ (float | None | Unset):
            max_ (float | None | Unset):
            max_length (int | None | Unset):
            shown_when (None | Unset |
                UpdateVrboListingAmenitiesResponse200DataGroupsAdditionalPropertyFieldsItemShownWhenType0): The parent field and
                value this field is shown under.
     """

    id: str | Unset = UNSET
    type_: UpdateVrboListingAmenitiesResponse200DataGroupsAdditionalPropertyFieldsItemType | Unset = UNSET
    title: None | str | Unset = UNSET
    section: None | str | Unset = UNSET
    value: bool | float | None | str | Unset = UNSET
    options: list[UpdateVrboListingAmenitiesResponse200DataGroupsAdditionalPropertyFieldsItemOptionsItem] | Unset = UNSET
    min_: float | None | Unset = UNSET
    max_: float | None | Unset = UNSET
    max_length: int | None | Unset = UNSET
    shown_when: None | Unset | UpdateVrboListingAmenitiesResponse200DataGroupsAdditionalPropertyFieldsItemShownWhenType0 = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_vrbo_listing_amenities_response_200_data_groups_additional_property_fields_item_options_item import UpdateVrboListingAmenitiesResponse200DataGroupsAdditionalPropertyFieldsItemOptionsItem
        from ..models.update_vrbo_listing_amenities_response_200_data_groups_additional_property_fields_item_shown_when_type_0 import UpdateVrboListingAmenitiesResponse200DataGroupsAdditionalPropertyFieldsItemShownWhenType0
        id = self.id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value


        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        section: None | str | Unset
        if isinstance(self.section, Unset):
            section = UNSET
        else:
            section = self.section

        value: bool | float | None | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()
                options.append(options_item)



        min_: float | None | Unset
        if isinstance(self.min_, Unset):
            min_ = UNSET
        else:
            min_ = self.min_

        max_: float | None | Unset
        if isinstance(self.max_, Unset):
            max_ = UNSET
        else:
            max_ = self.max_

        max_length: int | None | Unset
        if isinstance(self.max_length, Unset):
            max_length = UNSET
        else:
            max_length = self.max_length

        shown_when: dict[str, Any] | None | Unset
        if isinstance(self.shown_when, Unset):
            shown_when = UNSET
        elif isinstance(self.shown_when, UpdateVrboListingAmenitiesResponse200DataGroupsAdditionalPropertyFieldsItemShownWhenType0):
            shown_when = self.shown_when.to_dict()
        else:
            shown_when = self.shown_when


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if title is not UNSET:
            field_dict["title"] = title
        if section is not UNSET:
            field_dict["section"] = section
        if value is not UNSET:
            field_dict["value"] = value
        if options is not UNSET:
            field_dict["options"] = options
        if min_ is not UNSET:
            field_dict["min"] = min_
        if max_ is not UNSET:
            field_dict["max"] = max_
        if max_length is not UNSET:
            field_dict["maxLength"] = max_length
        if shown_when is not UNSET:
            field_dict["shownWhen"] = shown_when

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_vrbo_listing_amenities_response_200_data_groups_additional_property_fields_item_options_item import UpdateVrboListingAmenitiesResponse200DataGroupsAdditionalPropertyFieldsItemOptionsItem
        from ..models.update_vrbo_listing_amenities_response_200_data_groups_additional_property_fields_item_shown_when_type_0 import UpdateVrboListingAmenitiesResponse200DataGroupsAdditionalPropertyFieldsItemShownWhenType0
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: UpdateVrboListingAmenitiesResponse200DataGroupsAdditionalPropertyFieldsItemType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = UpdateVrboListingAmenitiesResponse200DataGroupsAdditionalPropertyFieldsItemType(_type_)




        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))


        def _parse_section(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        section = _parse_section(d.pop("section", UNSET))


        def _parse_value(data: object) -> bool | float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | float | None | str | Unset, data)

        value = _parse_value(d.pop("value", UNSET))


        _options = d.pop("options", UNSET)
        options: list[UpdateVrboListingAmenitiesResponse200DataGroupsAdditionalPropertyFieldsItemOptionsItem] | Unset = UNSET
        if _options is not UNSET:
            options = []
            for options_item_data in _options:
                options_item = UpdateVrboListingAmenitiesResponse200DataGroupsAdditionalPropertyFieldsItemOptionsItem.from_dict(options_item_data)



                options.append(options_item)


        def _parse_min_(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        min_ = _parse_min_(d.pop("min", UNSET))


        def _parse_max_(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_ = _parse_max_(d.pop("max", UNSET))


        def _parse_max_length(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_length = _parse_max_length(d.pop("maxLength", UNSET))


        def _parse_shown_when(data: object) -> None | Unset | UpdateVrboListingAmenitiesResponse200DataGroupsAdditionalPropertyFieldsItemShownWhenType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                shown_when_type_0 = UpdateVrboListingAmenitiesResponse200DataGroupsAdditionalPropertyFieldsItemShownWhenType0.from_dict(data)



                return shown_when_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateVrboListingAmenitiesResponse200DataGroupsAdditionalPropertyFieldsItemShownWhenType0, data)

        shown_when = _parse_shown_when(d.pop("shownWhen", UNSET))


        update_vrbo_listing_amenities_response_200_data_groups_additional_property_fields_item = cls(
            id=id,
            type_=type_,
            title=title,
            section=section,
            value=value,
            options=options,
            min_=min_,
            max_=max_,
            max_length=max_length,
            shown_when=shown_when,
        )


        update_vrbo_listing_amenities_response_200_data_groups_additional_property_fields_item.additional_properties = d
        return update_vrbo_listing_amenities_response_200_data_groups_additional_property_fields_item

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
