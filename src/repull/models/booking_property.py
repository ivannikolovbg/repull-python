from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.booking_property_mapping_status import BookingPropertyMappingStatus
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.booking_property_listings_item import BookingPropertyListingsItem





T = TypeVar("T", bound="BookingProperty")



@_attrs_define
class BookingProperty:
    """ A Booking.com property this workspace holds, with the Repull listings mapped under it. A property is a building; its
    rooms are what guests book, and each room maps to one Repull listing — so one property commonly carries many
    listings.

        Attributes:
            connection_id (str | Unset): Repull-side id for this Booking.com connection.
            hotel_id (str | Unset): Booking.com hotel/property id. This is what `/v1/channels/booking/availability` takes as
                `property_id`.
            active (bool | Unset):
            sync_enabled (bool | Unset):
            booking_url (None | str | Unset):
            markup (None | str | Unset): The Booking.com markup on this property, as a fraction: "0.18" = +18%, shared by
                every listing on the property. Read or set it as a percentage with `/v1/listings/{id}/markups`.
            sync_category (None | str | Unset):
            suspended_at (datetime.datetime | None | Unset):
            suspension_reason (None | str | Unset):
            created_at (datetime.datetime | None | Unset):
            mapping_status (BookingPropertyMappingStatus | Unset): `mapped` — at least one room points at a listing.
                `unmapped` — the property is claimed but its rooms are not mapped yet, so `listings` is empty; finish `POST
                /v1/connect/booking/map-rooms`. An unmapped property is listed rather than hidden, so a half-finished connection
                is visible instead of looking like no connection at all.
            listings (list[BookingPropertyListingsItem] | Unset): The Repull listings mapped under this property. Empty when
                `mappingStatus` is `unmapped`. Inactive listings are left out.
     """

    connection_id: str | Unset = UNSET
    hotel_id: str | Unset = UNSET
    active: bool | Unset = UNSET
    sync_enabled: bool | Unset = UNSET
    booking_url: None | str | Unset = UNSET
    markup: None | str | Unset = UNSET
    sync_category: None | str | Unset = UNSET
    suspended_at: datetime.datetime | None | Unset = UNSET
    suspension_reason: None | str | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    mapping_status: BookingPropertyMappingStatus | Unset = UNSET
    listings: list[BookingPropertyListingsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.booking_property_listings_item import BookingPropertyListingsItem
        connection_id = self.connection_id

        hotel_id = self.hotel_id

        active = self.active

        sync_enabled = self.sync_enabled

        booking_url: None | str | Unset
        if isinstance(self.booking_url, Unset):
            booking_url = UNSET
        else:
            booking_url = self.booking_url

        markup: None | str | Unset
        if isinstance(self.markup, Unset):
            markup = UNSET
        else:
            markup = self.markup

        sync_category: None | str | Unset
        if isinstance(self.sync_category, Unset):
            sync_category = UNSET
        else:
            sync_category = self.sync_category

        suspended_at: None | str | Unset
        if isinstance(self.suspended_at, Unset):
            suspended_at = UNSET
        elif isinstance(self.suspended_at, datetime.datetime):
            suspended_at = self.suspended_at.isoformat()
        else:
            suspended_at = self.suspended_at

        suspension_reason: None | str | Unset
        if isinstance(self.suspension_reason, Unset):
            suspension_reason = UNSET
        else:
            suspension_reason = self.suspension_reason

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        mapping_status: str | Unset = UNSET
        if not isinstance(self.mapping_status, Unset):
            mapping_status = self.mapping_status.value


        listings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.listings, Unset):
            listings = []
            for listings_item_data in self.listings:
                listings_item = listings_item_data.to_dict()
                listings.append(listings_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if connection_id is not UNSET:
            field_dict["connectionId"] = connection_id
        if hotel_id is not UNSET:
            field_dict["hotelId"] = hotel_id
        if active is not UNSET:
            field_dict["active"] = active
        if sync_enabled is not UNSET:
            field_dict["syncEnabled"] = sync_enabled
        if booking_url is not UNSET:
            field_dict["bookingUrl"] = booking_url
        if markup is not UNSET:
            field_dict["markup"] = markup
        if sync_category is not UNSET:
            field_dict["syncCategory"] = sync_category
        if suspended_at is not UNSET:
            field_dict["suspendedAt"] = suspended_at
        if suspension_reason is not UNSET:
            field_dict["suspensionReason"] = suspension_reason
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if mapping_status is not UNSET:
            field_dict["mappingStatus"] = mapping_status
        if listings is not UNSET:
            field_dict["listings"] = listings

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.booking_property_listings_item import BookingPropertyListingsItem
        d = dict(src_dict)
        connection_id = d.pop("connectionId", UNSET)

        hotel_id = d.pop("hotelId", UNSET)

        active = d.pop("active", UNSET)

        sync_enabled = d.pop("syncEnabled", UNSET)

        def _parse_booking_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        booking_url = _parse_booking_url(d.pop("bookingUrl", UNSET))


        def _parse_markup(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        markup = _parse_markup(d.pop("markup", UNSET))


        def _parse_sync_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sync_category = _parse_sync_category(d.pop("syncCategory", UNSET))


        def _parse_suspended_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                suspended_at_type_0 = isoparse(data)



                return suspended_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        suspended_at = _parse_suspended_at(d.pop("suspendedAt", UNSET))


        def _parse_suspension_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        suspension_reason = _parse_suspension_reason(d.pop("suspensionReason", UNSET))


        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = isoparse(data)



                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("createdAt", UNSET))


        _mapping_status = d.pop("mappingStatus", UNSET)
        mapping_status: BookingPropertyMappingStatus | Unset
        if isinstance(_mapping_status,  Unset):
            mapping_status = UNSET
        else:
            mapping_status = BookingPropertyMappingStatus(_mapping_status)




        _listings = d.pop("listings", UNSET)
        listings: list[BookingPropertyListingsItem] | Unset = UNSET
        if _listings is not UNSET:
            listings = []
            for listings_item_data in _listings:
                listings_item = BookingPropertyListingsItem.from_dict(listings_item_data)



                listings.append(listings_item)


        booking_property = cls(
            connection_id=connection_id,
            hotel_id=hotel_id,
            active=active,
            sync_enabled=sync_enabled,
            booking_url=booking_url,
            markup=markup,
            sync_category=sync_category,
            suspended_at=suspended_at,
            suspension_reason=suspension_reason,
            created_at=created_at,
            mapping_status=mapping_status,
            listings=listings,
        )


        booking_property.additional_properties = d
        return booking_property

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
