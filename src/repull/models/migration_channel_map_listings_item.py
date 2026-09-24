from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.migration_channel_map_listings_item_airbnb_type_0 import MigrationChannelMapListingsItemAirbnbType0
  from ..models.migration_channel_map_listings_item_booking_type_0 import MigrationChannelMapListingsItemBookingType0
  from ..models.migration_channel_map_listings_item_vrbo_type_0 import MigrationChannelMapListingsItemVrboType0





T = TypeVar("T", bound="MigrationChannelMapListingsItem")



@_attrs_define
class MigrationChannelMapListingsItem:
    """ 
        Attributes:
            listing_id (None | str | Unset): The property in this workspace, when it came across.
            name (None | str | Unset):
            provider (str | Unset):
            external_listing_id (str | Unset): The listing id in the source PMS.
            airbnb (MigrationChannelMapListingsItemAirbnbType0 | None | Unset):
            booking (MigrationChannelMapListingsItemBookingType0 | None | Unset):
            vrbo (MigrationChannelMapListingsItemVrboType0 | None | Unset):
     """

    listing_id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    provider: str | Unset = UNSET
    external_listing_id: str | Unset = UNSET
    airbnb: MigrationChannelMapListingsItemAirbnbType0 | None | Unset = UNSET
    booking: MigrationChannelMapListingsItemBookingType0 | None | Unset = UNSET
    vrbo: MigrationChannelMapListingsItemVrboType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.migration_channel_map_listings_item_airbnb_type_0 import MigrationChannelMapListingsItemAirbnbType0
        from ..models.migration_channel_map_listings_item_booking_type_0 import MigrationChannelMapListingsItemBookingType0
        from ..models.migration_channel_map_listings_item_vrbo_type_0 import MigrationChannelMapListingsItemVrboType0
        listing_id: None | str | Unset
        if isinstance(self.listing_id, Unset):
            listing_id = UNSET
        else:
            listing_id = self.listing_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        provider = self.provider

        external_listing_id = self.external_listing_id

        airbnb: dict[str, Any] | None | Unset
        if isinstance(self.airbnb, Unset):
            airbnb = UNSET
        elif isinstance(self.airbnb, MigrationChannelMapListingsItemAirbnbType0):
            airbnb = self.airbnb.to_dict()
        else:
            airbnb = self.airbnb

        booking: dict[str, Any] | None | Unset
        if isinstance(self.booking, Unset):
            booking = UNSET
        elif isinstance(self.booking, MigrationChannelMapListingsItemBookingType0):
            booking = self.booking.to_dict()
        else:
            booking = self.booking

        vrbo: dict[str, Any] | None | Unset
        if isinstance(self.vrbo, Unset):
            vrbo = UNSET
        elif isinstance(self.vrbo, MigrationChannelMapListingsItemVrboType0):
            vrbo = self.vrbo.to_dict()
        else:
            vrbo = self.vrbo


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if name is not UNSET:
            field_dict["name"] = name
        if provider is not UNSET:
            field_dict["provider"] = provider
        if external_listing_id is not UNSET:
            field_dict["externalListingId"] = external_listing_id
        if airbnb is not UNSET:
            field_dict["airbnb"] = airbnb
        if booking is not UNSET:
            field_dict["booking"] = booking
        if vrbo is not UNSET:
            field_dict["vrbo"] = vrbo

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.migration_channel_map_listings_item_airbnb_type_0 import MigrationChannelMapListingsItemAirbnbType0
        from ..models.migration_channel_map_listings_item_booking_type_0 import MigrationChannelMapListingsItemBookingType0
        from ..models.migration_channel_map_listings_item_vrbo_type_0 import MigrationChannelMapListingsItemVrboType0
        d = dict(src_dict)
        def _parse_listing_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        listing_id = _parse_listing_id(d.pop("listingId", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        provider = d.pop("provider", UNSET)

        external_listing_id = d.pop("externalListingId", UNSET)

        def _parse_airbnb(data: object) -> MigrationChannelMapListingsItemAirbnbType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                airbnb_type_0 = MigrationChannelMapListingsItemAirbnbType0.from_dict(data)



                return airbnb_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MigrationChannelMapListingsItemAirbnbType0 | None | Unset, data)

        airbnb = _parse_airbnb(d.pop("airbnb", UNSET))


        def _parse_booking(data: object) -> MigrationChannelMapListingsItemBookingType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                booking_type_0 = MigrationChannelMapListingsItemBookingType0.from_dict(data)



                return booking_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MigrationChannelMapListingsItemBookingType0 | None | Unset, data)

        booking = _parse_booking(d.pop("booking", UNSET))


        def _parse_vrbo(data: object) -> MigrationChannelMapListingsItemVrboType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                vrbo_type_0 = MigrationChannelMapListingsItemVrboType0.from_dict(data)



                return vrbo_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MigrationChannelMapListingsItemVrboType0 | None | Unset, data)

        vrbo = _parse_vrbo(d.pop("vrbo", UNSET))


        migration_channel_map_listings_item = cls(
            listing_id=listing_id,
            name=name,
            provider=provider,
            external_listing_id=external_listing_id,
            airbnb=airbnb,
            booking=booking,
            vrbo=vrbo,
        )


        migration_channel_map_listings_item.additional_properties = d
        return migration_channel_map_listings_item

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
