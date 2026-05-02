from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.listing_create_request_cancellation_policy import ListingCreateRequestCancellationPolicy
from ..types import UNSET, Unset






T = TypeVar("T", bound="ListingCreateRequest")



@_attrs_define
class ListingCreateRequest:
    """ Inputs for `POST /v1/listings`. Provide enough address detail (street + city + lat/lng) for downstream Airbnb
    publish to work.

        Attributes:
            name (str): Public guest-facing title Example: Sunset Loft #2.
            property_type (str | Unset):  Example: apartment.
            street (str | Unset):  Example: 123 Main St.
            city (str | Unset):  Example: Miami Beach.
            state (str | Unset):  Example: FL.
            country_code (str | Unset):  Example: US.
            lat (float | Unset):  Example: 25.7617.
            lng (float | Unset):  Example: -80.1918.
            bedrooms (int | Unset):  Example: 2.
            bathrooms (float | Unset):  Example: 1.5.
            beds (int | Unset):  Example: 2.
            person_capacity (int | Unset):  Example: 4.
            summary (str | Unset):
            description (str | Unset):
            default_daily_price (float | Unset):
            cleaning_fee (float | Unset):
            cancellation_policy (ListingCreateRequestCancellationPolicy | Unset):
            check_in_time_start (str | Unset):  Example: 15:00.
            check_out_time (str | Unset):  Example: 11:00.
            allows_pets (bool | Unset):
            allows_smoking (bool | Unset):
            allows_children (bool | Unset):
            allows_events (bool | Unset):
     """

    name: str
    property_type: str | Unset = UNSET
    street: str | Unset = UNSET
    city: str | Unset = UNSET
    state: str | Unset = UNSET
    country_code: str | Unset = UNSET
    lat: float | Unset = UNSET
    lng: float | Unset = UNSET
    bedrooms: int | Unset = UNSET
    bathrooms: float | Unset = UNSET
    beds: int | Unset = UNSET
    person_capacity: int | Unset = UNSET
    summary: str | Unset = UNSET
    description: str | Unset = UNSET
    default_daily_price: float | Unset = UNSET
    cleaning_fee: float | Unset = UNSET
    cancellation_policy: ListingCreateRequestCancellationPolicy | Unset = UNSET
    check_in_time_start: str | Unset = UNSET
    check_out_time: str | Unset = UNSET
    allows_pets: bool | Unset = UNSET
    allows_smoking: bool | Unset = UNSET
    allows_children: bool | Unset = UNSET
    allows_events: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        property_type = self.property_type

        street = self.street

        city = self.city

        state = self.state

        country_code = self.country_code

        lat = self.lat

        lng = self.lng

        bedrooms = self.bedrooms

        bathrooms = self.bathrooms

        beds = self.beds

        person_capacity = self.person_capacity

        summary = self.summary

        description = self.description

        default_daily_price = self.default_daily_price

        cleaning_fee = self.cleaning_fee

        cancellation_policy: str | Unset = UNSET
        if not isinstance(self.cancellation_policy, Unset):
            cancellation_policy = self.cancellation_policy.value


        check_in_time_start = self.check_in_time_start

        check_out_time = self.check_out_time

        allows_pets = self.allows_pets

        allows_smoking = self.allows_smoking

        allows_children = self.allows_children

        allows_events = self.allows_events


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
        })
        if property_type is not UNSET:
            field_dict["propertyType"] = property_type
        if street is not UNSET:
            field_dict["street"] = street
        if city is not UNSET:
            field_dict["city"] = city
        if state is not UNSET:
            field_dict["state"] = state
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code
        if lat is not UNSET:
            field_dict["lat"] = lat
        if lng is not UNSET:
            field_dict["lng"] = lng
        if bedrooms is not UNSET:
            field_dict["bedrooms"] = bedrooms
        if bathrooms is not UNSET:
            field_dict["bathrooms"] = bathrooms
        if beds is not UNSET:
            field_dict["beds"] = beds
        if person_capacity is not UNSET:
            field_dict["personCapacity"] = person_capacity
        if summary is not UNSET:
            field_dict["summary"] = summary
        if description is not UNSET:
            field_dict["description"] = description
        if default_daily_price is not UNSET:
            field_dict["defaultDailyPrice"] = default_daily_price
        if cleaning_fee is not UNSET:
            field_dict["cleaningFee"] = cleaning_fee
        if cancellation_policy is not UNSET:
            field_dict["cancellationPolicy"] = cancellation_policy
        if check_in_time_start is not UNSET:
            field_dict["checkInTimeStart"] = check_in_time_start
        if check_out_time is not UNSET:
            field_dict["checkOutTime"] = check_out_time
        if allows_pets is not UNSET:
            field_dict["allowsPets"] = allows_pets
        if allows_smoking is not UNSET:
            field_dict["allowsSmoking"] = allows_smoking
        if allows_children is not UNSET:
            field_dict["allowsChildren"] = allows_children
        if allows_events is not UNSET:
            field_dict["allowsEvents"] = allows_events

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        property_type = d.pop("propertyType", UNSET)

        street = d.pop("street", UNSET)

        city = d.pop("city", UNSET)

        state = d.pop("state", UNSET)

        country_code = d.pop("countryCode", UNSET)

        lat = d.pop("lat", UNSET)

        lng = d.pop("lng", UNSET)

        bedrooms = d.pop("bedrooms", UNSET)

        bathrooms = d.pop("bathrooms", UNSET)

        beds = d.pop("beds", UNSET)

        person_capacity = d.pop("personCapacity", UNSET)

        summary = d.pop("summary", UNSET)

        description = d.pop("description", UNSET)

        default_daily_price = d.pop("defaultDailyPrice", UNSET)

        cleaning_fee = d.pop("cleaningFee", UNSET)

        _cancellation_policy = d.pop("cancellationPolicy", UNSET)
        cancellation_policy: ListingCreateRequestCancellationPolicy | Unset
        if isinstance(_cancellation_policy,  Unset):
            cancellation_policy = UNSET
        else:
            cancellation_policy = ListingCreateRequestCancellationPolicy(_cancellation_policy)




        check_in_time_start = d.pop("checkInTimeStart", UNSET)

        check_out_time = d.pop("checkOutTime", UNSET)

        allows_pets = d.pop("allowsPets", UNSET)

        allows_smoking = d.pop("allowsSmoking", UNSET)

        allows_children = d.pop("allowsChildren", UNSET)

        allows_events = d.pop("allowsEvents", UNSET)

        listing_create_request = cls(
            name=name,
            property_type=property_type,
            street=street,
            city=city,
            state=state,
            country_code=country_code,
            lat=lat,
            lng=lng,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            beds=beds,
            person_capacity=person_capacity,
            summary=summary,
            description=description,
            default_daily_price=default_daily_price,
            cleaning_fee=cleaning_fee,
            cancellation_policy=cancellation_policy,
            check_in_time_start=check_in_time_start,
            check_out_time=check_out_time,
            allows_pets=allows_pets,
            allows_smoking=allows_smoking,
            allows_children=allows_children,
            allows_events=allows_events,
        )


        listing_create_request.additional_properties = d
        return listing_create_request

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
