from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_vrbo_listing_welcome_guide_body_access import UpdateVrboListingWelcomeGuideBodyAccess
  from ..models.update_vrbo_listing_welcome_guide_body_amenities import UpdateVrboListingWelcomeGuideBodyAmenities
  from ..models.update_vrbo_listing_welcome_guide_body_check_in import UpdateVrboListingWelcomeGuideBodyCheckIn
  from ..models.update_vrbo_listing_welcome_guide_body_check_out import UpdateVrboListingWelcomeGuideBodyCheckOut
  from ..models.update_vrbo_listing_welcome_guide_body_driving_directions import UpdateVrboListingWelcomeGuideBodyDrivingDirections
  from ..models.update_vrbo_listing_welcome_guide_body_parking_directions import UpdateVrboListingWelcomeGuideBodyParkingDirections
  from ..models.update_vrbo_listing_welcome_guide_body_wifi import UpdateVrboListingWelcomeGuideBodyWifi





T = TypeVar("T", bound="UpdateVrboListingWelcomeGuideBody")



@_attrs_define
class UpdateVrboListingWelcomeGuideBody:
    """ 
        Attributes:
            check_in (UpdateVrboListingWelcomeGuideBodyCheckIn | Unset):
            check_out (UpdateVrboListingWelcomeGuideBodyCheckOut | Unset):
            driving_directions (UpdateVrboListingWelcomeGuideBodyDrivingDirections | Unset):
            parking_directions (UpdateVrboListingWelcomeGuideBodyParkingDirections | Unset):
            wifi (UpdateVrboListingWelcomeGuideBodyWifi | Unset):
            access (UpdateVrboListingWelcomeGuideBodyAccess | Unset):
            amenities (UpdateVrboListingWelcomeGuideBodyAmenities | Unset): `{AMENITY_ID: {instructions}}` — notes are one-
                way (not removable).
     """

    check_in: UpdateVrboListingWelcomeGuideBodyCheckIn | Unset = UNSET
    check_out: UpdateVrboListingWelcomeGuideBodyCheckOut | Unset = UNSET
    driving_directions: UpdateVrboListingWelcomeGuideBodyDrivingDirections | Unset = UNSET
    parking_directions: UpdateVrboListingWelcomeGuideBodyParkingDirections | Unset = UNSET
    wifi: UpdateVrboListingWelcomeGuideBodyWifi | Unset = UNSET
    access: UpdateVrboListingWelcomeGuideBodyAccess | Unset = UNSET
    amenities: UpdateVrboListingWelcomeGuideBodyAmenities | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_vrbo_listing_welcome_guide_body_access import UpdateVrboListingWelcomeGuideBodyAccess
        from ..models.update_vrbo_listing_welcome_guide_body_amenities import UpdateVrboListingWelcomeGuideBodyAmenities
        from ..models.update_vrbo_listing_welcome_guide_body_check_in import UpdateVrboListingWelcomeGuideBodyCheckIn
        from ..models.update_vrbo_listing_welcome_guide_body_check_out import UpdateVrboListingWelcomeGuideBodyCheckOut
        from ..models.update_vrbo_listing_welcome_guide_body_driving_directions import UpdateVrboListingWelcomeGuideBodyDrivingDirections
        from ..models.update_vrbo_listing_welcome_guide_body_parking_directions import UpdateVrboListingWelcomeGuideBodyParkingDirections
        from ..models.update_vrbo_listing_welcome_guide_body_wifi import UpdateVrboListingWelcomeGuideBodyWifi
        check_in: dict[str, Any] | Unset = UNSET
        if not isinstance(self.check_in, Unset):
            check_in = self.check_in.to_dict()

        check_out: dict[str, Any] | Unset = UNSET
        if not isinstance(self.check_out, Unset):
            check_out = self.check_out.to_dict()

        driving_directions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.driving_directions, Unset):
            driving_directions = self.driving_directions.to_dict()

        parking_directions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parking_directions, Unset):
            parking_directions = self.parking_directions.to_dict()

        wifi: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wifi, Unset):
            wifi = self.wifi.to_dict()

        access: dict[str, Any] | Unset = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.to_dict()

        amenities: dict[str, Any] | Unset = UNSET
        if not isinstance(self.amenities, Unset):
            amenities = self.amenities.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if check_in is not UNSET:
            field_dict["checkIn"] = check_in
        if check_out is not UNSET:
            field_dict["checkOut"] = check_out
        if driving_directions is not UNSET:
            field_dict["drivingDirections"] = driving_directions
        if parking_directions is not UNSET:
            field_dict["parkingDirections"] = parking_directions
        if wifi is not UNSET:
            field_dict["wifi"] = wifi
        if access is not UNSET:
            field_dict["access"] = access
        if amenities is not UNSET:
            field_dict["amenities"] = amenities

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_vrbo_listing_welcome_guide_body_access import UpdateVrboListingWelcomeGuideBodyAccess
        from ..models.update_vrbo_listing_welcome_guide_body_amenities import UpdateVrboListingWelcomeGuideBodyAmenities
        from ..models.update_vrbo_listing_welcome_guide_body_check_in import UpdateVrboListingWelcomeGuideBodyCheckIn
        from ..models.update_vrbo_listing_welcome_guide_body_check_out import UpdateVrboListingWelcomeGuideBodyCheckOut
        from ..models.update_vrbo_listing_welcome_guide_body_driving_directions import UpdateVrboListingWelcomeGuideBodyDrivingDirections
        from ..models.update_vrbo_listing_welcome_guide_body_parking_directions import UpdateVrboListingWelcomeGuideBodyParkingDirections
        from ..models.update_vrbo_listing_welcome_guide_body_wifi import UpdateVrboListingWelcomeGuideBodyWifi
        d = dict(src_dict)
        _check_in = d.pop("checkIn", UNSET)
        check_in: UpdateVrboListingWelcomeGuideBodyCheckIn | Unset
        if isinstance(_check_in,  Unset):
            check_in = UNSET
        else:
            check_in = UpdateVrboListingWelcomeGuideBodyCheckIn.from_dict(_check_in)




        _check_out = d.pop("checkOut", UNSET)
        check_out: UpdateVrboListingWelcomeGuideBodyCheckOut | Unset
        if isinstance(_check_out,  Unset):
            check_out = UNSET
        else:
            check_out = UpdateVrboListingWelcomeGuideBodyCheckOut.from_dict(_check_out)




        _driving_directions = d.pop("drivingDirections", UNSET)
        driving_directions: UpdateVrboListingWelcomeGuideBodyDrivingDirections | Unset
        if isinstance(_driving_directions,  Unset):
            driving_directions = UNSET
        else:
            driving_directions = UpdateVrboListingWelcomeGuideBodyDrivingDirections.from_dict(_driving_directions)




        _parking_directions = d.pop("parkingDirections", UNSET)
        parking_directions: UpdateVrboListingWelcomeGuideBodyParkingDirections | Unset
        if isinstance(_parking_directions,  Unset):
            parking_directions = UNSET
        else:
            parking_directions = UpdateVrboListingWelcomeGuideBodyParkingDirections.from_dict(_parking_directions)




        _wifi = d.pop("wifi", UNSET)
        wifi: UpdateVrboListingWelcomeGuideBodyWifi | Unset
        if isinstance(_wifi,  Unset):
            wifi = UNSET
        else:
            wifi = UpdateVrboListingWelcomeGuideBodyWifi.from_dict(_wifi)




        _access = d.pop("access", UNSET)
        access: UpdateVrboListingWelcomeGuideBodyAccess | Unset
        if isinstance(_access,  Unset):
            access = UNSET
        else:
            access = UpdateVrboListingWelcomeGuideBodyAccess.from_dict(_access)




        _amenities = d.pop("amenities", UNSET)
        amenities: UpdateVrboListingWelcomeGuideBodyAmenities | Unset
        if isinstance(_amenities,  Unset):
            amenities = UNSET
        else:
            amenities = UpdateVrboListingWelcomeGuideBodyAmenities.from_dict(_amenities)




        update_vrbo_listing_welcome_guide_body = cls(
            check_in=check_in,
            check_out=check_out,
            driving_directions=driving_directions,
            parking_directions=parking_directions,
            wifi=wifi,
            access=access,
            amenities=amenities,
        )

        return update_vrbo_listing_welcome_guide_body

