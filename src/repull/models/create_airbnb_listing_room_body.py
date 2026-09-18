from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_airbnb_listing_room_body_room_type import CreateAirbnbListingRoomBodyRoomType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.create_airbnb_listing_room_body_beds_item import CreateAirbnbListingRoomBodyBedsItem
  from ..models.create_airbnb_listing_room_body_metadata import CreateAirbnbListingRoomBodyMetadata
  from ..models.create_airbnb_listing_room_body_room_amenities_item import CreateAirbnbListingRoomBodyRoomAmenitiesItem





T = TypeVar("T", bound="CreateAirbnbListingRoomBody")



@_attrs_define
class CreateAirbnbListingRoomBody:
    """ 
        Attributes:
            room_number (int): The room's position among the listing's rooms. Airbnb keys rooms of the same type by this
                number, so two bedrooms are 1 and 2.
            room_type (CreateAirbnbListingRoomBodyRoomType):
            beds (list[CreateAirbnbListingRoomBodyBedsItem] | Unset): The room's whole sleeping arrangement. Replaces what
                is there — send every bed, not just the changed one.
            room_amenities (list[CreateAirbnbListingRoomBodyRoomAmenitiesItem] | Unset): Amenities attached to this room,
                not to the listing.
            is_private (bool | Unset):
            metadata (CreateAirbnbListingRoomBodyMetadata | Unset):
            listing_id (int | str | Unset): Accepted and ignored — the listing comes from the path.
     """

    room_number: int
    room_type: CreateAirbnbListingRoomBodyRoomType
    beds: list[CreateAirbnbListingRoomBodyBedsItem] | Unset = UNSET
    room_amenities: list[CreateAirbnbListingRoomBodyRoomAmenitiesItem] | Unset = UNSET
    is_private: bool | Unset = UNSET
    metadata: CreateAirbnbListingRoomBodyMetadata | Unset = UNSET
    listing_id: int | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.create_airbnb_listing_room_body_beds_item import CreateAirbnbListingRoomBodyBedsItem
        from ..models.create_airbnb_listing_room_body_metadata import CreateAirbnbListingRoomBodyMetadata
        from ..models.create_airbnb_listing_room_body_room_amenities_item import CreateAirbnbListingRoomBodyRoomAmenitiesItem
        room_number = self.room_number

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

        listing_id: int | str | Unset
        if isinstance(self.listing_id, Unset):
            listing_id = UNSET
        else:
            listing_id = self.listing_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "room_number": room_number,
            "room_type": room_type,
        })
        if beds is not UNSET:
            field_dict["beds"] = beds
        if room_amenities is not UNSET:
            field_dict["room_amenities"] = room_amenities
        if is_private is not UNSET:
            field_dict["is_private"] = is_private
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if listing_id is not UNSET:
            field_dict["listing_id"] = listing_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_airbnb_listing_room_body_beds_item import CreateAirbnbListingRoomBodyBedsItem
        from ..models.create_airbnb_listing_room_body_metadata import CreateAirbnbListingRoomBodyMetadata
        from ..models.create_airbnb_listing_room_body_room_amenities_item import CreateAirbnbListingRoomBodyRoomAmenitiesItem
        d = dict(src_dict)
        room_number = d.pop("room_number")

        room_type = CreateAirbnbListingRoomBodyRoomType(d.pop("room_type"))




        _beds = d.pop("beds", UNSET)
        beds: list[CreateAirbnbListingRoomBodyBedsItem] | Unset = UNSET
        if _beds is not UNSET:
            beds = []
            for beds_item_data in _beds:
                beds_item = CreateAirbnbListingRoomBodyBedsItem.from_dict(beds_item_data)



                beds.append(beds_item)


        _room_amenities = d.pop("room_amenities", UNSET)
        room_amenities: list[CreateAirbnbListingRoomBodyRoomAmenitiesItem] | Unset = UNSET
        if _room_amenities is not UNSET:
            room_amenities = []
            for room_amenities_item_data in _room_amenities:
                room_amenities_item = CreateAirbnbListingRoomBodyRoomAmenitiesItem.from_dict(room_amenities_item_data)



                room_amenities.append(room_amenities_item)


        is_private = d.pop("is_private", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: CreateAirbnbListingRoomBodyMetadata | Unset
        if isinstance(_metadata,  Unset):
            metadata = UNSET
        else:
            metadata = CreateAirbnbListingRoomBodyMetadata.from_dict(_metadata)




        def _parse_listing_id(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        listing_id = _parse_listing_id(d.pop("listing_id", UNSET))


        create_airbnb_listing_room_body = cls(
            room_number=room_number,
            room_type=room_type,
            beds=beds,
            room_amenities=room_amenities,
            is_private=is_private,
            metadata=metadata,
            listing_id=listing_id,
        )

        return create_airbnb_listing_room_body

