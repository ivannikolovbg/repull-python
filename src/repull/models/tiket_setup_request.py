from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.tiket_setup_request_action import TiketSetupRequestAction
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.tiket_setup_request_contacts_item import TiketSetupRequestContactsItem
  from ..models.tiket_setup_request_properties_item import TiketSetupRequestPropertiesItem





T = TypeVar("T", bound="TiketSetupRequest")



@_attrs_define
class TiketSetupRequest:
    """ Fields depend on `action`. Every action except `create-property`, `request-activation` and `check-activation` names
    a property with `property_id` or, for a property Repull created that tiket.com has not assigned an id to yet,
    `partner_hotel_code`.

        Attributes:
            action (TiketSetupRequestAction):
            property_id (str | Unset): tiket.com Hotel ID.
            partner_hotel_code (str | Unset): Repull's code for a property Repull created.
            listing_id (int | Unset): `create-property`, `add-room`, `add-rate-plan`: the listing whose content is used.
            hotel_id (str | Unset): `set-tiket-hotel-id`: the Hotel ID tiket.com assigned. `check-activation`: the Hotel ID
                to check.
            name (str | Unset): `create-property`, `add-room`, `add-rate-plan`: name on tiket.com.
            currency (str | Unset): `create-property`: ISO 4217. Example: IDR.
            property_type_id (int | Unset): `create-property`: tiket.com property type.
            latitude (float | Unset):
            longitude (float | Unset):
            address (str | Unset):
            postal_code (str | Unset):
            country_code (str | Unset):  Example: ID.
            state_code (str | Unset):
            company_name (str | Unset): `create-property`: the legal entity that operates the property.
            company_address (str | Unset):
            star_rating (float | Unset):
            pricing_model (str | Unset): `create-property`: `Room Based` or `Occupancy Based`.
            description (str | Unset):
            total_rooms (int | Unset):
            floors (int | Unset):
            when_built (int | Unset):
            contacts (list[TiketSetupRequestContactsItem] | Unset): `create-property`: property contacts.
            quantity (int | Unset): `add-room`: rooms of this type.
            max_adults (int | Unset):
            max_children (int | Unset):
            room_ids (list[str] | Unset): `add-rate-plan`: rooms the rate plan applies to.
            cancellation_policy (str | Unset): `add-rate-plan`.
            breakfast (bool | Unset): `add-rate-plan`: breakfast included.
            properties (list[TiketSetupRequestPropertiesItem] | Unset): `request-activation`: the properties to activate.
            rate_plan_ids (list[str] | Unset): `set-push-rate-plans`: the `ratePlanId`s that receive prices and
                restrictions.
            enabled (bool | Unset): `set-sync`: send calendar changes to tiket.com automatically.
     """

    action: TiketSetupRequestAction
    property_id: str | Unset = UNSET
    partner_hotel_code: str | Unset = UNSET
    listing_id: int | Unset = UNSET
    hotel_id: str | Unset = UNSET
    name: str | Unset = UNSET
    currency: str | Unset = UNSET
    property_type_id: int | Unset = UNSET
    latitude: float | Unset = UNSET
    longitude: float | Unset = UNSET
    address: str | Unset = UNSET
    postal_code: str | Unset = UNSET
    country_code: str | Unset = UNSET
    state_code: str | Unset = UNSET
    company_name: str | Unset = UNSET
    company_address: str | Unset = UNSET
    star_rating: float | Unset = UNSET
    pricing_model: str | Unset = UNSET
    description: str | Unset = UNSET
    total_rooms: int | Unset = UNSET
    floors: int | Unset = UNSET
    when_built: int | Unset = UNSET
    contacts: list[TiketSetupRequestContactsItem] | Unset = UNSET
    quantity: int | Unset = UNSET
    max_adults: int | Unset = UNSET
    max_children: int | Unset = UNSET
    room_ids: list[str] | Unset = UNSET
    cancellation_policy: str | Unset = UNSET
    breakfast: bool | Unset = UNSET
    properties: list[TiketSetupRequestPropertiesItem] | Unset = UNSET
    rate_plan_ids: list[str] | Unset = UNSET
    enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.tiket_setup_request_contacts_item import TiketSetupRequestContactsItem
        from ..models.tiket_setup_request_properties_item import TiketSetupRequestPropertiesItem
        action = self.action.value

        property_id = self.property_id

        partner_hotel_code = self.partner_hotel_code

        listing_id = self.listing_id

        hotel_id = self.hotel_id

        name = self.name

        currency = self.currency

        property_type_id = self.property_type_id

        latitude = self.latitude

        longitude = self.longitude

        address = self.address

        postal_code = self.postal_code

        country_code = self.country_code

        state_code = self.state_code

        company_name = self.company_name

        company_address = self.company_address

        star_rating = self.star_rating

        pricing_model = self.pricing_model

        description = self.description

        total_rooms = self.total_rooms

        floors = self.floors

        when_built = self.when_built

        contacts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.contacts, Unset):
            contacts = []
            for contacts_item_data in self.contacts:
                contacts_item = contacts_item_data.to_dict()
                contacts.append(contacts_item)



        quantity = self.quantity

        max_adults = self.max_adults

        max_children = self.max_children

        room_ids: list[str] | Unset = UNSET
        if not isinstance(self.room_ids, Unset):
            room_ids = self.room_ids



        cancellation_policy = self.cancellation_policy

        breakfast = self.breakfast

        properties: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = []
            for properties_item_data in self.properties:
                properties_item = properties_item_data.to_dict()
                properties.append(properties_item)



        rate_plan_ids: list[str] | Unset = UNSET
        if not isinstance(self.rate_plan_ids, Unset):
            rate_plan_ids = self.rate_plan_ids



        enabled = self.enabled


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "action": action,
        })
        if property_id is not UNSET:
            field_dict["property_id"] = property_id
        if partner_hotel_code is not UNSET:
            field_dict["partner_hotel_code"] = partner_hotel_code
        if listing_id is not UNSET:
            field_dict["listing_id"] = listing_id
        if hotel_id is not UNSET:
            field_dict["hotel_id"] = hotel_id
        if name is not UNSET:
            field_dict["name"] = name
        if currency is not UNSET:
            field_dict["currency"] = currency
        if property_type_id is not UNSET:
            field_dict["property_type_id"] = property_type_id
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if address is not UNSET:
            field_dict["address"] = address
        if postal_code is not UNSET:
            field_dict["postal_code"] = postal_code
        if country_code is not UNSET:
            field_dict["country_code"] = country_code
        if state_code is not UNSET:
            field_dict["state_code"] = state_code
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if company_address is not UNSET:
            field_dict["company_address"] = company_address
        if star_rating is not UNSET:
            field_dict["star_rating"] = star_rating
        if pricing_model is not UNSET:
            field_dict["pricing_model"] = pricing_model
        if description is not UNSET:
            field_dict["description"] = description
        if total_rooms is not UNSET:
            field_dict["total_rooms"] = total_rooms
        if floors is not UNSET:
            field_dict["floors"] = floors
        if when_built is not UNSET:
            field_dict["when_built"] = when_built
        if contacts is not UNSET:
            field_dict["contacts"] = contacts
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if max_adults is not UNSET:
            field_dict["max_adults"] = max_adults
        if max_children is not UNSET:
            field_dict["max_children"] = max_children
        if room_ids is not UNSET:
            field_dict["room_ids"] = room_ids
        if cancellation_policy is not UNSET:
            field_dict["cancellation_policy"] = cancellation_policy
        if breakfast is not UNSET:
            field_dict["breakfast"] = breakfast
        if properties is not UNSET:
            field_dict["properties"] = properties
        if rate_plan_ids is not UNSET:
            field_dict["rate_plan_ids"] = rate_plan_ids
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tiket_setup_request_contacts_item import TiketSetupRequestContactsItem
        from ..models.tiket_setup_request_properties_item import TiketSetupRequestPropertiesItem
        d = dict(src_dict)
        action = TiketSetupRequestAction(d.pop("action"))




        property_id = d.pop("property_id", UNSET)

        partner_hotel_code = d.pop("partner_hotel_code", UNSET)

        listing_id = d.pop("listing_id", UNSET)

        hotel_id = d.pop("hotel_id", UNSET)

        name = d.pop("name", UNSET)

        currency = d.pop("currency", UNSET)

        property_type_id = d.pop("property_type_id", UNSET)

        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        address = d.pop("address", UNSET)

        postal_code = d.pop("postal_code", UNSET)

        country_code = d.pop("country_code", UNSET)

        state_code = d.pop("state_code", UNSET)

        company_name = d.pop("company_name", UNSET)

        company_address = d.pop("company_address", UNSET)

        star_rating = d.pop("star_rating", UNSET)

        pricing_model = d.pop("pricing_model", UNSET)

        description = d.pop("description", UNSET)

        total_rooms = d.pop("total_rooms", UNSET)

        floors = d.pop("floors", UNSET)

        when_built = d.pop("when_built", UNSET)

        _contacts = d.pop("contacts", UNSET)
        contacts: list[TiketSetupRequestContactsItem] | Unset = UNSET
        if _contacts is not UNSET:
            contacts = []
            for contacts_item_data in _contacts:
                contacts_item = TiketSetupRequestContactsItem.from_dict(contacts_item_data)



                contacts.append(contacts_item)


        quantity = d.pop("quantity", UNSET)

        max_adults = d.pop("max_adults", UNSET)

        max_children = d.pop("max_children", UNSET)

        room_ids = cast(list[str], d.pop("room_ids", UNSET))


        cancellation_policy = d.pop("cancellation_policy", UNSET)

        breakfast = d.pop("breakfast", UNSET)

        _properties = d.pop("properties", UNSET)
        properties: list[TiketSetupRequestPropertiesItem] | Unset = UNSET
        if _properties is not UNSET:
            properties = []
            for properties_item_data in _properties:
                properties_item = TiketSetupRequestPropertiesItem.from_dict(properties_item_data)



                properties.append(properties_item)


        rate_plan_ids = cast(list[str], d.pop("rate_plan_ids", UNSET))


        enabled = d.pop("enabled", UNSET)

        tiket_setup_request = cls(
            action=action,
            property_id=property_id,
            partner_hotel_code=partner_hotel_code,
            listing_id=listing_id,
            hotel_id=hotel_id,
            name=name,
            currency=currency,
            property_type_id=property_type_id,
            latitude=latitude,
            longitude=longitude,
            address=address,
            postal_code=postal_code,
            country_code=country_code,
            state_code=state_code,
            company_name=company_name,
            company_address=company_address,
            star_rating=star_rating,
            pricing_model=pricing_model,
            description=description,
            total_rooms=total_rooms,
            floors=floors,
            when_built=when_built,
            contacts=contacts,
            quantity=quantity,
            max_adults=max_adults,
            max_children=max_children,
            room_ids=room_ids,
            cancellation_policy=cancellation_policy,
            breakfast=breakfast,
            properties=properties,
            rate_plan_ids=rate_plan_ids,
            enabled=enabled,
        )


        tiket_setup_request.additional_properties = d
        return tiket_setup_request

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
