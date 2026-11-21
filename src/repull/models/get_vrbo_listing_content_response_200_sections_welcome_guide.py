from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_vrbo_listing_content_response_200_sections_welcome_guide_access_type_0 import GetVrboListingContentResponse200SectionsWelcomeGuideAccessType0
  from ..models.get_vrbo_listing_content_response_200_sections_welcome_guide_amenities import GetVrboListingContentResponse200SectionsWelcomeGuideAmenities
  from ..models.get_vrbo_listing_content_response_200_sections_welcome_guide_check_in_type_0 import GetVrboListingContentResponse200SectionsWelcomeGuideCheckInType0
  from ..models.get_vrbo_listing_content_response_200_sections_welcome_guide_check_out_type_0 import GetVrboListingContentResponse200SectionsWelcomeGuideCheckOutType0
  from ..models.get_vrbo_listing_content_response_200_sections_welcome_guide_contacts_item import GetVrboListingContentResponse200SectionsWelcomeGuideContactsItem
  from ..models.get_vrbo_listing_content_response_200_sections_welcome_guide_driving_directions_type_0 import GetVrboListingContentResponse200SectionsWelcomeGuideDrivingDirectionsType0
  from ..models.get_vrbo_listing_content_response_200_sections_welcome_guide_parking_directions_type_0 import GetVrboListingContentResponse200SectionsWelcomeGuideParkingDirectionsType0
  from ..models.get_vrbo_listing_content_response_200_sections_welcome_guide_wifi_type_0 import GetVrboListingContentResponse200SectionsWelcomeGuideWifiType0





T = TypeVar("T", bound="GetVrboListingContentResponse200SectionsWelcomeGuide")



@_attrs_define
class GetVrboListingContentResponse200SectionsWelcomeGuide:
    """ 
        Attributes:
            check_in (GetVrboListingContentResponse200SectionsWelcomeGuideCheckInType0 | None | Unset):
            check_out (GetVrboListingContentResponse200SectionsWelcomeGuideCheckOutType0 | None | Unset):
            driving_directions (GetVrboListingContentResponse200SectionsWelcomeGuideDrivingDirectionsType0 | None | Unset):
            parking_directions (GetVrboListingContentResponse200SectionsWelcomeGuideParkingDirectionsType0 | None | Unset):
            access (GetVrboListingContentResponse200SectionsWelcomeGuideAccessType0 | None | Unset):
            wifi (GetVrboListingContentResponse200SectionsWelcomeGuideWifiType0 | None | Unset):
            amenities (GetVrboListingContentResponse200SectionsWelcomeGuideAmenities | Unset): Keyed by Vrbo amenity id
                (e.g. HOT_TUB_HOSPITALITY).
            contacts (list[GetVrboListingContentResponse200SectionsWelcomeGuideContactsItem] | Unset):
     """

    check_in: GetVrboListingContentResponse200SectionsWelcomeGuideCheckInType0 | None | Unset = UNSET
    check_out: GetVrboListingContentResponse200SectionsWelcomeGuideCheckOutType0 | None | Unset = UNSET
    driving_directions: GetVrboListingContentResponse200SectionsWelcomeGuideDrivingDirectionsType0 | None | Unset = UNSET
    parking_directions: GetVrboListingContentResponse200SectionsWelcomeGuideParkingDirectionsType0 | None | Unset = UNSET
    access: GetVrboListingContentResponse200SectionsWelcomeGuideAccessType0 | None | Unset = UNSET
    wifi: GetVrboListingContentResponse200SectionsWelcomeGuideWifiType0 | None | Unset = UNSET
    amenities: GetVrboListingContentResponse200SectionsWelcomeGuideAmenities | Unset = UNSET
    contacts: list[GetVrboListingContentResponse200SectionsWelcomeGuideContactsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_vrbo_listing_content_response_200_sections_welcome_guide_access_type_0 import GetVrboListingContentResponse200SectionsWelcomeGuideAccessType0
        from ..models.get_vrbo_listing_content_response_200_sections_welcome_guide_amenities import GetVrboListingContentResponse200SectionsWelcomeGuideAmenities
        from ..models.get_vrbo_listing_content_response_200_sections_welcome_guide_check_in_type_0 import GetVrboListingContentResponse200SectionsWelcomeGuideCheckInType0
        from ..models.get_vrbo_listing_content_response_200_sections_welcome_guide_check_out_type_0 import GetVrboListingContentResponse200SectionsWelcomeGuideCheckOutType0
        from ..models.get_vrbo_listing_content_response_200_sections_welcome_guide_contacts_item import GetVrboListingContentResponse200SectionsWelcomeGuideContactsItem
        from ..models.get_vrbo_listing_content_response_200_sections_welcome_guide_driving_directions_type_0 import GetVrboListingContentResponse200SectionsWelcomeGuideDrivingDirectionsType0
        from ..models.get_vrbo_listing_content_response_200_sections_welcome_guide_parking_directions_type_0 import GetVrboListingContentResponse200SectionsWelcomeGuideParkingDirectionsType0
        from ..models.get_vrbo_listing_content_response_200_sections_welcome_guide_wifi_type_0 import GetVrboListingContentResponse200SectionsWelcomeGuideWifiType0
        check_in: dict[str, Any] | None | Unset
        if isinstance(self.check_in, Unset):
            check_in = UNSET
        elif isinstance(self.check_in, GetVrboListingContentResponse200SectionsWelcomeGuideCheckInType0):
            check_in = self.check_in.to_dict()
        else:
            check_in = self.check_in

        check_out: dict[str, Any] | None | Unset
        if isinstance(self.check_out, Unset):
            check_out = UNSET
        elif isinstance(self.check_out, GetVrboListingContentResponse200SectionsWelcomeGuideCheckOutType0):
            check_out = self.check_out.to_dict()
        else:
            check_out = self.check_out

        driving_directions: dict[str, Any] | None | Unset
        if isinstance(self.driving_directions, Unset):
            driving_directions = UNSET
        elif isinstance(self.driving_directions, GetVrboListingContentResponse200SectionsWelcomeGuideDrivingDirectionsType0):
            driving_directions = self.driving_directions.to_dict()
        else:
            driving_directions = self.driving_directions

        parking_directions: dict[str, Any] | None | Unset
        if isinstance(self.parking_directions, Unset):
            parking_directions = UNSET
        elif isinstance(self.parking_directions, GetVrboListingContentResponse200SectionsWelcomeGuideParkingDirectionsType0):
            parking_directions = self.parking_directions.to_dict()
        else:
            parking_directions = self.parking_directions

        access: dict[str, Any] | None | Unset
        if isinstance(self.access, Unset):
            access = UNSET
        elif isinstance(self.access, GetVrboListingContentResponse200SectionsWelcomeGuideAccessType0):
            access = self.access.to_dict()
        else:
            access = self.access

        wifi: dict[str, Any] | None | Unset
        if isinstance(self.wifi, Unset):
            wifi = UNSET
        elif isinstance(self.wifi, GetVrboListingContentResponse200SectionsWelcomeGuideWifiType0):
            wifi = self.wifi.to_dict()
        else:
            wifi = self.wifi

        amenities: dict[str, Any] | Unset = UNSET
        if not isinstance(self.amenities, Unset):
            amenities = self.amenities.to_dict()

        contacts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.contacts, Unset):
            contacts = []
            for contacts_item_data in self.contacts:
                contacts_item = contacts_item_data.to_dict()
                contacts.append(contacts_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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
        if access is not UNSET:
            field_dict["access"] = access
        if wifi is not UNSET:
            field_dict["wifi"] = wifi
        if amenities is not UNSET:
            field_dict["amenities"] = amenities
        if contacts is not UNSET:
            field_dict["contacts"] = contacts

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_vrbo_listing_content_response_200_sections_welcome_guide_access_type_0 import GetVrboListingContentResponse200SectionsWelcomeGuideAccessType0
        from ..models.get_vrbo_listing_content_response_200_sections_welcome_guide_amenities import GetVrboListingContentResponse200SectionsWelcomeGuideAmenities
        from ..models.get_vrbo_listing_content_response_200_sections_welcome_guide_check_in_type_0 import GetVrboListingContentResponse200SectionsWelcomeGuideCheckInType0
        from ..models.get_vrbo_listing_content_response_200_sections_welcome_guide_check_out_type_0 import GetVrboListingContentResponse200SectionsWelcomeGuideCheckOutType0
        from ..models.get_vrbo_listing_content_response_200_sections_welcome_guide_contacts_item import GetVrboListingContentResponse200SectionsWelcomeGuideContactsItem
        from ..models.get_vrbo_listing_content_response_200_sections_welcome_guide_driving_directions_type_0 import GetVrboListingContentResponse200SectionsWelcomeGuideDrivingDirectionsType0
        from ..models.get_vrbo_listing_content_response_200_sections_welcome_guide_parking_directions_type_0 import GetVrboListingContentResponse200SectionsWelcomeGuideParkingDirectionsType0
        from ..models.get_vrbo_listing_content_response_200_sections_welcome_guide_wifi_type_0 import GetVrboListingContentResponse200SectionsWelcomeGuideWifiType0
        d = dict(src_dict)
        def _parse_check_in(data: object) -> GetVrboListingContentResponse200SectionsWelcomeGuideCheckInType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                check_in_type_0 = GetVrboListingContentResponse200SectionsWelcomeGuideCheckInType0.from_dict(data)



                return check_in_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetVrboListingContentResponse200SectionsWelcomeGuideCheckInType0 | None | Unset, data)

        check_in = _parse_check_in(d.pop("checkIn", UNSET))


        def _parse_check_out(data: object) -> GetVrboListingContentResponse200SectionsWelcomeGuideCheckOutType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                check_out_type_0 = GetVrboListingContentResponse200SectionsWelcomeGuideCheckOutType0.from_dict(data)



                return check_out_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetVrboListingContentResponse200SectionsWelcomeGuideCheckOutType0 | None | Unset, data)

        check_out = _parse_check_out(d.pop("checkOut", UNSET))


        def _parse_driving_directions(data: object) -> GetVrboListingContentResponse200SectionsWelcomeGuideDrivingDirectionsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                driving_directions_type_0 = GetVrboListingContentResponse200SectionsWelcomeGuideDrivingDirectionsType0.from_dict(data)



                return driving_directions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetVrboListingContentResponse200SectionsWelcomeGuideDrivingDirectionsType0 | None | Unset, data)

        driving_directions = _parse_driving_directions(d.pop("drivingDirections", UNSET))


        def _parse_parking_directions(data: object) -> GetVrboListingContentResponse200SectionsWelcomeGuideParkingDirectionsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                parking_directions_type_0 = GetVrboListingContentResponse200SectionsWelcomeGuideParkingDirectionsType0.from_dict(data)



                return parking_directions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetVrboListingContentResponse200SectionsWelcomeGuideParkingDirectionsType0 | None | Unset, data)

        parking_directions = _parse_parking_directions(d.pop("parkingDirections", UNSET))


        def _parse_access(data: object) -> GetVrboListingContentResponse200SectionsWelcomeGuideAccessType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                access_type_0 = GetVrboListingContentResponse200SectionsWelcomeGuideAccessType0.from_dict(data)



                return access_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetVrboListingContentResponse200SectionsWelcomeGuideAccessType0 | None | Unset, data)

        access = _parse_access(d.pop("access", UNSET))


        def _parse_wifi(data: object) -> GetVrboListingContentResponse200SectionsWelcomeGuideWifiType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                wifi_type_0 = GetVrboListingContentResponse200SectionsWelcomeGuideWifiType0.from_dict(data)



                return wifi_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetVrboListingContentResponse200SectionsWelcomeGuideWifiType0 | None | Unset, data)

        wifi = _parse_wifi(d.pop("wifi", UNSET))


        _amenities = d.pop("amenities", UNSET)
        amenities: GetVrboListingContentResponse200SectionsWelcomeGuideAmenities | Unset
        if isinstance(_amenities,  Unset):
            amenities = UNSET
        else:
            amenities = GetVrboListingContentResponse200SectionsWelcomeGuideAmenities.from_dict(_amenities)




        _contacts = d.pop("contacts", UNSET)
        contacts: list[GetVrboListingContentResponse200SectionsWelcomeGuideContactsItem] | Unset = UNSET
        if _contacts is not UNSET:
            contacts = []
            for contacts_item_data in _contacts:
                contacts_item = GetVrboListingContentResponse200SectionsWelcomeGuideContactsItem.from_dict(contacts_item_data)



                contacts.append(contacts_item)


        get_vrbo_listing_content_response_200_sections_welcome_guide = cls(
            check_in=check_in,
            check_out=check_out,
            driving_directions=driving_directions,
            parking_directions=parking_directions,
            access=access,
            wifi=wifi,
            amenities=amenities,
            contacts=contacts,
        )


        get_vrbo_listing_content_response_200_sections_welcome_guide.additional_properties = d
        return get_vrbo_listing_content_response_200_sections_welcome_guide

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
