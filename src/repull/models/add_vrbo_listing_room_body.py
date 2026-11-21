from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.add_vrbo_listing_room_body_amenities_type_0 import AddVrboListingRoomBodyAmenitiesType0
  from ..models.add_vrbo_listing_room_body_amenities_type_1_item import AddVrboListingRoomBodyAmenitiesType1Item
  from ..models.add_vrbo_listing_room_body_beds_item import AddVrboListingRoomBodyBedsItem





T = TypeVar("T", bound="AddVrboListingRoomBody")



@_attrs_define
class AddVrboListingRoomBody:
    """ 
        Attributes:
            room_type (str):  Example: bedroom.
            room_number (int | Unset): Names the room "Bedroom 2" etc. when no `name` is given.
            name (str | Unset):
            description (str | Unset): Vrbo cannot clear a room description once set.
            sub_type (str | Unset): Bathrooms: FULL_BATH (default) or NO_TUB_OR_SHOWER (half bath). Example: FULL_BATH.
            beds (list[AddVrboListingRoomBodyBedsItem] | Unset): The room's whole sleeping arrangement: every bed, not just
                the changed one.
            amenities (AddVrboListingRoomBodyAmenitiesType0 | list[AddVrboListingRoomBodyAmenitiesType1Item] | Unset):
                `{amenityId: true|false}` or `[{id, selected, detail?}]` — only the ones given change. Ids are in GET …/rooms.
     """

    room_type: str
    room_number: int | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    sub_type: str | Unset = UNSET
    beds: list[AddVrboListingRoomBodyBedsItem] | Unset = UNSET
    amenities: AddVrboListingRoomBodyAmenitiesType0 | list[AddVrboListingRoomBodyAmenitiesType1Item] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.add_vrbo_listing_room_body_amenities_type_0 import AddVrboListingRoomBodyAmenitiesType0
        from ..models.add_vrbo_listing_room_body_amenities_type_1_item import AddVrboListingRoomBodyAmenitiesType1Item
        from ..models.add_vrbo_listing_room_body_beds_item import AddVrboListingRoomBodyBedsItem
        room_type = self.room_type

        room_number = self.room_number

        name = self.name

        description = self.description

        sub_type = self.sub_type

        beds: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.beds, Unset):
            beds = []
            for beds_item_data in self.beds:
                beds_item = beds_item_data.to_dict()
                beds.append(beds_item)



        amenities: dict[str, Any] | list[dict[str, Any]] | Unset
        if isinstance(self.amenities, Unset):
            amenities = UNSET
        elif isinstance(self.amenities, AddVrboListingRoomBodyAmenitiesType0):
            amenities = self.amenities.to_dict()
        else:
            amenities = []
            for amenities_type_1_item_data in self.amenities:
                amenities_type_1_item = amenities_type_1_item_data.to_dict()
                amenities.append(amenities_type_1_item)





        field_dict: dict[str, Any] = {}

        field_dict.update({
            "room_type": room_type,
        })
        if room_number is not UNSET:
            field_dict["room_number"] = room_number
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if sub_type is not UNSET:
            field_dict["sub_type"] = sub_type
        if beds is not UNSET:
            field_dict["beds"] = beds
        if amenities is not UNSET:
            field_dict["amenities"] = amenities

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_vrbo_listing_room_body_amenities_type_0 import AddVrboListingRoomBodyAmenitiesType0
        from ..models.add_vrbo_listing_room_body_amenities_type_1_item import AddVrboListingRoomBodyAmenitiesType1Item
        from ..models.add_vrbo_listing_room_body_beds_item import AddVrboListingRoomBodyBedsItem
        d = dict(src_dict)
        room_type = d.pop("room_type")

        room_number = d.pop("room_number", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        sub_type = d.pop("sub_type", UNSET)

        _beds = d.pop("beds", UNSET)
        beds: list[AddVrboListingRoomBodyBedsItem] | Unset = UNSET
        if _beds is not UNSET:
            beds = []
            for beds_item_data in _beds:
                beds_item = AddVrboListingRoomBodyBedsItem.from_dict(beds_item_data)



                beds.append(beds_item)


        def _parse_amenities(data: object) -> AddVrboListingRoomBodyAmenitiesType0 | list[AddVrboListingRoomBodyAmenitiesType1Item] | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                amenities_type_0 = AddVrboListingRoomBodyAmenitiesType0.from_dict(data)



                return amenities_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, list):
                raise TypeError()
            amenities_type_1 = []
            _amenities_type_1 = data
            for amenities_type_1_item_data in (_amenities_type_1):
                amenities_type_1_item = AddVrboListingRoomBodyAmenitiesType1Item.from_dict(amenities_type_1_item_data)



                amenities_type_1.append(amenities_type_1_item)

            return amenities_type_1

        amenities = _parse_amenities(d.pop("amenities", UNSET))


        add_vrbo_listing_room_body = cls(
            room_type=room_type,
            room_number=room_number,
            name=name,
            description=description,
            sub_type=sub_type,
            beds=beds,
            amenities=amenities,
        )

        return add_vrbo_listing_room_body

