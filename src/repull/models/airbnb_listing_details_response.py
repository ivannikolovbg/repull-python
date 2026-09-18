from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.airbnb_listing_details_response_check_in_option_type_0 import AirbnbListingDetailsResponseCheckInOptionType0





T = TypeVar("T", bound="AirbnbListingDetailsResponse")



@_attrs_define
class AirbnbListingDetailsResponse:
    """ The Airbnb-side detail row(s) for the listing, from the local mirror. One entry per Airbnb connection.

        Attributes:
            listing_airbnb_id (str | Unset):
            name (None | str | Unset):
            property_type_group (None | str | Unset):
            property_type_category (None | str | Unset):
            room_type_category (None | str | Unset):
            person_capacity (int | None | Unset):
            bedrooms (int | None | Unset):
            beds (int | None | Unset):
            bathrooms (None | str | Unset):
            has_availability (bool | None | Unset): Whether the Airbnb listing is live. `false` means unlisted on Airbnb —
                unrelated to the Repull record being active.
            check_in_option (AirbnbListingDetailsResponseCheckInOptionType0 | None | Unset): `{ category, instruction }` —
                how the guest gets in.
            listing_nickname (None | str | Unset):
            locked_fields (list[str] | Unset): Attributes Airbnb refuses to change on this listing.
            updated_at (datetime.datetime | None | Unset):
     """

    listing_airbnb_id: str | Unset = UNSET
    name: None | str | Unset = UNSET
    property_type_group: None | str | Unset = UNSET
    property_type_category: None | str | Unset = UNSET
    room_type_category: None | str | Unset = UNSET
    person_capacity: int | None | Unset = UNSET
    bedrooms: int | None | Unset = UNSET
    beds: int | None | Unset = UNSET
    bathrooms: None | str | Unset = UNSET
    has_availability: bool | None | Unset = UNSET
    check_in_option: AirbnbListingDetailsResponseCheckInOptionType0 | None | Unset = UNSET
    listing_nickname: None | str | Unset = UNSET
    locked_fields: list[str] | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.airbnb_listing_details_response_check_in_option_type_0 import AirbnbListingDetailsResponseCheckInOptionType0
        listing_airbnb_id = self.listing_airbnb_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        property_type_group: None | str | Unset
        if isinstance(self.property_type_group, Unset):
            property_type_group = UNSET
        else:
            property_type_group = self.property_type_group

        property_type_category: None | str | Unset
        if isinstance(self.property_type_category, Unset):
            property_type_category = UNSET
        else:
            property_type_category = self.property_type_category

        room_type_category: None | str | Unset
        if isinstance(self.room_type_category, Unset):
            room_type_category = UNSET
        else:
            room_type_category = self.room_type_category

        person_capacity: int | None | Unset
        if isinstance(self.person_capacity, Unset):
            person_capacity = UNSET
        else:
            person_capacity = self.person_capacity

        bedrooms: int | None | Unset
        if isinstance(self.bedrooms, Unset):
            bedrooms = UNSET
        else:
            bedrooms = self.bedrooms

        beds: int | None | Unset
        if isinstance(self.beds, Unset):
            beds = UNSET
        else:
            beds = self.beds

        bathrooms: None | str | Unset
        if isinstance(self.bathrooms, Unset):
            bathrooms = UNSET
        else:
            bathrooms = self.bathrooms

        has_availability: bool | None | Unset
        if isinstance(self.has_availability, Unset):
            has_availability = UNSET
        else:
            has_availability = self.has_availability

        check_in_option: dict[str, Any] | None | Unset
        if isinstance(self.check_in_option, Unset):
            check_in_option = UNSET
        elif isinstance(self.check_in_option, AirbnbListingDetailsResponseCheckInOptionType0):
            check_in_option = self.check_in_option.to_dict()
        else:
            check_in_option = self.check_in_option

        listing_nickname: None | str | Unset
        if isinstance(self.listing_nickname, Unset):
            listing_nickname = UNSET
        else:
            listing_nickname = self.listing_nickname

        locked_fields: list[str] | Unset = UNSET
        if not isinstance(self.locked_fields, Unset):
            locked_fields = self.locked_fields



        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if listing_airbnb_id is not UNSET:
            field_dict["listingAirbnbId"] = listing_airbnb_id
        if name is not UNSET:
            field_dict["name"] = name
        if property_type_group is not UNSET:
            field_dict["propertyTypeGroup"] = property_type_group
        if property_type_category is not UNSET:
            field_dict["propertyTypeCategory"] = property_type_category
        if room_type_category is not UNSET:
            field_dict["roomTypeCategory"] = room_type_category
        if person_capacity is not UNSET:
            field_dict["personCapacity"] = person_capacity
        if bedrooms is not UNSET:
            field_dict["bedrooms"] = bedrooms
        if beds is not UNSET:
            field_dict["beds"] = beds
        if bathrooms is not UNSET:
            field_dict["bathrooms"] = bathrooms
        if has_availability is not UNSET:
            field_dict["hasAvailability"] = has_availability
        if check_in_option is not UNSET:
            field_dict["checkInOption"] = check_in_option
        if listing_nickname is not UNSET:
            field_dict["listingNickname"] = listing_nickname
        if locked_fields is not UNSET:
            field_dict["lockedFields"] = locked_fields
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.airbnb_listing_details_response_check_in_option_type_0 import AirbnbListingDetailsResponseCheckInOptionType0
        d = dict(src_dict)
        listing_airbnb_id = d.pop("listingAirbnbId", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_property_type_group(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        property_type_group = _parse_property_type_group(d.pop("propertyTypeGroup", UNSET))


        def _parse_property_type_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        property_type_category = _parse_property_type_category(d.pop("propertyTypeCategory", UNSET))


        def _parse_room_type_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        room_type_category = _parse_room_type_category(d.pop("roomTypeCategory", UNSET))


        def _parse_person_capacity(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        person_capacity = _parse_person_capacity(d.pop("personCapacity", UNSET))


        def _parse_bedrooms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        bedrooms = _parse_bedrooms(d.pop("bedrooms", UNSET))


        def _parse_beds(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        beds = _parse_beds(d.pop("beds", UNSET))


        def _parse_bathrooms(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bathrooms = _parse_bathrooms(d.pop("bathrooms", UNSET))


        def _parse_has_availability(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        has_availability = _parse_has_availability(d.pop("hasAvailability", UNSET))


        def _parse_check_in_option(data: object) -> AirbnbListingDetailsResponseCheckInOptionType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                check_in_option_type_0 = AirbnbListingDetailsResponseCheckInOptionType0.from_dict(data)



                return check_in_option_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AirbnbListingDetailsResponseCheckInOptionType0 | None | Unset, data)

        check_in_option = _parse_check_in_option(d.pop("checkInOption", UNSET))


        def _parse_listing_nickname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        listing_nickname = _parse_listing_nickname(d.pop("listingNickname", UNSET))


        locked_fields = cast(list[str], d.pop("lockedFields", UNSET))


        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = isoparse(data)



                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updatedAt", UNSET))


        airbnb_listing_details_response = cls(
            listing_airbnb_id=listing_airbnb_id,
            name=name,
            property_type_group=property_type_group,
            property_type_category=property_type_category,
            room_type_category=room_type_category,
            person_capacity=person_capacity,
            bedrooms=bedrooms,
            beds=beds,
            bathrooms=bathrooms,
            has_availability=has_availability,
            check_in_option=check_in_option,
            listing_nickname=listing_nickname,
            locked_fields=locked_fields,
            updated_at=updated_at,
        )


        airbnb_listing_details_response.additional_properties = d
        return airbnb_listing_details_response

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
