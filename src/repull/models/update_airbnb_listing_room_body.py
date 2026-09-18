from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.update_airbnb_listing_room_body_room_type import UpdateAirbnbListingRoomBodyRoomType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_airbnb_listing_room_body_beds_item import UpdateAirbnbListingRoomBodyBedsItem
  from ..models.update_airbnb_listing_room_body_metadata import UpdateAirbnbListingRoomBodyMetadata
  from ..models.update_airbnb_listing_room_body_room_amenities_item import UpdateAirbnbListingRoomBodyRoomAmenitiesItem





T = TypeVar("T", bound="UpdateAirbnbListingRoomBody")



@_attrs_define
class UpdateAirbnbListingRoomBody:
    """ At least one field. A body that changes nothing is refused rather than reported as a successful write.

        Attributes:
            room_number (int | Unset): The room's position among the listing's rooms. Airbnb keys rooms of the same type by
                this number, so two bedrooms are 1 and 2.
            room_type (UpdateAirbnbListingRoomBodyRoomType | Unset):
            beds (list[UpdateAirbnbListingRoomBodyBedsItem] | Unset): The room's whole sleeping arrangement. Replaces what
                is there — send every bed, not just the changed one.
            room_amenities (list[UpdateAirbnbListingRoomBodyRoomAmenitiesItem] | Unset): Amenities attached to this room,
                not to the listing.
            is_private (bool | Unset):
            metadata (UpdateAirbnbListingRoomBodyMetadata | Unset):
     """

    room_number: int | Unset = UNSET
    room_type: UpdateAirbnbListingRoomBodyRoomType | Unset = UNSET
    beds: list[UpdateAirbnbListingRoomBodyBedsItem] | Unset = UNSET
    room_amenities: list[UpdateAirbnbListingRoomBodyRoomAmenitiesItem] | Unset = UNSET
    is_private: bool | Unset = UNSET
    metadata: UpdateAirbnbListingRoomBodyMetadata | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_airbnb_listing_room_body_beds_item import UpdateAirbnbListingRoomBodyBedsItem
        from ..models.update_airbnb_listing_room_body_metadata import UpdateAirbnbListingRoomBodyMetadata
        from ..models.update_airbnb_listing_room_body_room_amenities_item import UpdateAirbnbListingRoomBodyRoomAmenitiesItem
        room_number = self.room_number

        room_type: str | Unset = UNSET
        if not isinstance(self.room_type, Unset):
            room_type = self.room_type.value


        beds: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.beds, Unset):
            beds = []
            for beds_item_data in self.beds:
                beds_item = beds_item_data.to_dict()
                beds.append(beds_item)



        room_amenities: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.room_amenities, Unset):
            room_amenities = []
            for room_amenities_item_data in self.room_amenities:
                room_amenities_item = room_amenities_item_data.to_dict()
                room_amenities.append(room_amenities_item)



        is_private = self.is_private

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if room_number is not UNSET:
            field_dict["room_number"] = room_number
        if room_type is not UNSET:
            field_dict["room_type"] = room_type
        if beds is not UNSET:
            field_dict["beds"] = beds
        if room_amenities is not UNSET:
            field_dict["room_amenities"] = room_amenities
        if is_private is not UNSET:
            field_dict["is_private"] = is_private
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_airbnb_listing_room_body_beds_item import UpdateAirbnbListingRoomBodyBedsItem
        from ..models.update_airbnb_listing_room_body_metadata import UpdateAirbnbListingRoomBodyMetadata
        from ..models.update_airbnb_listing_room_body_room_amenities_item import UpdateAirbnbListingRoomBodyRoomAmenitiesItem
        d = dict(src_dict)
        room_number = d.pop("room_number", UNSET)

        _room_type = d.pop("room_type", UNSET)
        room_type: UpdateAirbnbListingRoomBodyRoomType | Unset
        if isinstance(_room_type,  Unset):
            room_type = UNSET
        else:
            room_type = UpdateAirbnbListingRoomBodyRoomType(_room_type)




        _beds = d.pop("beds", UNSET)
        beds: list[UpdateAirbnbListingRoomBodyBedsItem] | Unset = UNSET
        if _beds is not UNSET:
            beds = []
            for beds_item_data in _beds:
                beds_item = UpdateAirbnbListingRoomBodyBedsItem.from_dict(beds_item_data)



                beds.append(beds_item)


        _room_amenities = d.pop("room_amenities", UNSET)
        room_amenities: list[UpdateAirbnbListingRoomBodyRoomAmenitiesItem] | Unset = UNSET
        if _room_amenities is not UNSET:
            room_amenities = []
            for room_amenities_item_data in _room_amenities:
                room_amenities_item = UpdateAirbnbListingRoomBodyRoomAmenitiesItem.from_dict(room_amenities_item_data)



                room_amenities.append(room_amenities_item)


        is_private = d.pop("is_private", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: UpdateAirbnbListingRoomBodyMetadata | Unset
        if isinstance(_metadata,  Unset):
            metadata = UNSET
        else:
            metadata = UpdateAirbnbListingRoomBodyMetadata.from_dict(_metadata)




        update_airbnb_listing_room_body = cls(
            room_number=room_number,
            room_type=room_type,
            beds=beds,
            room_amenities=room_amenities,
            is_private=is_private,
            metadata=metadata,
        )

        return update_airbnb_listing_room_body

