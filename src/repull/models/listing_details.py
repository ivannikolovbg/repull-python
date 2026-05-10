from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ListingDetails")



@_attrs_define
class ListingDetails:
    """ Structural detail slab for a listing — bedrooms/bathrooms/beds, person capacity, check-in window, wifi credentials,
    house manual, directions. Sourced from `listings_details` (one row per listing). Surfaced on `GET /v1/listings/{id}`
    and `GET /v1/listings` only when the caller passes `?include=details`. All fields are individually nullable.

        Attributes:
            property_type (None | str | Unset): Specific property type (e.g. `apartment`, `townhouse`, `cabin`).
            property_type_category (None | str | Unset): Coarser grouping above propertyType (e.g. `house`, `apartment`).
            room_type_category (None | str | Unset): Sleeping arrangement (e.g. `entire_home`, `private_room`,
                `shared_room`).
            bedrooms (int | None | Unset):
            bathrooms (None | str | Unset): Numeric value carried as a string to preserve fractional bathrooms (e.g.
                `"1.5"`).
            beds (int | None | Unset):
            person_capacity (int | None | Unset): Maximum guest capacity.
            check_in_time_start (None | str | Unset): Earliest check-in time, free-form (e.g. `"15:00"`, `"3 PM"`,
                `"flexible"`).
            check_in_time_end (None | str | Unset): Latest check-in time.
            check_out_time (None | str | Unset): Check-out time.
            min_nights (int | None | Unset):
            max_nights (int | None | Unset):
            advance_booking_days (int | None | Unset): How far in advance bookings are allowed.
            turnover_days (int | None | Unset): Required gap (in days) between consecutive bookings.
            wifi_network (None | str | Unset):
            wifi_password (None | str | Unset):
            house_manual (None | str | Unset): Long-form house manual / welcome guide.
            directions (None | str | Unset): Long-form arrival directions.
            property_size (Any | Unset): Structured size info (JSON; e.g. `{ "value": 65, "unit": "sqm" }`). Shape evolves
                with the listings_details schema.
            year_built (int | None | Unset):
            number_of_floors (int | None | Unset): Total floors in the building.
            listing_floor (int | None | Unset): Which floor the listing is on.
     """

    property_type: None | str | Unset = UNSET
    property_type_category: None | str | Unset = UNSET
    room_type_category: None | str | Unset = UNSET
    bedrooms: int | None | Unset = UNSET
    bathrooms: None | str | Unset = UNSET
    beds: int | None | Unset = UNSET
    person_capacity: int | None | Unset = UNSET
    check_in_time_start: None | str | Unset = UNSET
    check_in_time_end: None | str | Unset = UNSET
    check_out_time: None | str | Unset = UNSET
    min_nights: int | None | Unset = UNSET
    max_nights: int | None | Unset = UNSET
    advance_booking_days: int | None | Unset = UNSET
    turnover_days: int | None | Unset = UNSET
    wifi_network: None | str | Unset = UNSET
    wifi_password: None | str | Unset = UNSET
    house_manual: None | str | Unset = UNSET
    directions: None | str | Unset = UNSET
    property_size: Any | Unset = UNSET
    year_built: int | None | Unset = UNSET
    number_of_floors: int | None | Unset = UNSET
    listing_floor: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        property_type: None | str | Unset
        if isinstance(self.property_type, Unset):
            property_type = UNSET
        else:
            property_type = self.property_type

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

        bedrooms: int | None | Unset
        if isinstance(self.bedrooms, Unset):
            bedrooms = UNSET
        else:
            bedrooms = self.bedrooms

        bathrooms: None | str | Unset
        if isinstance(self.bathrooms, Unset):
            bathrooms = UNSET
        else:
            bathrooms = self.bathrooms

        beds: int | None | Unset
        if isinstance(self.beds, Unset):
            beds = UNSET
        else:
            beds = self.beds

        person_capacity: int | None | Unset
        if isinstance(self.person_capacity, Unset):
            person_capacity = UNSET
        else:
            person_capacity = self.person_capacity

        check_in_time_start: None | str | Unset
        if isinstance(self.check_in_time_start, Unset):
            check_in_time_start = UNSET
        else:
            check_in_time_start = self.check_in_time_start

        check_in_time_end: None | str | Unset
        if isinstance(self.check_in_time_end, Unset):
            check_in_time_end = UNSET
        else:
            check_in_time_end = self.check_in_time_end

        check_out_time: None | str | Unset
        if isinstance(self.check_out_time, Unset):
            check_out_time = UNSET
        else:
            check_out_time = self.check_out_time

        min_nights: int | None | Unset
        if isinstance(self.min_nights, Unset):
            min_nights = UNSET
        else:
            min_nights = self.min_nights

        max_nights: int | None | Unset
        if isinstance(self.max_nights, Unset):
            max_nights = UNSET
        else:
            max_nights = self.max_nights

        advance_booking_days: int | None | Unset
        if isinstance(self.advance_booking_days, Unset):
            advance_booking_days = UNSET
        else:
            advance_booking_days = self.advance_booking_days

        turnover_days: int | None | Unset
        if isinstance(self.turnover_days, Unset):
            turnover_days = UNSET
        else:
            turnover_days = self.turnover_days

        wifi_network: None | str | Unset
        if isinstance(self.wifi_network, Unset):
            wifi_network = UNSET
        else:
            wifi_network = self.wifi_network

        wifi_password: None | str | Unset
        if isinstance(self.wifi_password, Unset):
            wifi_password = UNSET
        else:
            wifi_password = self.wifi_password

        house_manual: None | str | Unset
        if isinstance(self.house_manual, Unset):
            house_manual = UNSET
        else:
            house_manual = self.house_manual

        directions: None | str | Unset
        if isinstance(self.directions, Unset):
            directions = UNSET
        else:
            directions = self.directions

        property_size = self.property_size

        year_built: int | None | Unset
        if isinstance(self.year_built, Unset):
            year_built = UNSET
        else:
            year_built = self.year_built

        number_of_floors: int | None | Unset
        if isinstance(self.number_of_floors, Unset):
            number_of_floors = UNSET
        else:
            number_of_floors = self.number_of_floors

        listing_floor: int | None | Unset
        if isinstance(self.listing_floor, Unset):
            listing_floor = UNSET
        else:
            listing_floor = self.listing_floor


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if property_type is not UNSET:
            field_dict["propertyType"] = property_type
        if property_type_category is not UNSET:
            field_dict["propertyTypeCategory"] = property_type_category
        if room_type_category is not UNSET:
            field_dict["roomTypeCategory"] = room_type_category
        if bedrooms is not UNSET:
            field_dict["bedrooms"] = bedrooms
        if bathrooms is not UNSET:
            field_dict["bathrooms"] = bathrooms
        if beds is not UNSET:
            field_dict["beds"] = beds
        if person_capacity is not UNSET:
            field_dict["personCapacity"] = person_capacity
        if check_in_time_start is not UNSET:
            field_dict["checkInTimeStart"] = check_in_time_start
        if check_in_time_end is not UNSET:
            field_dict["checkInTimeEnd"] = check_in_time_end
        if check_out_time is not UNSET:
            field_dict["checkOutTime"] = check_out_time
        if min_nights is not UNSET:
            field_dict["minNights"] = min_nights
        if max_nights is not UNSET:
            field_dict["maxNights"] = max_nights
        if advance_booking_days is not UNSET:
            field_dict["advanceBookingDays"] = advance_booking_days
        if turnover_days is not UNSET:
            field_dict["turnoverDays"] = turnover_days
        if wifi_network is not UNSET:
            field_dict["wifiNetwork"] = wifi_network
        if wifi_password is not UNSET:
            field_dict["wifiPassword"] = wifi_password
        if house_manual is not UNSET:
            field_dict["houseManual"] = house_manual
        if directions is not UNSET:
            field_dict["directions"] = directions
        if property_size is not UNSET:
            field_dict["propertySize"] = property_size
        if year_built is not UNSET:
            field_dict["yearBuilt"] = year_built
        if number_of_floors is not UNSET:
            field_dict["numberOfFloors"] = number_of_floors
        if listing_floor is not UNSET:
            field_dict["listingFloor"] = listing_floor

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_property_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        property_type = _parse_property_type(d.pop("propertyType", UNSET))


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


        def _parse_bedrooms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        bedrooms = _parse_bedrooms(d.pop("bedrooms", UNSET))


        def _parse_bathrooms(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bathrooms = _parse_bathrooms(d.pop("bathrooms", UNSET))


        def _parse_beds(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        beds = _parse_beds(d.pop("beds", UNSET))


        def _parse_person_capacity(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        person_capacity = _parse_person_capacity(d.pop("personCapacity", UNSET))


        def _parse_check_in_time_start(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        check_in_time_start = _parse_check_in_time_start(d.pop("checkInTimeStart", UNSET))


        def _parse_check_in_time_end(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        check_in_time_end = _parse_check_in_time_end(d.pop("checkInTimeEnd", UNSET))


        def _parse_check_out_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        check_out_time = _parse_check_out_time(d.pop("checkOutTime", UNSET))


        def _parse_min_nights(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_nights = _parse_min_nights(d.pop("minNights", UNSET))


        def _parse_max_nights(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_nights = _parse_max_nights(d.pop("maxNights", UNSET))


        def _parse_advance_booking_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        advance_booking_days = _parse_advance_booking_days(d.pop("advanceBookingDays", UNSET))


        def _parse_turnover_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        turnover_days = _parse_turnover_days(d.pop("turnoverDays", UNSET))


        def _parse_wifi_network(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        wifi_network = _parse_wifi_network(d.pop("wifiNetwork", UNSET))


        def _parse_wifi_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        wifi_password = _parse_wifi_password(d.pop("wifiPassword", UNSET))


        def _parse_house_manual(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        house_manual = _parse_house_manual(d.pop("houseManual", UNSET))


        def _parse_directions(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        directions = _parse_directions(d.pop("directions", UNSET))


        property_size = d.pop("propertySize", UNSET)

        def _parse_year_built(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        year_built = _parse_year_built(d.pop("yearBuilt", UNSET))


        def _parse_number_of_floors(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        number_of_floors = _parse_number_of_floors(d.pop("numberOfFloors", UNSET))


        def _parse_listing_floor(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        listing_floor = _parse_listing_floor(d.pop("listingFloor", UNSET))


        listing_details = cls(
            property_type=property_type,
            property_type_category=property_type_category,
            room_type_category=room_type_category,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            beds=beds,
            person_capacity=person_capacity,
            check_in_time_start=check_in_time_start,
            check_in_time_end=check_in_time_end,
            check_out_time=check_out_time,
            min_nights=min_nights,
            max_nights=max_nights,
            advance_booking_days=advance_booking_days,
            turnover_days=turnover_days,
            wifi_network=wifi_network,
            wifi_password=wifi_password,
            house_manual=house_manual,
            directions=directions,
            property_size=property_size,
            year_built=year_built,
            number_of_floors=number_of_floors,
            listing_floor=listing_floor,
        )


        listing_details.additional_properties = d
        return listing_details

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
