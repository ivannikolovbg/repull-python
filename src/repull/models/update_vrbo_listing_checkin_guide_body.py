from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_vrbo_listing_checkin_guide_body_access import UpdateVrboListingCheckinGuideBodyAccess
  from ..models.update_vrbo_listing_checkin_guide_body_amenities import UpdateVrboListingCheckinGuideBodyAmenities
  from ..models.update_vrbo_listing_checkin_guide_body_check_in import UpdateVrboListingCheckinGuideBodyCheckIn
  from ..models.update_vrbo_listing_checkin_guide_body_check_out import UpdateVrboListingCheckinGuideBodyCheckOut
  from ..models.update_vrbo_listing_checkin_guide_body_driving_directions import UpdateVrboListingCheckinGuideBodyDrivingDirections
  from ..models.update_vrbo_listing_checkin_guide_body_parking_directions import UpdateVrboListingCheckinGuideBodyParkingDirections
  from ..models.update_vrbo_listing_checkin_guide_body_wifi import UpdateVrboListingCheckinGuideBodyWifi





T = TypeVar("T", bound="UpdateVrboListingCheckinGuideBody")



@_attrs_define
class UpdateVrboListingCheckinGuideBody:
    """ 
        Attributes:
            check_in (UpdateVrboListingCheckinGuideBodyCheckIn | Unset):
            check_out (UpdateVrboListingCheckinGuideBodyCheckOut | Unset):
            driving_directions (UpdateVrboListingCheckinGuideBodyDrivingDirections | Unset):
            parking_directions (UpdateVrboListingCheckinGuideBodyParkingDirections | Unset):
            wifi (UpdateVrboListingCheckinGuideBodyWifi | Unset):
            access (UpdateVrboListingCheckinGuideBodyAccess | Unset):
            amenities (UpdateVrboListingCheckinGuideBodyAmenities | Unset): `{AMENITY_ID: {instructions}}` — notes are one-
                way (not removable).
     """

    check_in: UpdateVrboListingCheckinGuideBodyCheckIn | Unset = UNSET
    check_out: UpdateVrboListingCheckinGuideBodyCheckOut | Unset = UNSET
    driving_directions: UpdateVrboListingCheckinGuideBodyDrivingDirections | Unset = UNSET
    parking_directions: UpdateVrboListingCheckinGuideBodyParkingDirections | Unset = UNSET
    wifi: UpdateVrboListingCheckinGuideBodyWifi | Unset = UNSET
    access: UpdateVrboListingCheckinGuideBodyAccess | Unset = UNSET
    amenities: UpdateVrboListingCheckinGuideBodyAmenities | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_vrbo_listing_checkin_guide_body_access import UpdateVrboListingCheckinGuideBodyAccess
        from ..models.update_vrbo_listing_checkin_guide_body_amenities import UpdateVrboListingCheckinGuideBodyAmenities
        from ..models.update_vrbo_listing_checkin_guide_body_check_in import UpdateVrboListingCheckinGuideBodyCheckIn
        from ..models.update_vrbo_listing_checkin_guide_body_check_out import UpdateVrboListingCheckinGuideBodyCheckOut
        from ..models.update_vrbo_listing_checkin_guide_body_driving_directions import UpdateVrboListingCheckinGuideBodyDrivingDirections
        from ..models.update_vrbo_listing_checkin_guide_body_parking_directions import UpdateVrboListingCheckinGuideBodyParkingDirections
        from ..models.update_vrbo_listing_checkin_guide_body_wifi import UpdateVrboListingCheckinGuideBodyWifi
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
        from ..models.update_vrbo_listing_checkin_guide_body_access import UpdateVrboListingCheckinGuideBodyAccess
        from ..models.update_vrbo_listing_checkin_guide_body_amenities import UpdateVrboListingCheckinGuideBodyAmenities
        from ..models.update_vrbo_listing_checkin_guide_body_check_in import UpdateVrboListingCheckinGuideBodyCheckIn
        from ..models.update_vrbo_listing_checkin_guide_body_check_out import UpdateVrboListingCheckinGuideBodyCheckOut
        from ..models.update_vrbo_listing_checkin_guide_body_driving_directions import UpdateVrboListingCheckinGuideBodyDrivingDirections
        from ..models.update_vrbo_listing_checkin_guide_body_parking_directions import UpdateVrboListingCheckinGuideBodyParkingDirections
        from ..models.update_vrbo_listing_checkin_guide_body_wifi import UpdateVrboListingCheckinGuideBodyWifi
        d = dict(src_dict)
        _check_in = d.pop("checkIn", UNSET)
        check_in: UpdateVrboListingCheckinGuideBodyCheckIn | Unset
        if isinstance(_check_in,  Unset):
            check_in = UNSET
        else:
            check_in = UpdateVrboListingCheckinGuideBodyCheckIn.from_dict(_check_in)




        _check_out = d.pop("checkOut", UNSET)
        check_out: UpdateVrboListingCheckinGuideBodyCheckOut | Unset
        if isinstance(_check_out,  Unset):
            check_out = UNSET
        else:
            check_out = UpdateVrboListingCheckinGuideBodyCheckOut.from_dict(_check_out)




        _driving_directions = d.pop("drivingDirections", UNSET)
        driving_directions: UpdateVrboListingCheckinGuideBodyDrivingDirections | Unset
        if isinstance(_driving_directions,  Unset):
            driving_directions = UNSET
        else:
            driving_directions = UpdateVrboListingCheckinGuideBodyDrivingDirections.from_dict(_driving_directions)




        _parking_directions = d.pop("parkingDirections", UNSET)
        parking_directions: UpdateVrboListingCheckinGuideBodyParkingDirections | Unset
        if isinstance(_parking_directions,  Unset):
            parking_directions = UNSET
        else:
            parking_directions = UpdateVrboListingCheckinGuideBodyParkingDirections.from_dict(_parking_directions)




        _wifi = d.pop("wifi", UNSET)
        wifi: UpdateVrboListingCheckinGuideBodyWifi | Unset
        if isinstance(_wifi,  Unset):
            wifi = UNSET
        else:
            wifi = UpdateVrboListingCheckinGuideBodyWifi.from_dict(_wifi)




        _access = d.pop("access", UNSET)
        access: UpdateVrboListingCheckinGuideBodyAccess | Unset
        if isinstance(_access,  Unset):
            access = UNSET
        else:
            access = UpdateVrboListingCheckinGuideBodyAccess.from_dict(_access)




        _amenities = d.pop("amenities", UNSET)
        amenities: UpdateVrboListingCheckinGuideBodyAmenities | Unset
        if isinstance(_amenities,  Unset):
            amenities = UNSET
        else:
            amenities = UpdateVrboListingCheckinGuideBodyAmenities.from_dict(_amenities)




        update_vrbo_listing_checkin_guide_body = cls(
            check_in=check_in,
            check_out=check_out,
            driving_directions=driving_directions,
            parking_directions=parking_directions,
            wifi=wifi,
            access=access,
            amenities=amenities,
        )

        return update_vrbo_listing_checkin_guide_body

