from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.listing_create_request_cancellation_policy import ListingCreateRequestCancellationPolicy
from ..models.listing_create_request_room_type_category import ListingCreateRequestRoomTypeCategory
from ..types import UNSET, Unset






T = TypeVar("T", bound="ListingCreateRequest")



@_attrs_define
class ListingCreateRequest:
    """ Inputs for `POST /v1/listings`.

    **Address requirements — read this before you build the payload.** Publishing to Airbnb runs a create preflight that
    refuses the listing outright if the address is incomplete, and the refusal only surfaces later, at publish time.
    Airbnb requires `street` and `city` for every country. For a **US** property it additionally requires `state` and
    `postalCode`. Crucially, **omitting `countryCode` makes the listing behave as US**, so a listing created without a
    country needs `state` and `postalCode` too. Send `countryCode` explicitly for a non-US property. `lat`/`lng` alone
    are not enough — Airbnb rejects coordinates that are not backed by a full postal address. Use `GET
    /v1/listings/{id}/publish-status` to see which parts are still missing before you attempt a publish.

        Attributes:
            name (str): Public guest-facing title Example: Sunset Loft #2.
            property_type (str | Unset):  Example: apartment.
            room_type_category (ListingCreateRequestRoomTypeCategory | Unset): What the guest actually gets. Airbnb refuses
                to activate a listing that has not stated one, answering "Please specify a valid room type" — which reads like a
                beds problem and is not. It is never defaulted: most listings are an entire home, but hundreds are a private or
                hotel room, and publishing one of those as an entire home is a false claim about someone's property. Settable
                later with `PUT /v1/listings/{id}/content` under `details`. Example: entire_home.
            property_type_category (str | Unset): Airbnb's finer property-type category, when you know it. Optional.
            street (str | Unset): Street address including the number. Required by Airbnb for every country — a publish is
                refused without it. Example: 123 Main St.
            city (str | Unset): City / town. Required by Airbnb for every country — a publish is refused without it.
                Example: Miami Beach.
            state (str | Unset): State, province or region. **Required for a US property**, and a listing with no
                `countryCode` counts as US. Optional elsewhere, but stored and used wherever the channel carries it. Example:
                FL.
            postal_code (str | Unset): Postal code — ZIP in the US, postcode in the UK, and so on. **Required for a US
                property**, and a listing with no `countryCode` counts as US. Send the complete code: Booking.com rejects a
                partial postcode such as `SW6` where the full value is `SW6 1EP`. Alias: `zipcode`. Example: 33139.
            zipcode (str | Unset): Alias for `postalCode`, accepted because it is the field name on the Airbnb mirror.
                `postalCode` wins if you send both. Prefer `postalCode` — the field holds non-US postcodes too. Example: 33139.
            country_code (str | Unset): ISO-3166 alpha-2 country code. **Send this for any non-US property.** Omitting it
                does not mean "unknown" — the publish path treats a listing with no country as US, which then requires `state`
                and `postalCode` and will refuse the listing when they are absent. Example: US.
            lat (float | Unset): Latitude. Useful for map search, but never a substitute for the postal address — Airbnb
                rejects coordinates it cannot reconcile with a full address. Example: 25.7617.
            lng (float | Unset): Longitude. See `lat`. Example: -80.1918.
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
    room_type_category: ListingCreateRequestRoomTypeCategory | Unset = UNSET
    property_type_category: str | Unset = UNSET
    street: str | Unset = UNSET
    city: str | Unset = UNSET
    state: str | Unset = UNSET
    postal_code: str | Unset = UNSET
    zipcode: str | Unset = UNSET
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

        room_type_category: str | Unset = UNSET
        if not isinstance(self.room_type_category, Unset):
            room_type_category = self.room_type_category.value


        property_type_category = self.property_type_category

        street = self.street

        city = self.city

        state = self.state

        postal_code = self.postal_code

        zipcode = self.zipcode

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
        if room_type_category is not UNSET:
            field_dict["roomTypeCategory"] = room_type_category
        if property_type_category is not UNSET:
            field_dict["propertyTypeCategory"] = property_type_category
        if street is not UNSET:
            field_dict["street"] = street
        if city is not UNSET:
            field_dict["city"] = city
        if state is not UNSET:
            field_dict["state"] = state
        if postal_code is not UNSET:
            field_dict["postalCode"] = postal_code
        if zipcode is not UNSET:
            field_dict["zipcode"] = zipcode
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

        _room_type_category = d.pop("roomTypeCategory", UNSET)
        room_type_category: ListingCreateRequestRoomTypeCategory | Unset
        if isinstance(_room_type_category,  Unset):
            room_type_category = UNSET
        else:
            room_type_category = ListingCreateRequestRoomTypeCategory(_room_type_category)




        property_type_category = d.pop("propertyTypeCategory", UNSET)

        street = d.pop("street", UNSET)

        city = d.pop("city", UNSET)

        state = d.pop("state", UNSET)

        postal_code = d.pop("postalCode", UNSET)

        zipcode = d.pop("zipcode", UNSET)

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
            room_type_category=room_type_category,
            property_type_category=property_type_category,
            street=street,
            city=city,
            state=state,
            postal_code=postal_code,
            zipcode=zipcode,
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
