from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_vrbo_listing_rooms_response_200_data_bathroom_types_item import UpdateVrboListingRoomsResponse200DataBathroomTypesItem
  from ..models.update_vrbo_listing_rooms_response_200_data_bed_types_item import UpdateVrboListingRoomsResponse200DataBedTypesItem
  from ..models.update_vrbo_listing_rooms_response_200_data_spaces_item import UpdateVrboListingRoomsResponse200DataSpacesItem





T = TypeVar("T", bound="UpdateVrboListingRoomsResponse200Data")



@_attrs_define
class UpdateVrboListingRoomsResponse200Data:
    """ What Vrbo has stored for the section, read back after the write.

        Attributes:
            unit_id (None | str | Unset):
            spaces (list[UpdateVrboListingRoomsResponse200DataSpacesItem] | Unset):
            addable_types (list[str] | Unset):
            bed_types (list[UpdateVrboListingRoomsResponse200DataBedTypesItem] | Unset):
            bathroom_types (list[UpdateVrboListingRoomsResponse200DataBathroomTypesItem] | Unset):
     """

    unit_id: None | str | Unset = UNSET
    spaces: list[UpdateVrboListingRoomsResponse200DataSpacesItem] | Unset = UNSET
    addable_types: list[str] | Unset = UNSET
    bed_types: list[UpdateVrboListingRoomsResponse200DataBedTypesItem] | Unset = UNSET
    bathroom_types: list[UpdateVrboListingRoomsResponse200DataBathroomTypesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_vrbo_listing_rooms_response_200_data_bathroom_types_item import UpdateVrboListingRoomsResponse200DataBathroomTypesItem
        from ..models.update_vrbo_listing_rooms_response_200_data_bed_types_item import UpdateVrboListingRoomsResponse200DataBedTypesItem
        from ..models.update_vrbo_listing_rooms_response_200_data_spaces_item import UpdateVrboListingRoomsResponse200DataSpacesItem
        unit_id: None | str | Unset
        if isinstance(self.unit_id, Unset):
            unit_id = UNSET
        else:
            unit_id = self.unit_id

        spaces: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.spaces, Unset):
            spaces = []
            for spaces_item_data in self.spaces:
                spaces_item = spaces_item_data.to_dict()
                spaces.append(spaces_item)



        addable_types: list[str] | Unset = UNSET
        if not isinstance(self.addable_types, Unset):
            addable_types = self.addable_types



        bed_types: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.bed_types, Unset):
            bed_types = []
            for bed_types_item_data in self.bed_types:
                bed_types_item = bed_types_item_data.to_dict()
                bed_types.append(bed_types_item)



        bathroom_types: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.bathroom_types, Unset):
            bathroom_types = []
            for bathroom_types_item_data in self.bathroom_types:
                bathroom_types_item = bathroom_types_item_data.to_dict()
                bathroom_types.append(bathroom_types_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if unit_id is not UNSET:
            field_dict["unitId"] = unit_id
        if spaces is not UNSET:
            field_dict["spaces"] = spaces
        if addable_types is not UNSET:
            field_dict["addableTypes"] = addable_types
        if bed_types is not UNSET:
            field_dict["bedTypes"] = bed_types
        if bathroom_types is not UNSET:
            field_dict["bathroomTypes"] = bathroom_types

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_vrbo_listing_rooms_response_200_data_bathroom_types_item import UpdateVrboListingRoomsResponse200DataBathroomTypesItem
        from ..models.update_vrbo_listing_rooms_response_200_data_bed_types_item import UpdateVrboListingRoomsResponse200DataBedTypesItem
        from ..models.update_vrbo_listing_rooms_response_200_data_spaces_item import UpdateVrboListingRoomsResponse200DataSpacesItem
        d = dict(src_dict)
        def _parse_unit_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unit_id = _parse_unit_id(d.pop("unitId", UNSET))


        _spaces = d.pop("spaces", UNSET)
        spaces: list[UpdateVrboListingRoomsResponse200DataSpacesItem] | Unset = UNSET
        if _spaces is not UNSET:
            spaces = []
            for spaces_item_data in _spaces:
                spaces_item = UpdateVrboListingRoomsResponse200DataSpacesItem.from_dict(spaces_item_data)



                spaces.append(spaces_item)


        addable_types = cast(list[str], d.pop("addableTypes", UNSET))


        _bed_types = d.pop("bedTypes", UNSET)
        bed_types: list[UpdateVrboListingRoomsResponse200DataBedTypesItem] | Unset = UNSET
        if _bed_types is not UNSET:
            bed_types = []
            for bed_types_item_data in _bed_types:
                bed_types_item = UpdateVrboListingRoomsResponse200DataBedTypesItem.from_dict(bed_types_item_data)



                bed_types.append(bed_types_item)


        _bathroom_types = d.pop("bathroomTypes", UNSET)
        bathroom_types: list[UpdateVrboListingRoomsResponse200DataBathroomTypesItem] | Unset = UNSET
        if _bathroom_types is not UNSET:
            bathroom_types = []
            for bathroom_types_item_data in _bathroom_types:
                bathroom_types_item = UpdateVrboListingRoomsResponse200DataBathroomTypesItem.from_dict(bathroom_types_item_data)



                bathroom_types.append(bathroom_types_item)


        update_vrbo_listing_rooms_response_200_data = cls(
            unit_id=unit_id,
            spaces=spaces,
            addable_types=addable_types,
            bed_types=bed_types,
            bathroom_types=bathroom_types,
        )


        update_vrbo_listing_rooms_response_200_data.additional_properties = d
        return update_vrbo_listing_rooms_response_200_data

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
