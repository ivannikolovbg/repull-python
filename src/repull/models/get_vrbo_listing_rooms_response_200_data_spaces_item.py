from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_vrbo_listing_rooms_response_200_data_spaces_item_amenities_item import GetVrboListingRoomsResponse200DataSpacesItemAmenitiesItem
  from ..models.get_vrbo_listing_rooms_response_200_data_spaces_item_beds_item import GetVrboListingRoomsResponse200DataSpacesItemBedsItem





T = TypeVar("T", bound="GetVrboListingRoomsResponse200DataSpacesItem")



@_attrs_define
class GetVrboListingRoomsResponse200DataSpacesItem:
    """ 
        Attributes:
            space_id (str | Unset):
            type_ (str | Unset):  Example: BEDROOM.
            sub_type (None | str | Unset):  Example: FULL_BATH.
            name (None | str | Unset):
            description (None | str | Unset):
            is_legacy_common_area (bool | Unset):
            beds (list[GetVrboListingRoomsResponse200DataSpacesItemBedsItem] | Unset):
            amenities (list[GetVrboListingRoomsResponse200DataSpacesItemAmenitiesItem] | Unset):
     """

    space_id: str | Unset = UNSET
    type_: str | Unset = UNSET
    sub_type: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    is_legacy_common_area: bool | Unset = UNSET
    beds: list[GetVrboListingRoomsResponse200DataSpacesItemBedsItem] | Unset = UNSET
    amenities: list[GetVrboListingRoomsResponse200DataSpacesItemAmenitiesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_vrbo_listing_rooms_response_200_data_spaces_item_amenities_item import GetVrboListingRoomsResponse200DataSpacesItemAmenitiesItem
        from ..models.get_vrbo_listing_rooms_response_200_data_spaces_item_beds_item import GetVrboListingRoomsResponse200DataSpacesItemBedsItem
        space_id = self.space_id

        type_ = self.type_

        sub_type: None | str | Unset
        if isinstance(self.sub_type, Unset):
            sub_type = UNSET
        else:
            sub_type = self.sub_type

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        is_legacy_common_area = self.is_legacy_common_area

        beds: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.beds, Unset):
            beds = []
            for beds_item_data in self.beds:
                beds_item = beds_item_data.to_dict()
                beds.append(beds_item)



        amenities: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.amenities, Unset):
            amenities = []
            for amenities_item_data in self.amenities:
                amenities_item = amenities_item_data.to_dict()
                amenities.append(amenities_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if space_id is not UNSET:
            field_dict["spaceId"] = space_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if sub_type is not UNSET:
            field_dict["subType"] = sub_type
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if is_legacy_common_area is not UNSET:
            field_dict["isLegacyCommonArea"] = is_legacy_common_area
        if beds is not UNSET:
            field_dict["beds"] = beds
        if amenities is not UNSET:
            field_dict["amenities"] = amenities

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_vrbo_listing_rooms_response_200_data_spaces_item_amenities_item import GetVrboListingRoomsResponse200DataSpacesItemAmenitiesItem
        from ..models.get_vrbo_listing_rooms_response_200_data_spaces_item_beds_item import GetVrboListingRoomsResponse200DataSpacesItemBedsItem
        d = dict(src_dict)
        space_id = d.pop("spaceId", UNSET)

        type_ = d.pop("type", UNSET)

        def _parse_sub_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sub_type = _parse_sub_type(d.pop("subType", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        is_legacy_common_area = d.pop("isLegacyCommonArea", UNSET)

        _beds = d.pop("beds", UNSET)
        beds: list[GetVrboListingRoomsResponse200DataSpacesItemBedsItem] | Unset = UNSET
        if _beds is not UNSET:
            beds = []
            for beds_item_data in _beds:
                beds_item = GetVrboListingRoomsResponse200DataSpacesItemBedsItem.from_dict(beds_item_data)



                beds.append(beds_item)


        _amenities = d.pop("amenities", UNSET)
        amenities: list[GetVrboListingRoomsResponse200DataSpacesItemAmenitiesItem] | Unset = UNSET
        if _amenities is not UNSET:
            amenities = []
            for amenities_item_data in _amenities:
                amenities_item = GetVrboListingRoomsResponse200DataSpacesItemAmenitiesItem.from_dict(amenities_item_data)



                amenities.append(amenities_item)


        get_vrbo_listing_rooms_response_200_data_spaces_item = cls(
            space_id=space_id,
            type_=type_,
            sub_type=sub_type,
            name=name,
            description=description,
            is_legacy_common_area=is_legacy_common_area,
            beds=beds,
            amenities=amenities,
        )


        get_vrbo_listing_rooms_response_200_data_spaces_item.additional_properties = d
        return get_vrbo_listing_rooms_response_200_data_spaces_item

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
