from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.tiket_property_mapping_status import TiketPropertyMappingStatus
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.tiket_property_listings_item import TiketPropertyListingsItem
  from ..models.tiket_room import TiketRoom





T = TypeVar("T", bound="TiketProperty")



@_attrs_define
class TiketProperty:
    """ A tiket.com property connected to this workspace. A property is a hotel or building; its room types are what guests
    book, and each room type maps to one Repull listing.

        Attributes:
            property_id (None | str | Unset): tiket.com Hotel ID. `null` for a property Repull created that tiket.com has
                not assigned an id to yet.
            partner_hotel_code (None | str | Unset): Repull's code for a property Repull created on tiket.com.
            name (None | str | Unset):
            currency (None | str | Unset):  Example: IDR.
            price_model (None | str | Unset): `Room Based` (one `price` per night) or `Occupancy Based` (`occupancyPrices`
                per number of guests). Set per property in the tiket.com extranet. Example: Room Based.
            activation_status (None | str | Unset): Whether tiket.com has activated Repull as the property's channel
                manager, `awaiting_activation` until tiket.com activates Repull, then `active`; `disconnected` after
                `disconnect`.
            content_mapped (bool | None | Unset): `true` when tiket.com has linked Repull's codes to the property, so `POST
                /v1/listings/{id}/publish/tiket` can send content.
            sync_enabled (bool | None | Unset): Whether calendar changes are sent to tiket.com automatically (`set-sync`).
            last_products_at (datetime.datetime | None | Unset): When room types and rate plans were last read from
                tiket.com.
            last_error (None | str | Unset):
            mapping_status (TiketPropertyMappingStatus | Unset): `mapped` — every room type has a listing; `partial` — some
                do; `unmapped` — none (a real onboarding state, not an error).
            listings (list[TiketPropertyListingsItem] | Unset):
            rooms (list[TiketRoom] | Unset):
     """

    property_id: None | str | Unset = UNSET
    partner_hotel_code: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    currency: None | str | Unset = UNSET
    price_model: None | str | Unset = UNSET
    activation_status: None | str | Unset = UNSET
    content_mapped: bool | None | Unset = UNSET
    sync_enabled: bool | None | Unset = UNSET
    last_products_at: datetime.datetime | None | Unset = UNSET
    last_error: None | str | Unset = UNSET
    mapping_status: TiketPropertyMappingStatus | Unset = UNSET
    listings: list[TiketPropertyListingsItem] | Unset = UNSET
    rooms: list[TiketRoom] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.tiket_property_listings_item import TiketPropertyListingsItem
        from ..models.tiket_room import TiketRoom
        property_id: None | str | Unset
        if isinstance(self.property_id, Unset):
            property_id = UNSET
        else:
            property_id = self.property_id

        partner_hotel_code: None | str | Unset
        if isinstance(self.partner_hotel_code, Unset):
            partner_hotel_code = UNSET
        else:
            partner_hotel_code = self.partner_hotel_code

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        price_model: None | str | Unset
        if isinstance(self.price_model, Unset):
            price_model = UNSET
        else:
            price_model = self.price_model

        activation_status: None | str | Unset
        if isinstance(self.activation_status, Unset):
            activation_status = UNSET
        else:
            activation_status = self.activation_status

        content_mapped: bool | None | Unset
        if isinstance(self.content_mapped, Unset):
            content_mapped = UNSET
        else:
            content_mapped = self.content_mapped

        sync_enabled: bool | None | Unset
        if isinstance(self.sync_enabled, Unset):
            sync_enabled = UNSET
        else:
            sync_enabled = self.sync_enabled

        last_products_at: None | str | Unset
        if isinstance(self.last_products_at, Unset):
            last_products_at = UNSET
        elif isinstance(self.last_products_at, datetime.datetime):
            last_products_at = self.last_products_at.isoformat()
        else:
            last_products_at = self.last_products_at

        last_error: None | str | Unset
        if isinstance(self.last_error, Unset):
            last_error = UNSET
        else:
            last_error = self.last_error

        mapping_status: str | Unset = UNSET
        if not isinstance(self.mapping_status, Unset):
            mapping_status = self.mapping_status.value


        listings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.listings, Unset):
            listings = []
            for listings_item_data in self.listings:
                listings_item = listings_item_data.to_dict()
                listings.append(listings_item)



        rooms: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rooms, Unset):
            rooms = []
            for rooms_item_data in self.rooms:
                rooms_item = rooms_item_data.to_dict()
                rooms.append(rooms_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if property_id is not UNSET:
            field_dict["propertyId"] = property_id
        if partner_hotel_code is not UNSET:
            field_dict["partnerHotelCode"] = partner_hotel_code
        if name is not UNSET:
            field_dict["name"] = name
        if currency is not UNSET:
            field_dict["currency"] = currency
        if price_model is not UNSET:
            field_dict["priceModel"] = price_model
        if activation_status is not UNSET:
            field_dict["activationStatus"] = activation_status
        if content_mapped is not UNSET:
            field_dict["contentMapped"] = content_mapped
        if sync_enabled is not UNSET:
            field_dict["syncEnabled"] = sync_enabled
        if last_products_at is not UNSET:
            field_dict["lastProductsAt"] = last_products_at
        if last_error is not UNSET:
            field_dict["lastError"] = last_error
        if mapping_status is not UNSET:
            field_dict["mappingStatus"] = mapping_status
        if listings is not UNSET:
            field_dict["listings"] = listings
        if rooms is not UNSET:
            field_dict["rooms"] = rooms

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tiket_property_listings_item import TiketPropertyListingsItem
        from ..models.tiket_room import TiketRoom
        d = dict(src_dict)
        def _parse_property_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        property_id = _parse_property_id(d.pop("propertyId", UNSET))


        def _parse_partner_hotel_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        partner_hotel_code = _parse_partner_hotel_code(d.pop("partnerHotelCode", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))


        def _parse_price_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        price_model = _parse_price_model(d.pop("priceModel", UNSET))


        def _parse_activation_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        activation_status = _parse_activation_status(d.pop("activationStatus", UNSET))


        def _parse_content_mapped(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        content_mapped = _parse_content_mapped(d.pop("contentMapped", UNSET))


        def _parse_sync_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        sync_enabled = _parse_sync_enabled(d.pop("syncEnabled", UNSET))


        def _parse_last_products_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_products_at_type_0 = isoparse(data)



                return last_products_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_products_at = _parse_last_products_at(d.pop("lastProductsAt", UNSET))


        def _parse_last_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_error = _parse_last_error(d.pop("lastError", UNSET))


        _mapping_status = d.pop("mappingStatus", UNSET)
        mapping_status: TiketPropertyMappingStatus | Unset
        if isinstance(_mapping_status,  Unset):
            mapping_status = UNSET
        else:
            mapping_status = TiketPropertyMappingStatus(_mapping_status)




        _listings = d.pop("listings", UNSET)
        listings: list[TiketPropertyListingsItem] | Unset = UNSET
        if _listings is not UNSET:
            listings = []
            for listings_item_data in _listings:
                listings_item = TiketPropertyListingsItem.from_dict(listings_item_data)



                listings.append(listings_item)


        _rooms = d.pop("rooms", UNSET)
        rooms: list[TiketRoom] | Unset = UNSET
        if _rooms is not UNSET:
            rooms = []
            for rooms_item_data in _rooms:
                rooms_item = TiketRoom.from_dict(rooms_item_data)



                rooms.append(rooms_item)


        tiket_property = cls(
            property_id=property_id,
            partner_hotel_code=partner_hotel_code,
            name=name,
            currency=currency,
            price_model=price_model,
            activation_status=activation_status,
            content_mapped=content_mapped,
            sync_enabled=sync_enabled,
            last_products_at=last_products_at,
            last_error=last_error,
            mapping_status=mapping_status,
            listings=listings,
            rooms=rooms,
        )


        tiket_property.additional_properties = d
        return tiket_property

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
