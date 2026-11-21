from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_vrbo_listing_rooms_body_update_item_amenities_type_0 import UpdateVrboListingRoomsBodyUpdateItemAmenitiesType0
  from ..models.update_vrbo_listing_rooms_body_update_item_amenities_type_1_item import UpdateVrboListingRoomsBodyUpdateItemAmenitiesType1Item
  from ..models.update_vrbo_listing_rooms_body_update_item_beds_item import UpdateVrboListingRoomsBodyUpdateItemBedsItem





T = TypeVar("T", bound="UpdateVrboListingRoomsBodyUpdateItem")



@_attrs_define
class UpdateVrboListingRoomsBodyUpdateItem:
    """ 
        Attributes:
            space_id (str):
            name (str | Unset):
            sub_type (str | Unset): Bathrooms: one of the read's `bathroomTypes` (FULL_BATH, HALF_BATH, …).
            description (str | Unset):
            beds (list[UpdateVrboListingRoomsBodyUpdateItemBedsItem] | Unset):
            amenities (list[UpdateVrboListingRoomsBodyUpdateItemAmenitiesType1Item] | Unset |
                UpdateVrboListingRoomsBodyUpdateItemAmenitiesType0): `{amenityId: true|false}` or `[{id, selected, detail?}]` —
                only the ones given change.
     """

    space_id: str
    name: str | Unset = UNSET
    sub_type: str | Unset = UNSET
    description: str | Unset = UNSET
    beds: list[UpdateVrboListingRoomsBodyUpdateItemBedsItem] | Unset = UNSET
    amenities: list[UpdateVrboListingRoomsBodyUpdateItemAmenitiesType1Item] | Unset | UpdateVrboListingRoomsBodyUpdateItemAmenitiesType0 = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_vrbo_listing_rooms_body_update_item_amenities_type_0 import UpdateVrboListingRoomsBodyUpdateItemAmenitiesType0
        from ..models.update_vrbo_listing_rooms_body_update_item_amenities_type_1_item import UpdateVrboListingRoomsBodyUpdateItemAmenitiesType1Item
        from ..models.update_vrbo_listing_rooms_body_update_item_beds_item import UpdateVrboListingRoomsBodyUpdateItemBedsItem
        space_id = self.space_id

        name = self.name

        sub_type = self.sub_type

        description = self.description

        beds: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.beds, Unset):
            beds = []
            for beds_item_data in self.beds:
                beds_item = beds_item_data.to_dict()
                beds.append(beds_item)



        amenities: dict[str, Any] | list[dict[str, Any]] | Unset
        if isinstance(self.amenities, Unset):
            amenities = UNSET
        elif isinstance(self.amenities, UpdateVrboListingRoomsBodyUpdateItemAmenitiesType0):
            amenities = self.amenities.to_dict()
        else:
            amenities = []
            for amenities_type_1_item_data in self.amenities:
                amenities_type_1_item = amenities_type_1_item_data.to_dict()
                amenities.append(amenities_type_1_item)





        field_dict: dict[str, Any] = {}

        field_dict.update({
            "spaceId": space_id,
        })
        if name is not UNSET:
            field_dict["name"] = name
        if sub_type is not UNSET:
            field_dict["subType"] = sub_type
        if description is not UNSET:
            field_dict["description"] = description
        if beds is not UNSET:
            field_dict["beds"] = beds
        if amenities is not UNSET:
            field_dict["amenities"] = amenities

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_vrbo_listing_rooms_body_update_item_amenities_type_0 import UpdateVrboListingRoomsBodyUpdateItemAmenitiesType0
        from ..models.update_vrbo_listing_rooms_body_update_item_amenities_type_1_item import UpdateVrboListingRoomsBodyUpdateItemAmenitiesType1Item
        from ..models.update_vrbo_listing_rooms_body_update_item_beds_item import UpdateVrboListingRoomsBodyUpdateItemBedsItem
        d = dict(src_dict)
        space_id = d.pop("spaceId")

        name = d.pop("name", UNSET)

        sub_type = d.pop("subType", UNSET)

        description = d.pop("description", UNSET)

        _beds = d.pop("beds", UNSET)
        beds: list[UpdateVrboListingRoomsBodyUpdateItemBedsItem] | Unset = UNSET
        if _beds is not UNSET:
            beds = []
            for beds_item_data in _beds:
                beds_item = UpdateVrboListingRoomsBodyUpdateItemBedsItem.from_dict(beds_item_data)



                beds.append(beds_item)


        def _parse_amenities(data: object) -> list[UpdateVrboListingRoomsBodyUpdateItemAmenitiesType1Item] | Unset | UpdateVrboListingRoomsBodyUpdateItemAmenitiesType0:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                amenities_type_0 = UpdateVrboListingRoomsBodyUpdateItemAmenitiesType0.from_dict(data)



                return amenities_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, list):
                raise TypeError()
            amenities_type_1 = []
            _amenities_type_1 = data
            for amenities_type_1_item_data in (_amenities_type_1):
                amenities_type_1_item = UpdateVrboListingRoomsBodyUpdateItemAmenitiesType1Item.from_dict(amenities_type_1_item_data)



                amenities_type_1.append(amenities_type_1_item)

            return amenities_type_1

        amenities = _parse_amenities(d.pop("amenities", UNSET))


        update_vrbo_listing_rooms_body_update_item = cls(
            space_id=space_id,
            name=name,
            sub_type=sub_type,
            description=description,
            beds=beds,
            amenities=amenities,
        )

        return update_vrbo_listing_rooms_body_update_item

